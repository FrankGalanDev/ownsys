from django.forms import ModelForm
from django.forms import TimeInput, TimeField, TextInput, Select
import datetime
from backoffice.models import Brand
from backoffice.models import Company
from backoffice.models import CategDoc
from backoffice.models import CategItem
from backoffice.models import CategPost
from backoffice.models import CategTask
from backoffice.models import Currency
from backoffice.models import Comment
from backoffice.models import Courier
from backoffice.models import Customer
from backoffice.models import Documt
from backoffice.models import Inventory
from backoffice.models import Item
from backoffice.models import Level
from backoffice.models import Operation
from backoffice.models import Platform
from backoffice.models import Post
from backoffice.models import User
from backoffice.models import UserClas
from backoffice.models import Returned
from backoffice.models import Section
from backoffice.models import Sold
from backoffice.models import SubcategoryItem
from backoffice.models import Task


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        exclude = ['created_by', 'updated_by']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class CategDocForm(ModelForm):
    class Meta:
        model = CategDoc
        fields = '__all__'


class CategItemForm(ModelForm):
    class Meta:
        model = CategItem
        fields = '__all__'


class CategPostForm(ModelForm):
    class Meta:
        model = CategPost
        fields = '__all__'


class CategTaskForm(ModelForm):
    class Meta:
        model = CategTask
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class CourierForm(ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class DocumtForm(ModelForm):
    class Meta:
        model = Documt
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class LevelForm(ModelForm):
    class Meta:
        model = Level
        fields = '__all__'


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserClasForm(ModelForm):
    class Meta:
        model = UserClas
        fields = '__all__'


class ReturnedForm(ModelForm):
    class Meta:
        model = Returned
        fields = '__all__'


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class SoldForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields(): 
        # con una iteracion asigno a los campos del form la clase y el autocomplete
            form.field.widget.attrs['class'] = 'form-control' 
            form.field.widget.attrs['autocomplete'] = 'off'
            #colocando autofocus en  sold_item
        self.fields['invoice_number'].widget.attrs['autofocus'] = True #colocando autofocus en  number

    '''            
           colocando autofocus en  sold_item pero con un dccionario

        self.fields['subtotal'].widget.attrs ={
            'readonly' : True,
            'class' :'form-control',
            'style': 'width : 100%'
            }
    '''        


    class Meta:
        model = Sold
        fields = '__all__'
        widgets = {
            'customer': Select(
                attrs={
                    'class':'form-control',
                    'style':'width:100%',
                    'type':'text'
                     
                }
            ),
            'sold_item': Select(
                attrs={
                    'class':'form-control',
                    'style':'width:100%',
                    'type':'text'
                     
                }
            ),
            'valid_until': TimeInput(
                format='%Y-%m-%d',
                attrs={
                    'class':'form-control datepicker',
                    'style':'width:100%',
                    'type':'text',
                    'value':datetime.datetime
                     
                }
            ),
            'tax': TextInput(
                attrs={
                    'class':'form-control'
                    }),
            'subtotal': TextInput(
                attrs={
                    'class':'form-control',
                    'readonly': True,
                    }),
            'total': TextInput(
                attrs={
                    'class':'form-control',
                    'readonly': True,
                    }),
            'courier_name': Select(
                attrs={
                    'class':'form-control',
                    'style':'width:100%',
                    'type':'text'
                     
                }
            ),
        }


class InvoiceForm(ModelForm):

    class Meta:
        model = Sold
        fields = '__all__'


class SubcategoryItemForm(ModelForm):
    class Meta:
        model = SubcategoryItem
        fields = '__all__'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
