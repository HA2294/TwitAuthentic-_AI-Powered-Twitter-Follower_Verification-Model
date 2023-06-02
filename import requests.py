import socket
from bs4 import BeautifulSoup

target_host = "www.website.com" 
request = "GET / HTTP/1.1\r\nHost:"+ target_host + "\r\n\r\n"

socc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socc.connect((target_host,80))
socc.sendall(request.encode())

html_str = socc.recv(5000).decode()
print(BeautifulSoup(html_str, 'html.parser').prettify())



