from ..base import BaseDTO
from sqlalchemy import String, Integer, JSON, LargeBinary, ForeignKey, Column
from sqlalchemy.orm import relationship

class HttpRequestDataDTO(BaseDTO):

    __tablename__ = "http_request_data"

    request_id = Column(Integer, ForeignKey("http_request.id"))
    headers = Column(JSON)
    data_type = Column(String) # form_data or json_data
    data = Column(LargeBinary)
    
    httpRequest = relationship("HttpRequestDTO", back_populates="httpRequestData")

    def to_dict(self, include_relationships=False):
        return {
            "id": self.id,
            "headers": self.headers,
            "data_type": self.data_type,
            "data": self.data,
            "request_id": self.request_id,
            "create_date": self.create_date,
            "last_updated": self.last_updated
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            headers=data.get("headers"),
            data_type=data.get("data_type"),
            data=data.get("data"),
            request_id=data.get("request_id")
        )

    def __repr__(self) -> str:
        return f"<HttpRequestDataDTO(id={self.id}, headers={self.headers}, data_type={self.data_type}, data={self.data}, request_id={self.request_id}, create_date={self.create_date}, last_updated={self.last_updated})>"
