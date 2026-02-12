"""
Flask API for Vehicle MSRP Calculator
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dataclasses import asdict
from calculator import MSRPCalculator
from models import VehicleInput
import os

app = Flask(__name__, static_folder='..', static_url_path='')
CORS(app)

calculator = MSRPCalculator()

# Configuration data
PRODUCTION_COUNTRIES = [
    "China", "USA", "Germany", "UK", "France", "Italy", "Turkey", 
    "Japan", "South Korea", "India", "Thailand", "Indonesia", 
    "Mexico", "Brazil"
]

DESTINATION_COUNTRIES = [
    "China", "USA", "Germany", "France", "Italy", "Spain", "Sweden", 
    "Norway", "Denmark", "Belgium", "Turkey", "UK", "Thailand", 
    "Indonesia", "India", "Japan", "South Korea", "Singapore", 
    "Vietnam", "Philippines", "Australia", "Canada", "Mexico", 
    "Brazil", "Argentina"
]

VEHICLE_TYPES = [
    "Car", "SUV", "Pickup", "Van", "Truck"
]

PROPULSION_TYPES = [
    "Gasoline", "Diesel", "PHEV", "BEV", "HEV", "FCEV"
]


@app.route('/')
def index():
    """Serve the landing page"""
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/calculator')
def calculator_page():
    """Serve the calculator frontend"""
    return send_from_directory(os.path.join(app.static_folder, 'frontend'), 'calculator.html')


@app.route('/api/countries/production', methods=['GET'])
def get_production_countries():
    """Get list of production countries"""
    return jsonify({
        'countries': PRODUCTION_COUNTRIES
    })


@app.route('/api/countries/destination', methods=['GET'])
def get_destination_countries():
    """Get list of destination countries"""
    return jsonify({
        'countries': DESTINATION_COUNTRIES
    })


@app.route('/api/vehicle-types', methods=['GET'])
def get_vehicle_types():
    """Get list of vehicle types"""
    return jsonify({
        'types': VEHICLE_TYPES
    })


@app.route('/api/propulsion-types', methods=['GET'])
def get_propulsion_types():
    """Get list of propulsion systems"""
    return jsonify({
        'types': PROPULSION_TYPES
    })


@app.route('/api/calculate', methods=['POST'])
def calculate_msrp():
    """Calculate MSRP based on input parameters"""
    try:
        data = request.json
        
        # Validate required fields
        required_fields = [
            'vehicle_type', 'propulsion', 'fob_price', 
            'target_margin', 'production_country', 'destination_country'
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Create vehicle input
        vehicle_input = VehicleInput(
            vehicle_type=data['vehicle_type'],
            propulsion=data['propulsion'],
            fob_price=float(data['fob_price']),
            target_margin=float(data['target_margin']),
            production_country=data['production_country'],
            destination_country=data['destination_country']
        )
        
        # Calculate MSRP
        result = calculator.calculate(vehicle_input)
        
        # Convert to dict for JSON response
        response = {
            'fob_price': result.fob_price,
            'freight_cost': result.freight_cost,
            'insurance_cost': result.insurance_cost,
            'cif_value': result.cif_value,
            'tariff_rate': result.tariff_rate,
            'tariff_amount': result.tariff_amount,
            'taxes': result.taxes,
            'total_taxes': result.total_taxes,
            'margin_rate': result.margin_rate,
            'margin_amount': result.margin_amount,
            'msrp': result.msrp,
            'sources': result.sources
        }
        
        return jsonify(response)
    
    except ValueError as e:
        return jsonify({
            'error': f'Invalid input: {str(e)}'
        }), 400
    
    except Exception as e:
        return jsonify({
            'error': f'Calculation error: {str(e)}'
        }), 500


if __name__ == '__main__':
    # Note: Set debug=False in production
    # For development, you can set debug=True via environment variable
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
