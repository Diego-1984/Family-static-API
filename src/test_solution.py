import pytest, os, sys, tempfile, mock, json
from flask import Flask

@pytest.fixture
def client():
    with mock.patch('flask.Flask', lambda x: Flask(x)):
        from app import app
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True

        with app.test_client() as client:
            # with app.app_context():
            #     app.init_db()
            yield client

        os.close(db_fd)
        os.unlink(app.config['DATABASE'])
	
@pytest.mark.it("The Family structure has to be initialized with the 3 members specified in the instructions")
def test_first_three(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 3

