"""
Core calculation engine for Vehicle MSRP Calculator
"""

import json
import os
from pathlib import Path
from typing import Dict, List
from models import VehicleInput, CalculationResult


class MSRPCalculator:
    """Main calculator class for vehicle MSRP"""
    
    def __init__(self):
        self.load_data()
    
    def load_data(self):
        """Load tariff, tax, and freight data"""
        # Get the directory containing this file
        base_dir = Path(__file__).resolve().parent.parent
        data_dir = base_dir / 'data'
        
        try:
            with open(data_dir / 'tariffs.json', 'r') as f:
                self.tariffs = json.load(f)
        except FileNotFoundError:
            self.tariffs = []
        
        try:
            with open(data_dir / 'taxes.json', 'r') as f:
                self.taxes = json.load(f)
        except FileNotFoundError:
            self.taxes = {}
        
        try:
            with open(data_dir / 'freight.json', 'r') as f:
                self.freight_data = json.load(f)
        except FileNotFoundError:
            self.freight_data = []
    
    def get_tariff(self, vehicle_input: VehicleInput) -> Dict:
        """Get tariff information for the vehicle"""
        for tariff in self.tariffs:
            if (tariff['origin'] == vehicle_input.production_country and
                tariff['destination'] == vehicle_input.destination_country and
                tariff['vehicle_type'] == vehicle_input.vehicle_type and
                tariff['propulsion'] == vehicle_input.propulsion):
                return tariff
        
        # Default tariff if not found
        return {
            'origin': vehicle_input.production_country,
            'destination': vehicle_input.destination_country,
            'vehicle_type': vehicle_input.vehicle_type,
            'propulsion': vehicle_input.propulsion,
            'base_tariff': 10.0,
            'fta_applicable': False,
            'fta_rate': 10.0,
            'special_tariff': 0.0,
            'effective_rate': 10.0,
            'source': 'Default WTO rate',
            'source_url': 'https://www.wto.org/',
            'last_updated': '2024-01-01'
        }
    
    def get_taxes(self, country: str) -> List[Dict]:
        """Get tax information for the destination country"""
        return self.taxes.get(country, [
            {
                'type': 'VAT',
                'rate': 20.0,
                'base': 'CIF_plus_duty',
                'source': 'Default rate',
                'source_url': ''
            }
        ])
    
    def get_freight_cost(self, vehicle_input: VehicleInput) -> Dict:
        """Get freight cost estimate"""
        for freight in self.freight_data:
            if (freight['origin'] == vehicle_input.production_country and
                freight['destination'] == vehicle_input.destination_country and
                freight['vehicle_type'] == vehicle_input.vehicle_type):
                return freight
        
        # Default freight estimate based on regions
        default_cost = self._estimate_default_freight(
            vehicle_input.production_country,
            vehicle_input.destination_country
        )
        
        return {
            'origin': vehicle_input.production_country,
            'destination': vehicle_input.destination_country,
            'vehicle_type': vehicle_input.vehicle_type,
            'cost': default_cost,
            'source': 'Estimated average shipping cost'
        }
    
    def _estimate_default_freight(self, origin: str, destination: str) -> float:
        """Estimate default freight cost based on origin-destination pair"""
        asia_countries = ['China', 'Japan', 'South Korea', 'Thailand', 'Indonesia', 'India', 'Vietnam', 'Philippines', 'Singapore']
        europe_countries = ['Germany', 'France', 'Italy', 'Spain', 'Sweden', 'Norway', 'Denmark', 'Belgium', 'UK']
        americas_countries = ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina']
        
        origin_region = 'other'
        dest_region = 'other'
        
        if origin in asia_countries:
            origin_region = 'asia'
        elif origin in europe_countries:
            origin_region = 'europe'
        elif origin in americas_countries:
            origin_region = 'americas'
        
        if destination in asia_countries:
            dest_region = 'asia'
        elif destination in europe_countries:
            dest_region = 'europe'
        elif destination in americas_countries:
            dest_region = 'americas'
        
        # Freight cost matrix
        if origin_region == dest_region:
            return 500.0  # Regional
        elif (origin_region == 'asia' and dest_region == 'europe') or \
             (origin_region == 'europe' and dest_region == 'asia'):
            return 1200.0
        elif (origin_region == 'asia' and dest_region == 'americas') or \
             (origin_region == 'americas' and dest_region == 'asia'):
            return 1500.0
        elif (origin_region == 'europe' and dest_region == 'americas') or \
             (origin_region == 'americas' and dest_region == 'europe'):
            return 2000.0
        else:
            return 1000.0
    
    def calculate(self, vehicle_input: VehicleInput) -> CalculationResult:
        """
        Calculate MSRP based on vehicle input
        
        Formula:
        CIF = FOB + Freight + Insurance
        Duty = CIF × Tariff Rate
        Tax Base = CIF + Duty (or other formula depending on country)
        Total Taxes = Tax Base × (VAT + Excise + Other Taxes)
        MSRP = CIF + Duty + Total Taxes + Margin
        """
        # Get data
        tariff_info = self.get_tariff(vehicle_input)
        tax_info = self.get_taxes(vehicle_input.destination_country)
        freight_info = self.get_freight_cost(vehicle_input)
        
        # Step 1: Calculate CIF
        fob_price = vehicle_input.fob_price
        freight_cost = freight_info['cost']
        insurance_cost = fob_price * 0.01  # 1% of FOB
        cif_value = fob_price + freight_cost + insurance_cost
        
        # Step 2: Calculate Duty
        tariff_rate = tariff_info['effective_rate']
        tariff_amount = cif_value * (tariff_rate / 100)
        
        # Step 3: Calculate Tax Base
        tax_base = cif_value + tariff_amount
        
        # Step 4: Calculate Taxes
        taxes_breakdown = []
        total_tax_rate = 0
        
        for tax in tax_info:
            if tax['base'] == 'CIF':
                tax_amount = cif_value * (tax['rate'] / 100)
            elif tax['base'] == 'CIF_plus_duty':
                tax_amount = tax_base * (tax['rate'] / 100)
            else:
                tax_amount = tax_base * (tax['rate'] / 100)
            
            taxes_breakdown.append({
                'type': tax['type'],
                'rate': tax['rate'],
                'amount': tax_amount,
                'source': tax['source'],
                'source_url': tax.get('source_url', ''),
                'note': tax.get('note', '')
            })
            total_tax_rate += tax['rate']
        
        total_taxes = sum(t['amount'] for t in taxes_breakdown)
        
        # Step 5: Calculate Margin and MSRP
        subtotal = cif_value + tariff_amount + total_taxes
        margin_rate = vehicle_input.target_margin
        margin_amount = subtotal * (margin_rate / 100)
        msrp = subtotal + margin_amount
        
        # Compile sources
        sources = {
            'tariff': {
                'source': tariff_info['source'],
                'url': tariff_info['source_url'],
                'last_updated': tariff_info['last_updated']
            },
            'freight': {
                'source': freight_info['source']
            },
            'taxes': [
                {
                    'type': t['type'],
                    'source': t['source'],
                    'url': t['source_url']
                }
                for t in taxes_breakdown
            ]
        }
        
        return CalculationResult(
            fob_price=fob_price,
            freight_cost=freight_cost,
            insurance_cost=insurance_cost,
            cif_value=cif_value,
            tariff_rate=tariff_rate,
            tariff_amount=tariff_amount,
            taxes=taxes_breakdown,
            total_taxes=total_taxes,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            msrp=msrp,
            sources=sources
        )
