#mandserver
#simple amnd server that returns pngs for a mandelbrot
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import mandelbrot
use_threaded_server = True
if use_threaded_server:
    from SocketServer import ThreadingMixIn

import cStringIO


class MandServer(BaseHTTPRequestHandler):
    cache = {}

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "image/png")
        self.end_headers()
        #we'll skip the leading slash
        if self.path not in self.cache:
            coords = self.path[1:].split('/')
            print self.path
            start = -1, -1
            end = 1, 1
            iters = 16
            if len(coords) >= 2:
                start = float(coords[0]), float(coords[1])
            if len(coords) >= 4:
                end = float(coords[2]), float(coords[3])
            if len(coords) >= 5:
                iters = int(coords[4])
            print "requesting ", iters, start, end
            memFile = cStringIO.StringIO()
            mandelbrot.mand_and_write(memFile, iters, start, end, 256)
            self.cache[self.path] = memFile
        else:
            print "Hitting cache!"
            memFile = self.cache[self.path]
        memFile.seek(0)
        self.wfile.write(memFile.read())


def main():
    httpserverclass = HTTPServer
    if use_threaded_server:
        class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
            pass
        httpserverclass = ThreadedHTTPServer

    try:
        server = httpserverclass(('', 8080), MandServer)
        print 'started MandServer...'
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
