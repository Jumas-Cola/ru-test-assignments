import socketserver
import http.server
import urllib.request
import requests
import io
from bs4 import BeautifulSoup
import re
import string
from urllib.parse import urljoin, urlparse


PORT = 9097


def text_modifier(text, re_from, re_to):
    soup = BeautifulSoup(text, 'html.parser')

    for tag in soup.html.find_all(text=True):
        if tag.parent.name not in ('script', 'style'):
            tag.string.replace_with(re.sub(re_from, re_to, tag.string))
    
    for a in soup.html.find_all('a'):
        parsed_url = urlparse(a.get('href'))
        if parsed_url.netloc == 'habr.com':
            a['href'] = urljoin(f'http://127.0.0.1:{PORT}', parsed_url.path)

    return str(soup)


class HabrProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = urljoin('https://habr.com', self.path)
        self.send_response(200)
        self.end_headers()
        resp = urllib.request.urlopen(url) 
        resp_text = resp.read().decode()
        resp_text = text_modifier(resp_text, r'\b(\w{6})\b', r'\1™')
        self.copyfile(io.BytesIO(resp_text.encode()), self.wfile)


with socketserver.ForkingTCPServer(('', PORT), HabrProxy) as httpd:
    print('Now serving at', str(PORT))
    httpd.serve_forever()
