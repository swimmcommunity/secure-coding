
import pytest

import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        with server.app.app_context():
            yield client


def test_hello_world(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert rv.data == b'Hello from Swimm!'


def test_get_picture(client):
    """Start with a blank database."""

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

