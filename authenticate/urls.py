from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^get_token/', views.get_token, name='get_token'),
]

