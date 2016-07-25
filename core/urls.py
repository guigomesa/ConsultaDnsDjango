from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^consulta', views.consulta, name='consulta'),
    url(r'^$', views.index, name='index'),

]