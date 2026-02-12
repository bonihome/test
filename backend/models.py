"""
Data models for Vehicle MSRP Calculator
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class VehicleInput:
    """Input data for vehicle MSRP calculation"""
    vehicle_type: str
    propulsion: str
    fob_price: float
    target_margin: float
    production_country: str
    destination_country: str


@dataclass
class TariffInfo:
    """Tariff information for a specific vehicle and route"""
    origin: str
    destination: str
    vehicle_type: str
    propulsion: str
    base_tariff: float
    fta_applicable: bool
    fta_rate: float
    special_tariff: float
    effective_rate: float
    source: str
    source_url: str
    last_updated: str


@dataclass
class TaxInfo:
    """Tax information for a specific country"""
    type: str
    rate: float
    base: str
    source: str
    source_url: str
    note: Optional[str] = None


@dataclass
class FreightEstimate:
    """Freight cost estimate"""
    origin: str
    destination: str
    vehicle_type: str
    cost: float
    source: str


@dataclass
class CalculationResult:
    """Complete calculation result"""
    fob_price: float
    freight_cost: float
    insurance_cost: float
    cif_value: float
    tariff_rate: float
    tariff_amount: float
    taxes: List[dict]
    total_taxes: float
    margin_rate: float
    margin_amount: float
    msrp: float
    sources: dict
