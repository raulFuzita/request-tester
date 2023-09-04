from ..repository_dao import RepositoryDAO
from ...dto.httprequest.http_request_data import HttpRequestDataDTO
from ....dbconnector.db_connector_manager import DatabaseConnectionManager

class HttpRequestDataRepository(RepositoryDAO[HttpRequestDataDTO]):
    def __init__(self, connection_manager: DatabaseConnectionManager):
        super().__init__(connection_manager, HttpRequestDataDTO)