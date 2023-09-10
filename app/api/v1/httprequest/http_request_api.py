from flask import Blueprint, request, jsonify
from ....exception.httprequest.http_error import HTTPError
from ....services.httprequest.http_request_service import HttpRequestService
from ....model.dto.httprequest.http_request import HttpRequestDTO
from ....authenticator.authenticate_request import authenticate_request

http_request_bp = Blueprint('request', __name__)
http_request_service = HttpRequestService()

@http_request_bp.before_request
def before_request():
    try:
        authenticate_request()
    except HTTPError as e:
        return jsonify({'error': e.message}), e.status_code

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
    http_request_dto = HttpRequestDTO.from_dict(request)
    http_request_service.add(http_request_dto)
    response_data = {'created_data': http_request_dto.to_dict()}
    return jsonify(response_data), 200

@http_request_bp.route('/<int:id>/update', methods=['POST'])
def update_request(id):
    http_request = HttpRequestDTO.from_dict(request, query_params={'id': id})
    http_request_service.update(http_request)
    response_data = {'id': id, 'updated_data': http_request.to_dict(), 'message': 'Request updated successfully'}
    return jsonify(response_data), 200

@http_request_bp.route('/<int:id>/delete', methods=['DELETE'])
def delete_request(id):
    http_request_service.delete(id)
    response_data = {'id': id, 'message': 'Request deleted successfully'}
    return jsonify(response_data), 200