"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
"""TY_IT_8Sept URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from newapp.views import view_hello,view_record,view_hello_20,StudentList
from newapp.views import StudentListCreate,StudentListUpdate,StudentListDelete
from newapp.views import view_sy,view_fy,view_ty,view_index
# from student.views import view_django


#from django.conf.urls import url

from django.urls import re_path as url


#   https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html    REPORTS GEN

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/', view_index, name='link_index'),
    url(r'^sy/', view_sy, name='link_sy'),
    url(r'^ty/', view_ty, name='link_ty'),
    url(r'^fy/', view_fy, name='link_fy'),
    url(r'^HI/', view_hello, name='link_hello'),
    url(r'^hello1/', view_hello),
    url(r'^hello20/', view_hello_20),
    url(r'^record1/', view_record, name='link_record'),
    path('', StudentList.as_view(), name='student1_list'),

    path('new', StudentListCreate.as_view(), name='Student_new'),
	path('edit/<int:pk>', StudentListUpdate.as_view(), name='Student_edit'),
  	path('delete/<int:pk>', StudentListDelete.as_view(), name='Student_delete'),


    # url(r'^django/', view_django),




]

from django.urls import re_path as url

