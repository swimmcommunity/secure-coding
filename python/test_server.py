
import pytest

import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        with server.app.app_context():
            yield client


def test_hello_world(client):
    rv = client.get('/')
    assert rv.data == b'Hello from Swimm!'


def test_get_picture(client):
    rv = client.get('/picture?image_name=logo.png')
    assert rv.status_code == 200

    # No name
    rv = client.get('/picture')
    assert rv.status_code == 404

    # File doesn't exist
    rv = client.get('/picture?image_name=doesnt_exist.png')
    assert rv.status_code == 404

    # EVIL INJECTION
    rv = client.get('/picture?image_name=../../../password')
    assert rv.status_code == 403

def test_redirect_me(client):
    # No `next`
    rv = client.get('/redirect_me?no_next=bla')
    assert rv.status_code == 404

    # The address is not within our server
    rv = client.get('/redirect_me?next=https://www.google.com')
    assert rv.status_code == 401

    # Valid address
    rv = client.get('/redirect_me?next=http://localhost/something')
    assert rv.status_code == 302