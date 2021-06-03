"""localsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:    path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(),name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import backoffice.views.home
import frontoffice.views
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import render
from backoffice.views.access import LoginFormView
from backoffice.views.brand import BrandCreate, BrandList, BrandUpdate, BrandDelete
from backoffice.views.categdoc import CategDocCreate, CategDocList, CategDocUpdate, CategDocDelete
from backoffice.views.categdoc import CategDocCreate, CategDocList, CategDocUpdate, CategDocDelete
from backoffice.views.subcategoryitem import SubcategoryItemCreate, SubcategoryItemList, SubcategoryItemUpdate, SubcategoryItemDelete
from backoffice.views.categitem import CategItemCreate, CategItemList, CategItemUpdate, CategItemDelete
from backoffice.views.categpost import CategPostCreate, CategPostList, CategPostUpdate, CategPostDelete
from backoffice.views.categtask import CategTaskCreate, CategTaskList, CategTaskUpdate, CategTaskDelete
from backoffice.views.comment import CommentCreate, CommentList, CommentUpdate, CommentDelete
from backoffice.views.courier import CourierCreate, CourierList, CourierUpdate, CourierDelete
from backoffice.views.currency import CurrencyCreate, CurrencyList, CurrencyUpdate, CurrencyDelete
from backoffice.views.customer import CustomerCreate, CustomerList, CustomerUpdate, CustomerDelete
from backoffice.views.documt import DocumtCreate, DocumtList, DocumtUpdate, DocumtDelete
from backoffice.views.inventory import InventoryCreate, InventoryList, InventoryUpdate, InventoryDelete
from backoffice.views.item import ItemCreate, ItemList, ItemUpdate, ItemDelete
from backoffice.views.level import LevelCreate, LevelList, LevelUpdate, LevelDelete
from backoffice.views.operation import OperationCreate, OperationList, OperationUpdate, OperationDelete
from backoffice.views.platform import PlatformCreate, PlatformList, PlatformUpdate, PlatformDelete
from backoffice.views.post import PostCreate, PostList, PostUpdate, PostDelete
from backoffice.views.user import UserList
from backoffice.views.returned import ReturnedCreate, ReturnedList, ReturnedUpdate, ReturnedDelete
from backoffice.views.section import SectionCreate, SectionList, SectionUpdate, SectionDelete
from backoffice.views.sold import SoldCreate, SoldList, SoldUpdate, SoldDelete
from backoffice.views.task import TaskCreate, TaskList, TaskUpdate, TaskDelete



 
urlpatterns = [

    path('admin/', admin.site.urls),

    path('dashboard/', include('backoffice.urls'), name="login"),

    # all frontoffice area
    path('', frontoffice.views.home, name="home"),
    path('about/', frontoffice.views.about, name="about"),
    path('contact/', frontoffice.views.contact, name="contact"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
