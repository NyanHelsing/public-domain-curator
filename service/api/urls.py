# -*- coding: utf-8 -*-
"""REST API URLs"""


from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers

from api import views
# from <app>.routers import router


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    # url(r'^', include(router.urls))
])
