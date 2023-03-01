

import threading
import http.server
import socketserver

from http.server import BaseHTTPRequestHandler, HTTPServer


def server(dir):
    def process():
        PORT = 50083
        class DevelopHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs, directory=dir)

            def do_GET(self):
                print("P1: "+self.path)
                f = self.send_head()
                #path = self.translate_path(self.path)
                #print("P2: "+path)
                print(f)
                #return http.server.SimpleHTTPRequestHandler.do_GET(self)

        with socketserver.TCPServer(("", PORT), DevelopHttpRequestHandler) as httpd:
            print("Server started at dir: " + dir)
            print("Server started at localhost: " + str(PORT))
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                httpd.server_close()
                httpd.shutdown()
                #sys.exit()
    return process

if __name__ == '__main__':
     process = server('.')
     process()