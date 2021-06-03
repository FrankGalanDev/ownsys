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
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
#from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import render
#access views
from backoffice.views.access import LoginFormView, LogoutView
#backoffice views
from backoffice.views.brand import BrandCreate, BrandList, BrandUpdate, BrandDelete
from backoffice.views.categdoc import CategDocCreate, CategDocList, CategDocUpdate, CategDocDelete
from backoffice.views.categdoc import CategDocCreate, CategDocList, CategDocUpdate, CategDocDelete
from backoffice.views.subcategoryitem import SubcategoryItemCreate, SubcategoryItemList, SubcategoryItemUpdate, SubcategoryItemDelete
from backoffice.views.categitem import CategItemCreate, CategItemList, CategItemUpdate, CategItemDelete
from backoffice.views.categpost import CategPostCreate, CategPostList, CategPostUpdate, CategPostDelete
from backoffice.views.categtask import CategTaskCreate, CategTaskList, CategTaskUpdate, CategTaskDelete
from backoffice.views.comment import CommentCreate, CommentList, CommentUpdate, CommentDelete
from backoffice.views.company import CompanyList, CompanyCreate, CompanyUpdate
from backoffice.views.courier import CourierCreate, CourierList, CourierUpdate, CourierDelete
from backoffice.views.currency import CurrencyCreate, CurrencyList, CurrencyUpdate, CurrencyDelete
from backoffice.views.customer import CustomerCreate, CustomerList, CustomerUpdate, CustomerDelete
from backoffice.views.documt import DocumtCreate, DocumtList, DocumtUpdate, DocumtDelete
from backoffice.views.inventory import InventoryCreate, InventoryList, InventoryUpdate, InventoryDelete
from backoffice.views.item import ItemCreate, ItemList, ItemByList,ItemUpdate, ItemDelete
from backoffice.views.level import LevelCreate, LevelList, LevelUpdate, LevelDelete
from backoffice.views.operation import OperationCreate, OperationList, OperationUpdate, OperationDelete
from backoffice.views.platform import PlatformCreate, PlatformList, PlatformUpdate, PlatformDelete
from backoffice.views.post import PostCreate, PostList, PostUpdate, PostDelete
from backoffice.views.user import UserList,UserByList, UserCreate, UserUpdate, UserDelete
from backoffice.views.userclas import UserClasList, UserClasCreate, UserClasUpdate, UserClasDelete
from backoffice.views.returned import ReturnedCreate, ReturnedList, ReturnedUpdate, ReturnedDelete
from backoffice.views.section import SectionCreate, SectionList, SectionUpdate, SectionDelete
from backoffice.views.sold import SoldCreate, SoldList, SoldUpdate, SoldDelete, InvoiceCreate,sold_generator #, invoice
from backoffice.views.subcategoryitem import SubcategoryItemCreate, SubcategoryItemList, SubcategoryItemUpdate, SubcategoryItemDelete
from backoffice.views.task import TaskCreate, TaskList, TaskUpdate, TaskDelete
from backoffice.views.mail import MailView
from backoffice.views.chat import ChatView, ChatMessagesView


urlpatterns = [

    path('login/', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),
    #path('register/', frontoffice.views.register, name='register'),
    path('mail/', MailView.as_view(), name='mail'),


    path('backoffice/', backoffice.views.home.management, name="backoffice"),
    

    #Company Urls
    path('backoffice/see_company',
         CompanyList.as_view(), name="company_data"),
    path('backoffice/create_company',
         CompanyCreate.as_view(), name="create_company"),
    path('backoffice/update_company/<int:pk>/',
         CompanyUpdate.as_view(), name="update_company"),

    #path('backoffice/delete_brand/<int:pk>/',
    #    BrandDelete.as_view(), name="delete_brand"),



    #Brands Urls
    path('backoffice/all_brands',
         BrandList.as_view(), name="all_brand"),
    path('backoffice/new_brand',
         BrandCreate.as_view(), name="new_brand"),
    path('backoffice/update_brand/<int:pk>/',
         BrandUpdate.as_view(), name="update_brand"),
    path('backoffice/delete_brand/<int:pk>/',
         BrandDelete.as_view(), name="delete_brand"),


    #CategDoc Urls
    path('backoffice/all_categdocs',
         CategDocList.as_view(), name="all_categdoc"),
    path('backoffice/new_categdoc',
         CategDocCreate.as_view(), name="new_categdoc"),
    path('backoffice/update_categdoc/<int:pk>/',
         CategDocUpdate.as_view(), name="update_categdoc"),
    path('backoffice/delete_categdoc/<int:pk>/',
         CategDocDelete.as_view(), name="delete_categdoc"),


    #CategItem Urls
    path('backoffice/all_categitems',
         CategItemList.as_view(), name="all_categitem"),
    path('backoffice/new_categitem',
         CategItemCreate.as_view(), name="new_categitem"),
    path('backoffice/update_categitem/<int:pk>/',
         CategItemUpdate.as_view(), name="update_categitem"),
    path('backoffice/delete_categitem/<int:pk>/',
         CategItemDelete.as_view(), name="delete_categitem"),


    #SubCategoryItem Urls
    path('backoffice/all_subcategoryitems',
         SubcategoryItemList.as_view(), name="all_subcategoryitem"),
    path('backoffice/new_subcategoryitem',
         SubcategoryItemCreate.as_view(), name="new_subcategoryitem"),
    path('backoffice/update_subcategoryitem/<int:pk>/',
         SubcategoryItemUpdate.as_view(), name="update_subcategoryitem"),
    path('backoffice/delete_subcategoryitem/<int:pk>/',
         SubcategoryItemDelete.as_view(), name="delete_subcategoryitem"),


    #CategPost Urls
    path('backoffice/all_categposts',
         CategPostList.as_view(), name="all_categpost"),
    path('backoffice/new_categpost',
         CategPostCreate.as_view(), name="new_categpost"),
    path('backoffice/update_categpost/<int:pk>/',
         CategPostUpdate.as_view(), name="update_categpost"),
    path('backoffice/delete_categpost/<int:pk>/',
         CategPostDelete.as_view(), name="delete_categpost"),
 

    #Chat Urls
    path('backoffice/chat',ChatView.as_view(),name='all_chat'),
    path('backoffice/chat_messages',ChatMessagesView.as_view(),name='chat_message'),
    

    #Post Urls
    path('backoffice/all_posts',
         PostList.as_view(), name="all_post"),
    path('backoffice/new_post',
         PostCreate.as_view(), name="new_post"),
    path('backoffice/update_post/<int:pk>/',
         PostUpdate.as_view(), name="update_post"),
    path('backoffice/delete_post/<int:pk>/',
         PostDelete.as_view(), name="delete_post"),
   
    #Comment Urls
    path('backoffice/all_comments',
         CommentList.as_view(), name="all_comment"),
    path('backoffice/new_comment',
         CommentCreate.as_view(), name="new_comment"),
    path('backoffice/update_comment/<int:pk>/',
         CommentUpdate.as_view(), name="update_comment"),
    path('backoffice/delete_comment/<int:pk>/',
         CommentDelete.as_view(), name="delete_comment"),


   #CategTask Urls
    path('backoffice/all_categtasks',
         CategTaskList.as_view(), name="all_categtask"),
    path('backoffice/new_categtask',
         CategTaskCreate.as_view(), name="new_categtask"),
    path('backoffice/update_categtask/<int:pk>/',
         CategTaskUpdate.as_view(), name="update_categtask"),
    path('backoffice/delete_categtask/<int:pk>/',
         CategTaskDelete.as_view(), name="delete_categtask"),

    #Courier Urls
    path('backoffice/all_couriers',
         CourierList.as_view(), name="all_courier"),
    path('backoffice/new_courier',
         CourierCreate.as_view(), name="new_courier"),
    path('backoffice/update_courier/<int:pk>/',
         CourierUpdate.as_view(), name="update_courier"),
    path('backoffice/delete_courier/<int:pk>/',
         CourierDelete.as_view(), name="delete_courier"),


    #Currency Urls
    path('backoffice/all_currencies',
         CurrencyList.as_view(), name="all_currency"),
    path('backoffice/new_currency',
         CurrencyCreate.as_view(), name="new_currency"),
    path('backoffice/update_currency/<int:pk>/',
         CurrencyUpdate.as_view(), name="update_currency"),
    path('backoffice/delete_currency/<int:pk>/',
         CurrencyDelete.as_view(), name="delete_currency"),


    #Customer Urls
    path('backoffice/all_customers',
         CustomerList.as_view(), name="all_customer"),
    path('backoffice/new_customer',
         CustomerCreate.as_view(), name="new_customer"),
    path('backoffice/update_customer/<int:pk>/',
         CustomerUpdate.as_view(), name="update_customer"),
    path('backoffice/delete_customer/<int:pk>/',
         CustomerDelete.as_view(), name="delete_customer"),
    

    #Documt Urls
    path('backoffice/all_documts',
         DocumtList.as_view(), name="all_documt"),
    path('backoffice/new_documt',
         DocumtCreate.as_view(), name="new_documt"),
    path('backoffice/update_documt/<int:pk>/',
         DocumtUpdate.as_view(), name="update_documt"),
    path('backoffice/delete_documt/<int:pk>/',
         DocumtDelete.as_view(), name="delete_documt"),
    

    #Inventory Urls
    path('backoffice/all_inventories',
         InventoryList.as_view(), name="all_inventory"),
    path('backoffice/new_inventory',
         InventoryCreate.as_view(), name="new_inventory"),
    path('backoffice/update_inventory/<int:pk>/',
         InventoryUpdate.as_view(), name="update_inventory"),
    path('backoffice/delete_inventory/<int:pk>/',
         InventoryDelete.as_view(), name="delete_inventory"),
    

    #Item Urls
    path('backoffice/all_items',
         ItemList.as_view(), name="all_item"),
    path('backoffice/all_items_by_list',
         ItemByList.as_view(), name="all_item_by_list"),
    path('backoffice/new_item',
         ItemCreate.as_view(), name="new_item"),
    path('backoffice/update_item/<int:pk>/',
         ItemUpdate.as_view(), name="update_item"),
    path('backoffice/delete_item/<int:pk>/',
         ItemDelete.as_view(), name="delete_item"),

    #Level Urls
    path('backoffice/all_levels',
         LevelList.as_view(), name="all_level"),
    path('backoffice/new_level',
         LevelCreate.as_view(), name="new_level"),
    path('backoffice/update_level/<int:pk>/',
         LevelUpdate.as_view(), name="update_level"),
    path('backoffice/delete_level/<int:pk>/',
         LevelDelete.as_view(), name="delete_level"),


    #Operation Urls
    path('backoffice/all_operations',
         OperationList.as_view(), name="all_operation"),
    path('backoffice/new_operation',
         OperationCreate.as_view(), name="new_operation"),
    path('backoffice/update_operation/<int:pk>/',
         OperationUpdate.as_view(), name="update_operation"),
    path('backoffice/delete_operation/<int:pk>/',
         OperationDelete.as_view(), name="delete_operation"),


    #Platform Urls
    path('backoffice/all_platforms',
         PlatformList.as_view(), name="all_platform"),
    path('backoffice/new_platform',
         PlatformCreate.as_view(), name="new_platform"),
    path('backoffice/update_platform/<int:pk>/',
         PlatformUpdate.as_view(), name="update_platform"),
    path('backoffice/delete_platform/<int:pk>/',
         PlatformDelete.as_view(), name="delete_platform"),


    #Post Urls
    path('backoffice/all_posts',
         PostList.as_view(), name="all_post"),
    path('backoffice/new_post',
         PostCreate.as_view(), name="new_post"),
    path('backoffice/update_post/<int:pk>/',
         PostUpdate.as_view(), name="update_post"),
    path('backoffice/delete_post/<int:pk>/',
         PostDelete.as_view(), name="delete_post"),


    #User Urls
    path('backoffice/all_users',
         UserList.as_view(), name="all_user"),
    path('backoffice/all_users_by_list',
         UserByList.as_view(), name="all_user_by_list"),
    path('backoffice/new_user',
        UserCreate.as_view(), name="new_user"),
   path('backoffice/update_user/<int:pk>/',
         UserUpdate.as_view(), name="update_user"),
    path('backoffice/delete_user/<int:pk>/',
         UserDelete.as_view(), name="delete_user"),


    #UserClas Urls
    path('backoffice/all_usersclas',
         UserClasList.as_view(), name="all_usersclas"),
    path('backoffice/new_userclas',
        UserClasCreate.as_view(), name="new_userclas"),
   path('backoffice/update_userclas/<int:pk>/',
         UserClasUpdate.as_view(), name="update_userclas"),
    path('backoffice/delete_userclas/<int:pk>/',
         UserClasDelete.as_view(), name="delete_userclas"),


    #Returned Urls
    path('backoffice/all_returneds',
         ReturnedList.as_view(), name="all_returned"),
    path('backoffice/new_returned',
         ReturnedCreate.as_view(), name="new_returned"),
    path('backoffice/update_returned/<int:pk>/',
         ReturnedUpdate.as_view(), name="update_returned"),
    path('backoffice/delete_returned/<int:pk>/',
         ReturnedDelete.as_view(), name="delete_returned"),

    # Section Urls
    path('backoffice/all_sections',
         SectionList.as_view(), name="all_section"),
    path('backoffice/new_section',
         SectionCreate.as_view(), name="new_section"),
    path('backoffice/update_section/<int:pk>/',
         SectionUpdate.as_view(), name="update_section"),
    path('backoffice/delete_section/<int:pk>/',
         SectionDelete.as_view(), name="delete_section"),
    

    #Sold Urls  
    path('backoffice/all_solds',
         SoldList.as_view(), name="all_sold"),
    path('backoffice/new_sold',
         SoldCreate.as_view(), name="new_sold"),
    #path('backoffice/new_invoice',
    #      backoffice.views.sold.invoice, name="new_invoice"),
    path('backoffice/new_invoice/<int:pk>/',
        InvoiceCreate.as_view(), name="new_invoice"),
    path('backoffice/invoice_1/<int:pk>/',
        backoffice.views.sold.sold_generator, name="invoice_1"),
    path('backoffice/update_sold/<int:pk>/',
         SoldUpdate.as_view(), name="update_sold"),
    path('backoffice/delete_sold/<int:pk>/',
         SoldDelete.as_view(), name="delete_sold"),
    

    #Subcategory Urls  
    path('backoffice/all_subcategoryitems',
         SubcategoryItemList.as_view(), name="all_subcategoryitem"),
    path('backoffice/new_subcategoryitem',
         SubcategoryItemCreate.as_view(), name="new_subcategoryitem"),
    path('backoffice/update_subcategoryitem/<int:pk>/',
         SubcategoryItemUpdate.as_view(), name="update_subcategoryitem"),
    path('backoffice/delete_subcategoryitem/<int:pk>/',
         SubcategoryItemDelete.as_view(), name="delete_subcategoryitem"),


    #Task Urls  
    path('backoffice/all_tasks',
         TaskList.as_view(), name="all_task"),
    path('backoffice/new_task',
         TaskCreate.as_view(), name="new_task"),
    path('backoffice/update_task/<int:pk>/',
         TaskUpdate.as_view(), name="update_task"),
    path('backoffice/delete_task/<int:pk>/',
         TaskDelete.as_view(), name="delete_task"),

]
