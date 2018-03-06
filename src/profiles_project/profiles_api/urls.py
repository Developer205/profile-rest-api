from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^hellow-view/', views.HelloApiView.as_view()),
]
