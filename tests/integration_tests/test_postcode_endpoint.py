import pytest
from fastapi.testclient import TestClient
from task_2_main import create_application


@pytest.fixture()
def testing_app():
    app = create_application()
    testing_app = TestClient(app)
    return testing_app


def test_postcode_scurri(testing_app):
    response = testing_app.get('/?input_postcode={}'.format('wc2n 4js'.replace(" ", "%20")))
    assert response.status_code == 200


def test_postcode_special(testing_app):
    response = testing_app.get('/?input_postcode={}'.format('gy10 1SF'.replace(" ", "%20")))  # Belle Vue, Sark
    assert response.status_code == 200


def test_incorrect_postcode_length(testing_app):
    response = testing_app.get('/?input_postcode={}'.format('fsggsdgshd'.replace(" ", "%20")))
    assert response.status_code == 400
