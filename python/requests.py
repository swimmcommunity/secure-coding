import requests
import socket
import ssl

def my_get(url):
    return requests.get(url)


def my_ssl_connection(remote_host):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname, ssl_version=ssl.PROTOCOL_SSLv23) as ssock:
            print(ssock.version())
