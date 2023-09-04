from ..repository_dao import RepositoryDAO
from ...dto.httprequest.http_request import HttpRequestDTO
from ...dto.httprequest.http_request_data import HttpRequestDataDTO
from ....dbconnector.db_connector_manager import DatabaseConnectionManager
from sqlalchemy import select

class HttpRequestRepository(RepositoryDAO[HttpRequestDTO]):
    def __init__(self, connection_manager: DatabaseConnectionManager):
        super().__init__(connection_manager, HttpRequestDTO)

    def get_data_by_request_id(self, request_id: int):
        session = self._get_session()
        stmt = (
            select(HttpRequestDTO, HttpRequestDataDTO)
            .join(HttpRequestDataDTO, HttpRequestDTO.id == HttpRequestDataDTO.request_id)
            .where(HttpRequestDTO.id == request_id)
        )
        return session.execute(stmt).all()