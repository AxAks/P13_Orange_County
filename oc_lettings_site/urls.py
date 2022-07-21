from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
]
