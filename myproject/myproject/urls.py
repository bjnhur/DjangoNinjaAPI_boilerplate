"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from myapi.api import api as myapi_router

# from myapi.api_v2 import router as myapi_router_v2

# urls_namespace doc:
# https://django-ninja.rest-framework.com/guides/versioning/
# Routers doc:
# https://django-ninja.rest-framework.com/guides/routers/
api = NinjaAPI(urls_namespace="bbbapi", version="1.0.1", title="My API")
api.add_router("my", myapi_router)
# api_v2 = NinjaAPI(urls_namespace="bbbapi_v2", version="2.0.1", title="My API")
# api_v2.add_router("my", myapi_router_v2)

urlpatterns = [
    path("admin/", admin.site.urls),
    # API urls
    path("v1/", api.urls),
    # path("v2/", api_v2.urls),
]
