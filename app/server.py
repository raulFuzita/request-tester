from flask import Flask
from .api.v1.httprequest.http_request_api import http_request_bp

app = Flask(__name__)

app.register_blueprint(http_request_bp, url_prefix='/api/v1/request')

if __name__ == '__main__':
    print("Server is running!")
    app.run(debug=True)
    print("Server is stopped!")