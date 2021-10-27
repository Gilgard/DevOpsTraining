from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views

app_name = 'accounts'

urlpatterns=[
    url(r'^signup/$', views.signup_view, name="signup")
]