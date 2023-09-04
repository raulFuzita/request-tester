from ..base import BaseDTO
from .http_request_data import HttpRequestDataDTO
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

class HttpRequestDTO(BaseDTO):

    __tablename__ = "http_request"

    url = Column(String)
    method = Column(String)
    
    httpRequestData = relationship(
        "HttpRequestDataDTO",
        back_populates="httpRequest",
        cascade="all, delete-orphan"
    )

    def to_dict(self, include_relationships=True):
        result = {
            "id": self.id,
            "url": self.url,
            "method": self.method,
            "create_date": self.create_date,
            "last_updated": self.last_updated
        }
        if include_relationships:
            result["httpRequestData"] = [http_request_data.to_dict() for http_request_data in self.httpRequestData]

        return result
    
    @classmethod
    def from_dict(cls, data):
        httpRequestData = data.get("httpRequestData")
        if httpRequestData is None:
            httpRequestData = []
        return cls(
            id=data.get("id"),
            url=data.get("url"),
            method=data.get("method"),
            httpRequestData=[HttpRequestDataDTO.from_dict(http_request_data) for http_request_data in httpRequestData]
        )

    def __repr__(self) -> str:
        return f"<HttpRequestDTO(id={self.id}, url={self.url}, method={self.method}, httpRequestData={self.httpRequestData}, create_date={self.create_date}, last_updated={self.last_updated})>"
    