import mysql.connector

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework import status, viewsets
from django.db import models
from django.contrib.auth.models import User

from django.shortcuts import render




# 如果登录成功，设置session
def login(request):
    username = request.session.get('username', '')
    error = request.session.get('error', '')
    if not username:
        request.session['error'] = ''
        return render(request, 'login.html', {'error': error})
    return HttpResponseRedirect('/mine/')

# 退出登录
def logout(request):
    request.session['username'] = ''
    request.session['error'] = ''
    return HttpResponseRedirect('/login/')


# 通过session判断用户是否已登录
def mine(request):
    if 'username' in request.POST:
        username = request.POST['username']
        passwd = request.POST['passwd']
        print('request.POST.username', username)
        print('request.POST.passwd', passwd)
        if passwd == 'xxx':
            request.session['username'] = username
            return render(request, 'index.html', {'username': username})
        else:
            request.session['error'] = 'true'
            return HttpResponseRedirect('/login/')
            # return render(request, 'login.html', {'error': 'true'})
    else:
        ss_username = request.session.get('username', '')
        print('ss_username', ss_username)
        if not ss_username:
            request.session['error'] = ''
            return HttpResponseRedirect('/login/')
        return render(request, 'index.html', {'username': ss_username})


def hello(request):
    context = {}
    context['title'] = 'Hello World!'
    context['content'] = 'hahahahaha'
    return render(request, 'hello.html', context)

@api_view(['GET'])
def getData(request):
    """
       GET请求获取数据.
    """

    token = request.META.get('TOKEN')
    print('request.methods', request.method)
    print('request.META', token)
    params = request.query_params
    params.token = token
    return Response({'data': '', 'message': params, 'code': 200})

@api_view(['POST'])
def postData(request):
    # fields = ('id', 'account_name', 'users', 'created')
    # name = models.CharField(u'姓名', max_length=100, default='no_name')
    # sex = models.CharField(u'性别', max_length=10, default='male')
    # age = models.CharField(u'年龄', max_length=3, default='0')
    """
       POST请求获取数据.
    """
    print(request.data)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="159357",
        database="test",
    )

    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("select  * from user")
    myresult = mycursor.fetchall()
    # # print myresult
    # for x in myresult:
    #     print(x['id'])

    mycursor.close()
    return Response({'data': '', 'message': myresult, 'code': 200})



# Create your views here.
# -*- coding: utf-8 -*-

# from rest_framework.views import APIView
#
# from rest_framework.permissions import AllowAny
# from rest_framework.schemas import SchemaGenerator
# from rest_framework.schemas.generators import LinkNode, insert_into
# from rest_framework.renderers import *
# from rest_framework_swagger import renderers
# from rest_framework.response import Response
#
# # from rest_framework.schemas import SchemaGenerator
# class MySchemaGenerator(SchemaGenerator):
#
#     def get_links(self, request=None):
#         # from rest_framework.schemas.generators import LinkNode,
#         links = LinkNode()
#
#         paths = []
#         view_endpoints = []
#         for path, method, callback in self.endpoints:
#             view = self.create_view(callback, method, request)
#             path = self.coerce_path(path, method, view)
#             paths.append(path)
#             view_endpoints.append((path, method, view))
#
#         # Only generate the path prefix for paths that will be included
#         if not paths:
#             return None
#         prefix = self.determine_path_prefix(paths)
#
#         for path, method, view in view_endpoints:
#             if not self.has_view_permissions(path, method, view):
#                 continue
#             link = view.schema.get_link(path, method, base_url=self.url)
#             # 添加下面这一行方便在views编写过程中自定义参数.
#             link._fields += self.get_core_fields(view)
#
#             subpath = path[len(prefix):]
#             keys = self.get_keys(subpath, method, view)
#
#             # from rest_framework.schemas.generators import LinkNode, insert_into
#             insert_into(links, keys, link)
#
#         return links
#
#     # 从类中取出我们自定义的参数, 交给swagger 以生成接口文档.
#     def get_core_fields(self, view):
#         return getattr(view, 'coreapi_fields', ())
#
# def DocParam(name="default", location="query", required=True, description=None, type="string", *args, **kwargs):
#     return coreapi.Field(name=name, location=location, required=required, description=description, type=type)
#
#
# class ReturnJson(APIView):
# 	"""
# 	retrieve:
# 		Return a user instance.
# 	"""
# 	coreapi_fields = (
# 		DocParam("name", description='test'),
# 		DocParam("nalanxiao", required=False, description='rohero'),
# 	)
# 	def get(self, request, *args, **kwargs):
# 		json_data = {'name': 'post', 'id': 0}
# 		return Response(json_data)
#
# 	def post(self, request, *args, **kwargs):
# 		json_data = {'name': 'post', 'id': 0}
# 		return Response(json_data)
#
# class SwaggerSchemaView(APIView):
#     _ignore_model_permissions = True
#     exclude_from_schema = True
#
#     # from rest_framework.permissions import AllowAny
#     permission_classes = [AllowAny]
#     # from rest_framework_swagger import renderers
#     # from rest_framework.renderers import *
#     renderer_classes = [
#         CoreJSONRenderer,
#         renderers.OpenAPIRenderer,
#         renderers.SwaggerUIRenderer
#     ]
#
#     def get(self, request):
#         generator = MySchemaGenerator(title='纳兰晓', description='''v1.0.0''')
#         schema = generator.get_schema(request=request)
#         # from rest_framework.response import Response
#         return Response(schema)
#
#
# class StudentsApiView(APIView):
# 	coreapi_fields = (
# 		DocParam("name", description='test'),
# 		DocParam("nalanxiao", required=False, description='rohero'),
# 	)
#
# 	def get(self,request,format=None):
# 		json_data = {'name': 'get', 'id': 1}
# 		return Response(json_data)
#
# 	def post(self,request, format=None):
# 		"""
# 		retrieve:
#         	Return a user instance.
# 		"""
# 		json_data = {'name': 'post', 'id': 0}
# 		return Response(json_data)