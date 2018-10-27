# BasicHTTPServer
Very basic HTTP server for serving files in a directory. This is not designed to host any production code, rather it is for serving up a directory quick for sharing a file or running a reveal.js presentation.

## Usage
By default the server will listen on 127.0.0.1 on port 8000 and serve files located in the current directory.

Run with defaults
```
python server.py
```
Specify port to listen on 
```
python server.py --ipaddr 0.0.0.0
```
Bind to specific port
```
python server.py --port 10000
```
Specify directory to serve
```
python server.py /path/to/my/files/
```
