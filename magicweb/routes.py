from parse import parse
import os
from webob import Request, Response

def run(app, host='0.0.0.0', port=5000):
      from waitress import serve
      serve(app, host=host, port=port)
class App:
    def __init__(self, frontend_folder="html"):
        self.routes = {}
        self.html = frontend_folder
    def render(self, html_file, response):
      with open(os.path.join(self.html, html_file)) as html:
        content = html.read()
      response.status_code = 200
      response.text = content

    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def route(self, path):
        assert path not in self.routes, f"Such a route {path} already exists"
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named

        return None, None

    def handle_request(self, request):
        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response