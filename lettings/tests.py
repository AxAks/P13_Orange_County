"""
Tests File for the lettings app using pytest (through pytest-django)
"""
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_index(client, test_lettings_list):
    """
    Checks that the lettings index page is well displayed
    """
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    response_decode = response.content.decode()
    assert 'Lettings' in response_decode
    assert "Good Bread" in response_decode
    assert 'Home' in response_decode
    assert 'Profiles' in response_decode


@pytest.mark.django_db
def test_one_letting(client, test_letting_id_as_str, test_letting_obj):
    """
    checks that the page for a specific profile is well displayed
    """
    response = client.get(reverse('lettings:letting', args={test_letting_id_as_str}))
    assert response.status_code == 200
    response_decode = response.content.decode()
    assert 'Man on the Floor' in response_decode
    assert '187 Redrum Alley' in response_decode
    assert 'Back' in response_decode
    assert 'Home' in response_decode
    assert 'Profiles' in response_decode
