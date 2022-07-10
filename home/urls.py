from django.urls import path
from home import views
from home.views import trigger_error

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('sentry-debug/', trigger_error, name='sentry-error')  # just for tests
    ]
