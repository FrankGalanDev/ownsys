
from django.db import models
from localsys.models import BaseModel
from django.urls import reverse
from django.contrib.auth.models import  AbstractUser, BaseUserManager
from django.utils.text import slugify
from django.templatetags.static import static
from crum import get_current_request
from crum import get_current_user
from django.conf import settings
from localsys.settings import MEDIA_URL, STATIC_URL
from django.forms import model_to_dict



"""SECTION AREA"""


class Company(models.Model):
    # Sections will be the differents area's enterprise are divided
    company_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    web = models.URLField(max_length=100, blank=True,null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    lema = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=600, blank=True, null=True)
    sales_conditions = models.TextField(blank=True, null=True)
    customer_notice = models.TextField(blank=True, null=True)
    protection_policies = models.TextField(blank=True, null=True)
    text_1 = models.TextField(blank=True, null=True)
    text_2 = models.TextField(blank=True, null=True)
    text_3 = models.TextField(blank=True, null=True)
    text_4 = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='backoffice/static/logos',
        blank=True,
        null=True
    ) 


    class Meta:
        ordering = ('company_name',)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('company_data.html', kwargs={'pk':self.id})

     

"""SECTION AREA"""


class Section(models.Model):
    # Sections will be the differents area's enterprise are divided
    section_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    web = models.URLField(max_length=100, blank=True,null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    section_description = models.TextField(blank=True, null=True)


    class Meta:
        ordering = ('section_name',)

    def __str__(self):
        return self.section_name
    
    def toJSON(self):
        sect = model_to_dict(self)
        return sect

    def get_absolute_url(self):
        return reverse('all_sections.html', kwargs={'pk':self.id})

     

"""-------USER AREA-------""" 

class UserClas(models.Model):
    # 
    clas_name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=3000, blank=True)

    class Meta:
        ordering = ('clas_name',)

    def __str__(self):
        return self.clas_name
    
    def get_absolute_url(self):
        return reverse('all_userclas.html', kwargs={'pk':self.id})


class User(AbstractUser):
    """ Model User extending funcionalities from our user model"""
    clas_name = models.ForeignKey(UserClas, on_delete = models.CASCADE,
        null=True, blank=True)
    section = models.ForeignKey(Section, on_delete = models.CASCADE,
        null=True, blank=True)
    photouser = models.ImageField(
        upload_to='backoffice/static/avatars',
        default='backoffice/static/avatars/avatar.jpg',
        blank=True,
        null=True
    )
    position = models.CharField(max_length=100)
    notices = models.TextField(blank=True)

    def __str__(self):
        """Returning  username."""
        return self.username
    
    def get_absolute_url(self):
        return reverse('all_users.html', kwargs={'pk':self.id})




"""-------PRODUCTS OR ITEM'S AREA-------"""



class Brand(BaseModel):
    # Brand 
    brand_name = models.CharField(max_length=100, unique=True)
    brand_logo = models.ImageField(
        upload_to='backoffice/static/logos',
        blank=True,
        null=True
        ) 

    class Meta:
        ordering = ('brand_name',)

    def __str__(self):
        return self.brand_name
    
    def get_absolute_url(self):
        return reverse('all_brands.html', kwargs={'pk':self.id})
    
    def toJSON(self):
        bra = model_to_dict(self, exclude=['brand_logo'])
        return bra
    
    #creating an history sequence of changes
    def save(self, force_insert=False,force_update=False, using=None,
        update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.created_by = user
            else:
                self.modified_by = user
        super(Brand, self).save()



class CategItem(models.Model):
    # CategProd will be the product's categories to use
    categprod_name = models.CharField(max_length=100, unique=True)
    categprod_description = models.CharField(max_length=3000, blank=True)

    class Meta:
        ordering = ('categprod_name',)

    def __str__(self):
        return self.categprod_name
    
    def toJSON(self):
        cat = model_to_dict(self)
        return cat

    def get_absolute_url(self):
        return reverse('all_categitems.html', kwargs={'pk':self.id})



class SubcategoryItem(models.Model):
    """Operation model, show the differents actions could done whit item."""
    categ = models.ForeignKey(CategItem, on_delete=models.CASCADE)
    subcategoryitem_name = models.CharField(max_length=255)

    def __str__(self):
        return self.subcategoryitem_name
    
    def toJSON(self):
        subcat = model_to_dict(self)
        return subcat

    def get_absolute_url(self):
        return reverse('all_subcategoryitem.html', kwargs={'pk':self.id})




class Operation(models.Model):
    """Operation model, show the differents actions could done whit item."""
    operation_name = models.CharField(max_length=255)

    def __str__(self):
        return self.operation_name
    
    def toJSON(self):
        oper = model_to_dict(self)
        return oper

    def get_absolute_url(self):
        return reverse('all_operations.html', kwargs={'pk':self.id})


"""------- CURRENCY AREA-------"""

class Currency(models.Model):
    #currency
    currency_name = models.CharField(max_length=100, blank=True)
    symbol = models.CharField(max_length=1, blank=True, null=True)
    current_value = models.DecimalField(max_digits=7, decimal_places=5, 
        blank=True, null=False)
     

    class Meta:
        ordering = ('currency_name',)

    def __str__(self):
        return self.currency_name

    def get_absolute_url(self):
        return reverse('all_currencies.html', kwargs={'pk':self.id})



class Item(models.Model):
    """Items Product model"""
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubcategoryItem, on_delete=models.CASCADE)
    categ = models.ForeignKey(CategItem, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, verbose_name='item')
    item_description = models.TextField(null=True)
    item_SKU = models.CharField(max_length=100, null=False, blank=True)
    ean = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField()
    price = models.PositiveIntegerField(null=True)
    purchase_price = models.PositiveIntegerField(null=True, blank=True)
    tax = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=30, null=True)
    size = models.CharField(max_length=3, null=True, blank=True)
    weight = models.CharField(max_length=5, null=True, blank=True)
    height = models.CharField(max_length=5, null=True, blank=True)

    image = models.ImageField(
        upload_to='backoffice/static/images',
        blank=True,
        null=True
    )
    image_1 = models.ImageField(
        upload_to='backoffice/static/images',
        blank=True,
        null=True
    )
    image_2 = models.ImageField(
        upload_to='backoffice/static/images',
        blank=True,
        null=True
    )
    image_3 = models.ImageField(
        upload_to='backoffice/static/images',
        blank=True,
        null=True
    )
    image_4 = models.ImageField(
        upload_to='backoffice/static/images',
        blank=True,
        null=True
    )
    image_5 = models.ImageField(
        upload_to='backoffice/static/images',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('item_name',)

    def __str__(self):
        return self.item_name

    def toJSON(self):
        #product = model_to_dict(self)
        
        product = model_to_dict(self, exclude=['image','image_1','image_2','image_3','image_4','image_5'])
        '''
        product['image'] = self.get_image()
        product['image_1'] = self.get_image()
        product['image_2'] = self.get_image()
        product['image_3'] = self.get_image()
        product['image_4'] = self.get_image()
        product['image_5'] = self.get_image()
        '''
        product['operation'] = self.operation.toJSON()
        product['brand'] = self.brand.toJSON()
        product['subcategory'] = self.subcategory.toJSON()
        product['categ'] = self.categ.toJSON()
        product['section'] = self.section.toJSON()
        product['price'] = format(self.price, '.2f')
        product['purchase_price'] = format(self.purchase_price, '.2f')
        product['tax'] = format(self.tax, '.2f')
        return product
    
    def get_absolute_url(self):
        return reverse('all_items.html', kwargs={'pk':self.id})



"""------- COURIER AREA-------"""

class Courier(models.Model):
    #courier
    courier_name = models.CharField(max_length=100, blank=True)
    logo =  models.ImageField(
        upload_to= 'backoffice/static/logos',
        blank=True,
        null=True
    )
    description = models.TextField(null=True, blank=True)
    delivery_terms = models.TextField(blank=True)

    class Meta:
        ordering = ('courier_name',)

    def __str__(self):
        return self.courier_name

    def get_absolute_url(self):
        return reverse('all_couriers.html', kwargs={'pk':self.id})



"""-------CUSTOMER AREA-------"""

class Level(models.Model):
    """"Categorys will be the document's categories to use"""
    level_name = models.CharField(max_length=255, blank=True)
    level_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.level_name

    def get_absolute_url(self):
        return reverse('all_levels.html', kwargs={'pk':self.id})



class Customer(models.Model):
    #customer
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100, blank=True)
    customer_lastname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, unique=True)
    phone = models.CharField(max_length=15, blank=True, unique=True )
    identification_number = models.CharField(max_length=100, blank=True, null=True)
    accept_promo = models.BooleanField()
    accept_survey = models.BooleanField()
    accept_notifications = models.BooleanField()
    note = models.TextField(blank=True, null=True)
    

    class Meta:
        ordering = ('customer_name',)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('all_customers.html', kwargs={'pk':self.id})


class Sold(models.Model):
    """"items sold"""
    sold_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1 )
    tax = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total= models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    courier_name = models.ForeignKey(Courier, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_until = models.TimeField()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.all()
    
    def get_absolute_url(self):
        return reverse('all_solds.html', kwargs={'pk':self.id})



class Returned(models.Model):
    """"items sold"""
    returned_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rma_code = models.CharField(max_length=100, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.sold_item
    
    def get_absolute_url(self):
        return reverse('all_returned.html', kwargs={'pk':self.id})


class Inventory(models.Model):
    """"items sold"""
    total_item_sold = models.PositiveIntegerField()
    total_item_stored = models.PositiveIntegerField()
    value_item_sold = models.PositiveIntegerField()
    value_item_stored =models.PositiveIntegerField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.total_item_sold
    
    def get_absolute_url(self):
        return reverse('all_inventories.html', kwargs={'pk':self.id})



"""-------INTERNAL CHAT AREA-------"""

class CategPost(models.Model):
    """"CategPost will be the post or message to use"""
    categpost_name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('categpost_name',)

    def __str__(self):
        return self.categpost_name
    
    def get_absolute_url(self):
        return reverse('all_categposts.html', kwargs={'pk':self.id})


class Post(models.Model):
    """"Post is the message  """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    categpost = models.ForeignKey(CategPost, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, blank=True)
    image_header = models.ImageField(
        upload_to='backoffice/static/images',
        blank=True,
        null=True
    )
    posttext = models.TextField(null=False, verbose_name='post_text')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        """Returning title and username."""
        return '{} by @{}'.format(self.title, self.user.username)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    """"Categorys will be the product's categories tu use"""
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    topic = models.CharField(
        max_length=100, verbose_name='topic', blank=True)
    commentext = models.TextField(verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('created_at',)

    def get_absolute_url(self):
        return reverse('all_comments.html', kwargs={'pk':self.id})


"""-------TASKS AREA-------"""

class CategTask(models.Model):
    """"Categorys will be the product's categories tu use"""
    category_task_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.category_task_name


class Task(models.Model):
    """Task model."""
    executer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='executer',)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='owner',)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    task_type = models.ForeignKey(CategTask, on_delete=models.CASCADE,)
    task_name = models.CharField(max_length=255, blank=False)
    task_description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    is_done = models.BooleanField()

    class Meta:
        ordering = ('updated_at',)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('all_tasks.html', kwargs={'pk':self.id})


"""-------DOCUMENT AREA-------"""
class CategDoc(models.Model):
    """"Categorys will be the document's categories to use"""
    categdoc_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.categdoc_name

    def get_absolute_url(self):
        return reverse('all_categdocs.html', kwargs={'pk':self.id})



class Documt(models.Model):
    """"Documents model's"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    categ_doc = models.ForeignKey(CategDoc, on_delete=models.PROTECT)
    document_name = models.CharField(max_length=255, verbose_name='document')
    document_description = models.TextField(blank=True)
    document_code = models.CharField(max_length=1000, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField(
        upload_to='backoffice/static/documents',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.document_name
    
    def get_absolute_url(self):
        return reverse('all_documts.html', kwargs={'pk':self.id})


"""-------PLATFORM TO CONNECT AREA-------"""

class Platform(models.Model):
    """"Platform's model, to third part connexions """
    platform_name = models.CharField(max_length=100, verbose_name='plataform')
    user_platf = models.CharField(max_length=100, verbose_name='nick_access')
    access_key = models.CharField(
        max_length=255, verbose_name='access_password')
    api_details = models.TextField(blank=True)
    api_description = models.TextField(blank=True)

    def __str__(self):
        return self.platform_name
    
    def get_absolute_url(self):
        return reverse('all_platforms.html', kwargs={'pk':self.id})


"""-------CHAT AREA-------"""

class Chat(models.Model):
    """"Chatting area model """
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('all_chat.html', kwargs={'pk':self.id})