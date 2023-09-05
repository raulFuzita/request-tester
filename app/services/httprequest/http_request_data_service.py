from ...model.repository.httprequest.http_request_repository import HttpRequestRepository
from ...model.dto.httprequest.http_request_data import HttpRequestDataDTO
from ...dbconnector.db_connection_factory import DatabaseConnectionManagerFactory

class HttpRequestDataService:

    def __init__(self):
        self.db_manager = DatabaseConnectionManagerFactory.get_instance("sqlite:///database.db")
        self.repository = HttpRequestRepository(self.db_manager)
    
    def add(self, cls: HttpRequestDataDTO):
        return self.repository.add(cls)

    def get_by_id(self, cls_id: int) -> HttpRequestDataDTO:
        return self.repository.get_by_id(cls_id)

    def get_all(self):
        return self.repository.get_all()

    def update(self, cls: HttpRequestDataDTO):
        self.repository.update(cls)

    def delete(self, cls_id: int):
        self.repository.delete(cls_id)