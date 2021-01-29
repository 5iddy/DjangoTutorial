from django.urls import path, re_path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    re_path(r'^(?P<video_id>\w{11})/(?P<format_id>\d{3})$', views.download, name='download')
]