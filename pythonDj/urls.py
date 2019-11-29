"""pythonDj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
from . import views
# from .views import SwaggerSchemaView, ReturnJson, StudentsApiView
urlpatterns = [
    # url(r'^$', schema_view),
    # path('', schema_view),
    path('', include_docs_urls(title='API', description='前端接口文档')),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('login/', views.login),
    path('logout/', views.logout),
    path('mine/', views.mine),
    path('getData', views.getData),
    path('postData', views.postData),

    # url(r'^api/$', ReturnJson.as_view(), name='api'),
    # url(r'^api/v1/$', StudentsApiView.as_view(), name='api_v1'),
    # url(r'^docs/', SwaggerSchemaView.as_view(), name='apiDocs'),
]
