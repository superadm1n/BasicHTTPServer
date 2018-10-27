#!/usr/bin/python

'''
Copyright 2018 Kyle Kowalczyk

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Basic HTTP server written in python to serve static web pages
'''

import http.server
import socketserver
import argparse
import os


def analyze_webdir(webdir):
    if args.webdir[0] == '/':
        dir = os.path.abspath(webdir)
    else:
        dir = os.path.dirname(os.path.abspath(webdir))

    return dir

parser = argparse.ArgumentParser("server.py")
parser.add_argument("--port", help="Port to serve on (Default: 8000)", type=int)
parser.add_argument("--ipaddr", help="IP Address to serve on (Default: 127.0.0.1)", type=str)
parser.add_argument("--webdir", help="Directory to serve (Default will serve the directory the file is in)", type=str)
args = parser.parse_args()

if not args.port:
    port = 8000
else:
    port = args.port

if not args.ipaddr:
    ipaddr = '127.0.0.1'
else:
    ipaddr = args.ipaddr

# changes directory to serve that directory if specified
if args.webdir:
    os.chdir(args.webdir)
    webdir = analyze_webdir(args.webdir)
else:
    webdir = os.path.dirname(os.path.abspath(__file__))


Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((ipaddr, port), Handler)

try:
    print("Serving directory '{}' on port {} bound to address {}".format(webdir, port, ipaddr))
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
