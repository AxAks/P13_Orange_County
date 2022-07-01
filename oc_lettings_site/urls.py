from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def trigger_error(request):
    """
    just for tests
    """
    try:
        division_by_zero = 1 / 0
        return division_by_zero
    except ZeroDivisionError:
        return redirect('home:index')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('sentry-debug/', trigger_error)  # just for tests
]
