# -*- coding: utf-8 -*-
from django.conf.urls  import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = "data_platform"
urlpatterns = [
    url(r'^$', views.index_view.as_view(), name="index"),
    url(r'^accident_list/',views.get_accident_list.as_view(), name="accident_list"),
    url(r'^term_list/',views.get_term_list.as_view(), name="term_list"),
    url(r'^term/(?P<term_id>\d+)$', views.get_term_detail.as_view(), name="term_detail"),
    url(r'^download/',views.get_download.as_view(), name="download"),
    url(r'^model_data/',views.get_model_data.as_view(), name="model_data"),
    url(r'^fm_list/',views.get_fm_list.as_view(), name="fm_list"),
]