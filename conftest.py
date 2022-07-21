"""
Tests Conf File for pytest
"""

import pytest
from typing import List

from django.contrib.auth.models import User
from lettings.models import Letting, Address
from profiles.models import Profile


@pytest.fixture
def test_profiles_list() -> List[Profile]:
    """
    Emulates a list of Profiles (with associated user) for the profile index page
    """
    test_profiles_list = []
    User.objects.get_or_create(
        id=1,
        first_name='test first',
        last_name='test profile',
        password='hello',
        username='test_profile',
        email='test_profile@email.com',
        is_active=True
        )
    User.objects.get_or_create(
        id=2,
        first_name='test second',
        last_name='test profile two',
        password='helloworld',
        username='test_profile2',
        email='test_profile_two@email.com',
        is_active=True
        )

    profile1 = Profile.objects.get_or_create(
        favorite_city='test city',
        user_id=1)
    profile2 = Profile.objects.get_or_create(
        favorite_city='test city two',
        user_id=2)

    test_profiles_list.append(profile1)
    test_profiles_list.append(profile2)
    return test_profiles_list


@pytest.fixture
def test_profile_three_string() -> str:
    """
    Replaces the username of a user
    to serve as argument in the specific profile page URI
    """
    return 'test_profile3'


@pytest.fixture
def test_profile_three_obj() -> Profile:
    """
     Emulates a Profile (along with the corresponding user) for the specific profile page
    """
    User.objects.get_or_create(
        id=3,
        first_name='test third',
        last_name='test profile three',
        password='helloall',
        username='test_profile3',
        email='test_profile_three@email.com',
        is_active=True
        )
    test_profile3 = Profile.objects.get_or_create(
        favorite_city='test city three',
        user_id=3)
    return test_profile3


@pytest.fixture
def test_lettings_list() -> List[Letting]:
    """
    Emulates a list of Lettings (with associated Addresses) for the letting index page
    """
    test_lettings_list = []
    Address.objects.get_or_create(
        id=1,
        number='28',
        street='Baker Street',
        city='Green City',
        state='WI',
        zip_code='23878',
        country_iso_code='USA'),
    Address.objects.get_or_create(
        id=2,
        number='4387',
        street='Miller Street',
        city='Big Rocky Mountain',
        state='CO',
        zip_code='43009',
        country_iso_code='USA'),

    letting1 = Letting.objects.get_or_create(
        id=1,
        title="Good Bread",
        address_id=1)
    letting2 = Letting.objects.get_or_create(
        id=2,
        title='Top of the Hill',
        address_id=2)

    test_lettings_list.append(letting1)
    test_lettings_list.append(letting2)
    return test_lettings_list


@pytest.fixture
def test_letting_id_as_str() -> str:
    """
    Replaces the id of a letting
    to serve as argument in the specific letting page URI
    """
    return '3'


@pytest.fixture
def test_letting_obj() -> Letting:
    """
    Emulates a Letting (along with the corresponding address) for the specific letting page
    """
    Address.objects.get_or_create(
        id=3,
        number='187',
        street='Redrum Alley',
        city='Chicago',
        state='IL',
        zip_code='43543',
        country_iso_code='USA'),

    letting3 = Letting.objects.get_or_create(
        id=3,
        title="Man on the Floor",
        address_id=3)

    return letting3
