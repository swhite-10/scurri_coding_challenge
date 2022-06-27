import pytest

from task_2.services.ukpostcode import GetPostcode


@pytest.fixture
def scurri_uk_address():
    return GetPostcode('wc2n 4js')


@pytest.fixture
def special_case_postcode():
    return GetPostcode('gy10 1SF')  # Belle Vue, Sark


@pytest.fixture
def incorrect_postcode_length():
    return GetPostcode('fsfasgsasfssa')


def test_postcode_scurri(scurri_uk_address):
    assert scurri_uk_address.postcode_formatter() is not None
    assert len(scurri_uk_address.postcode_formatter()) == 3
    assert scurri_uk_address.postcode_validator() is True


def test_postcode_special(special_case_postcode):
    assert special_case_postcode.postcode_formatter() is not None
    assert len(special_case_postcode.postcode_formatter()) == 3
    assert special_case_postcode.postcode_validator() is True


def test_postcode_incorrect_length(incorrect_postcode_length):
    assert incorrect_postcode_length.postcode_formatter() is None
    assert incorrect_postcode_length.postcode_validator() is False
