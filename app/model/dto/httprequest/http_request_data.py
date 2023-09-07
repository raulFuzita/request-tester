from ..base import BaseDTO
from sqlalchemy import String, Integer, JSON, LargeBinary, ForeignKey, Column
from sqlalchemy.orm import relationship
from urllib.parse import urlparse, parse_qs

class HttpRequestDataDTO(BaseDTO):

    __tablename__ = "http_request_data"

    request_id = Column(Integer, ForeignKey("http_request.id"))
    headers = Column(JSON)
    data = Column(JSON)
    
    httpRequest = relationship("HttpRequestDTO", back_populates="httpRequestData")

    def _get_query_params_from_url(url):
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query)

    def to_dict(self, include_relationships=False):
        return {
            "id": self.id,
            "headers": self.headers,
            "data": self.data,
            "request_id": self.request_id,
            "create_date": self.create_date,
            "last_updated": self.last_updated
        }
    
    @classmethod
    def from_dict(cls, request, query_params={}):
        kwargs = {
            'headers': dict(request.headers),
            'data': request.get_json(),
        }
        if 'id' in query_params:
            kwargs['id'] = query_params['id']
            kwargs['request_id'] = query_params['id']
        return cls(**kwargs)

    def __repr__(self) -> str:
        return f"<HttpRequestDataDTO(id={self.id}, headers={self.headers}, data={self.data}, request_id={self.request_id}, create_date={self.create_date}, last_updated={self.last_updated})>"
