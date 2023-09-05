import sys
import os
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the root directory by going up multiple levels
levels_up = 4  # Adjust this value based on your project structure
root_dir = os.path.abspath(os.path.join(script_dir, *([".."] * levels_up)))

# Add the root directory to sys.path
sys.path.append(root_dir)

# print("Modified sys.path:", sys.path)cls
import unittest
import requests
from urllib.parse import urlparse, parse_qs
from app.util.unittest.custom_test_runner import CustomTestRunner
from app.model.dto.httprequest import HttpRequestDTO
from app.model.dto.httprequest import HttpRequestDataDTO
from app.services.httprequest.http_request_service import HttpRequestService
from app.services.httprequest.http_request_data_service import HttpRequestDataService

class TestHttpRequest(unittest.TestCase):

    def test_http_request(self):
        query_params = {"param1": "value1", "param2": "value2"}
        requests_query_params = self._post_http_req_query_params(query_params)

        form_data = {"param1": "value1", "param2": "value2"}
        requests_form_data = self._post_http_req_form_data(form_data)

        json_data = {"param1": "value1", "param2": "value2"}
        requests_json_data = self._post_http_req_json_data(json_data)

        http_request_dto = HttpRequestDTO(
            method='POST',
            url='https://example.com/api',
            httpRequestData=[
                HttpRequestDataDTO(
                    headers=dict(requests_query_params.request.headers),
                    data_type='query_params', 
                    data=requests_query_params.content
                ),
                HttpRequestDataDTO(
                    headers=dict(requests_form_data.request.headers),
                    data_type='form_data', 
                    data=requests_form_data.content
                ),
                HttpRequestDataDTO(
                    headers=dict(requests_json_data.request.headers),
                    data_type='json_data', 
                    data=requests_json_data.content
                )
            ]
        )

        http_request_service = HttpRequestService()
        http_request_service.add(http_request_dto)
        http_req_saved = http_request_service.get_by_id(http_request_dto.id)
        self.assertEqual(http_req_saved.id, http_request_dto.id, "Expected id to be the same")
        print(http_req_saved.to_dict())

        http_request_data_service = HttpRequestDataService()
        http_req_data_saved = http_request_data_service.get_by_id(http_request_dto.httpRequestData[0].id)
        self.assertEqual(http_req_data_saved.id, http_request_dto.httpRequestData[0].id, "Expected id to be the same")

        result = http_request_service.get_data_by_request_id(http_request_dto.id)
        # Adding assertions
        self.assertIsNotNone(result, "Result should not be None")
        self.assertTrue(len(result) > 0, "Result should have at least one record")
        for record in result:
            http_request, http_request_data = record
            self.assertIsInstance(http_request, HttpRequestDTO, "Expected type HttpRequestDTO")
            self.assertIsInstance(http_request_data, HttpRequestDataDTO, "Expected type HttpRequestDataDTO")
            self.assertEqual(http_request.method, 'POST', "Expected method to be POST")


    def test_http_request_with_no_data(self):
        http_request_dto = HttpRequestDTO(
            method='POST',
            url='https://example.com/api'
        )
        http_request_service = HttpRequestService()
        http_request_service.add(http_request_dto)
        http_req_saved = http_request_service.get_by_id(http_request_dto.id)
        self.assertEqual(http_req_saved.id, http_request_dto.id, "Expected id to be the same")

        result = http_request_service.get_data_by_request_id(http_request_dto.id)
        self.assertIsNotNone(result, "Result should not be None")
        self.assertTrue(len(result) == 0, "Result should have at least one record")

    
    def _post_http_req_query_params(self, query_params: str):
        url = "https://example.com/api"
        params = {"param1": "value1", "param2": "value2"}
        headers = {"Content-Type": "application/form-data"}
        return requests.post(url, params=params, headers=headers)
    
    def _post_http_req_form_data(self, form_data: str):
        url = "https://example.com/api"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        return requests.post(url, data=form_data, headers=headers)
    
    def _post_http_req_json_data(self, json_data: str):
        url = "https://example.com/api"
        headers = {"Content-Type": "application/json"}
        return requests.post(url, json=json_data, headers=headers)
    
    def _get_query_params_from_url(url):
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query)

    def _get_http_request_dto_from_request(self, response):
        request = response.request
        return HttpRequestDTO(
            method=request.method,
            url=request.url,
            headers=dict(request.headers),
            body=request.body,
            query_params=self._get_query_params_from_url(request.url)
        )

if __name__ == '__main__':
    runner = CustomTestRunner()
    runner.log_failures = True
    runner.log_exceptions = True
    unittest.main(testRunner=runner)