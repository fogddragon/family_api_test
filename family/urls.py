from django.conf.urls import url

from . import api

urlpatterns = [
    url(r'^save_example/', api.SaveExampleApiView.as_view(), name="save_example"),
    url(r'^check_family/', api.CheckFamilyApiView.as_view(), name="check_family"),
]
