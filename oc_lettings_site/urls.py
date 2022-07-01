from django.contrib import admin
from django.urls import path, include


def trigger_error(request):  # just for tests
    try:
        division_by_zero = 1 / 0
    except ZeroDivisionError as e:
        print('hello Zero')
        raise ZeroDivisionError(e)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('sentry-debug/', trigger_error)  # just for tests
]
