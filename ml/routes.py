from flask import Blueprint, jsonify
from ml import model
from flask import request

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    return jsonify({"message": "Welcome to our API!"})


@api_bp.route('/api/model', methods=['POST'])
def predict():
    text = request.get_json().get('text')
    result = model.predict(text)
    return jsonify(result)