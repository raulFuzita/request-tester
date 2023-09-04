from ...model.repository.httprequest.http_request_repository import HttpRequestRepository
from ...model.dto.httprequest.http_request import HttpRequestDTO
from ...dbconnector.db_connection_factory import DatabaseConnectionManagerFactory

class HttpRequestService:

    def __init__(self):
        self.db_manager = DatabaseConnectionManagerFactory.get_instance("sqlite:///database.db")
        self.repository = HttpRequestRepository(self.db_manager)
    
    def add(self, cls: HttpRequestDTO):
        return self.repository.add(cls)

    def get_by_id(self, cls_id: int) -> HttpRequestDTO:
        return self.repository.get_by_id(cls_id)

    def get_all(self):
        print(self.db_manager)
        return self.repository.get_all()

    def update(self, cls: HttpRequestDTO):
        self.repository.update(cls)

    def delete(self, cls_id: int):
        self.repository.delete(cls_id)

    def get_data_by_request_id(self, request_id: int):
        return self.repository.get_data_by_request_id(request_id)