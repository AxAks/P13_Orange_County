"""
Tests File for the profiles app using pytest (through pytest-django)
"""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profile_index(client, test_profiles_list):
    """
    Checks that the profiles index page is well displayed
    """
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    response_decode = response.content.decode()
    assert 'Profiles' in response_decode
    assert 'test_profile' in response_decode
    assert 'Home' in response_decode
    assert 'Lettings' in response_decode


@pytest.mark.django_db
def test_one_profile(client, test_profile_three_string, test_profile_three_obj):
    """
    checks that the page for a specific profile is well displayed
    """
    response = client.get(reverse('profiles:profile', args={test_profile_three_string}))
    assert response.status_code == 200
    response_decode = response.content.decode()
    assert test_profile_three_string in response_decode
    assert 'First name: test third' in response_decode
    assert 'Last name: test profile three' in response_decode
    assert 'Email: test_profile_three@email.com' in response_decode
    assert 'Favorite city: test city three' in response_decode
    assert 'Back' in response_decode
    assert 'Home' in response_decode
    assert 'Lettings' in response_decode
