import SimpleHTTPServer
import SocketServer
import sys
import signal

def signal_handler(signal, frame):
        print('')
        sys.exit(0)

# Register a handler of <CTRL+C> to stop the server
signal.signal(signal.SIGINT, signal_handler)

PORT = 8000

if (len(sys.argv) > 1):
  PORT = int(sys.argv[1])

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()


