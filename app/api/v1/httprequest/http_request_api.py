from flask import Blueprint, request, jsonify
from ....services.httprequest.http_request_service import HttpRequestService
from ....model.dto.httprequest.http_request import HttpRequestDTO

http_request_bp = Blueprint('request', __name__)
http_request_service = HttpRequestService()

@http_request_bp.route('/', methods=['GET'])
def get_test_api():
    return jsonify({'message': 'Request API is running'}), 200

@http_request_bp.route('/all', methods=['GET'])
def get_all_request():
    http_request_all = http_request_service.get_all()
    http_request_all_dicts = [req.to_dict() for req in http_request_all]
    return jsonify(http_request_all_dicts), 200

@http_request_bp.route('/<int:id>', methods=['GET'])
def get_request(id):
    http_request = http_request_service.get_by_id(id)
    if http_request is None:
        return jsonify({'error': 'No request found with id {}'.format(id)}), 400
    return jsonify(http_request.to_dict()), 200

@http_request_bp.route('/add', methods=['POST'])
def add_request():
    data = request.get_json()
    http_request_dto = HttpRequestDTO.from_dict(data)
    http_request_service.add(http_request_dto)
    return jsonify({'created_data': data}), 200

@http_request_bp.route('/<int:id>/update', methods=['POST'])
def update_request(id):
    data = request.get_json()
    http_request = HttpRequestDTO.from_dict(data)
    http_request_service.update(http_request)
    return jsonify({'id': id, 'updated_data': data}), 200

@http_request_bp.route('/<int:id>/delete', methods=['DELETE'])
def delete_request(id):
    http_request_service.delete(id)
    return jsonify({'id': id}), 200