from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    return jsonify({"message": "Welcome to our API!"})

@api_bp.route('/api/data')
def get_data():
    data = {"key": "value"}  # Replace this with your actual data
    return jsonify(data)