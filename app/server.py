from flask import Flask
from .api.v1.httprequest.http_request_api import http_request_bp
from .authorization.httprequest import default_limit_ip_requests

app = Flask(__name__)

app.before_request(default_limit_ip_requests)

app.register_blueprint(http_request_bp, url_prefix='/api/v1/request')

app.route('/version')(lambda: "app version: 1.0.0.0")

if __name__ == '__main__':
    print("Server is running!")
    app.run(debug=True)
    print("Server is stopped!")