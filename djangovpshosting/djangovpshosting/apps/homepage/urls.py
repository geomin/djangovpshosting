from django.conf.urls import url

import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
