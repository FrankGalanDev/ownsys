from django.contrib import admin

# Register your models here.
from django.contrib import admin
from backoffice.models import( Brand, Company, CategDoc, CategItem,
	CategPost, CategTask, Comment, Courier, Currency, Customer, Documt,
	Inventory, Item, Level, Operation, Platform, Post, User,UserClas, Returned,
	Section, Sold, Task,
	)
# Register your models here.

from .models import Brand
from .models import Company
from .models import CategDoc
from .models import CategItem
from .models import CategPost
from .models import CategTask
from .models import Comment
from .models import Courier
from .models import Currency
from .models import Customer
from .models import Documt
from .models import Inventory
from .models import Item
from .models import Level
from .models import Operation
from .models import Platform
from .models import Post
from .models import User
from .models import UserClas
from .models import Returned
from .models import Section
from .models import Sold
from .models import SubcategoryItem
from .models import Task




admin.site.register(Brand),
admin.site.register(Company)
admin.site.register(CategDoc),
admin.site.register(CategItem),
admin.site.register(CategPost),
admin.site.register(CategTask),
admin.site.register(Comment),
admin.site.register(Courier),
admin.site.register(Currency),
admin.site.register(Customer),
admin.site.register(Documt),
admin.site.register(Inventory),
admin.site.register(Item),
admin.site.register(Level),
admin.site.register(Operation),
admin.site.register(Platform),
admin.site.register(Post),
admin.site.register(User),
admin.site.register(UserClas),
admin.site.register(Returned),
admin.site.register(Section),
admin.site.register(Sold),
admin.site.register(Task),
admin.site.register(SubcategoryItem),



""" customizando el panel de control"""
admin.site.site_header = 'LocalSys'
admin.site.site_title = 'Another way to help'
admin.site.index_title= 'Personal Dashboard'