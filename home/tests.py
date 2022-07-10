"""
Tests File for the home app using pytest (through pytest-django)
"""

import pytest
from django.urls import reverse


def test_home_index(client):
    """
    checks that the homepage is well displayed
    """
    response = client.get(reverse('home:index'))
    assert response.status_code == 200
    response_decode = response.content.decode()
    assert 'Welcome to Holiday Homes' in response_decode
    assert 'Welcome to Holiday Homes' in response_decode
    assert 'Profiles' in response_decode
    assert 'Lettings' in response_decode


def test_trigger_error(client):
    """
    Checks that the example error for sentry raises a ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError):
        assert client.get(reverse('home:sentry-error'))
