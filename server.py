from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import os
import json


httpcow = '''<!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/cow">cowsay</a></li>
        </ul>
        </nav>
    <header>
    <main>
        <!-- project description defining how users can further interact with the application -->
    </main>
</body>
</html>'''


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        This method will allow you to send HTTP Requests
        """
        cheese = cow.Moose()
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        # set a status code
        # set any headers
        # set any body data on the response
        # end headers

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(httpcow.encode())
            return

        elif parsed_path.path == '/cow':
            try:
                if len(parsed_qs['msg'][0]) < 1:
                    self.send_response(400)
                    self.send_header('Content-Type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'400 Bad Request')
                    return
                msg = cheese.milk(parsed_qs['msg'][0])
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(f'''<html><body>{msg}</body></html>'''.encode())
                return
            except KeyError:
                self.send_response(400)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b'400 Bad Request')
                return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        """
        This is the method that will allow us to post
        """
        cheese = cow.Moose()
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        # set a status code
        # set any headers
        # set any body data on the response
        # end headers

        if parsed_path.path == '/cow':
            try:
                if len(parsed_qs['msg'][0]) < 1:
                    self.send_response(400)
                    self.send_header('Content-Type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'400 Bad Request')
                    return
                msg = cheese.milk(parsed_qs['msg'][0])
                return_json = f'{{"content": "{msg}"}}'
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(return_json.encode())
                return
            except KeyError:
                self.send_response(400)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b'400 Bad Request')
                return

        self.send_response(404)
        self.end_headers()


def create_server():
    """
    This method will create the server
    """
    return HTTPServer(
        ('127.0.0.1', int(os.environ['PORT'])),
        SimpleHTTPRequestHandler
    )


def run_forever():
    """
    This method will run the server until an interrupt occurs
    """
    server = create_server()

    try:
        print(f'Server running on {os.environ["PORT"]}')
        server.serve_forever()

    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
