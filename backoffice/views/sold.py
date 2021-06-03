from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from backoffice.forms import SoldForm, ItemForm
from backoffice.forms import InvoiceForm
from backoffice.models import Sold, Item, Company, Customer
from django.core.paginator import Paginator
from django.http import JsonResponse
import json


# Create your views here.

class SoldList(LoginRequiredMixin, ListView):
    model = Sold
    paginate_by = 10 
    template_name = 'solds/all_solds.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_tittle'] = 'Sold Item List'
        context['table_subtittle'] = 'All solds'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

#Creating an invoice instance
class SoldCreate(LoginRequiredMixin, CreateView):
    model = Sold
    form_class = SoldForm
    template_name = 'solds/add_invoice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Sold Forms'
        context['table_tittle'] = 'New sold'
        context['table_subtittle'] = 'Add here your new solds'
        return context
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    '''    
    @method_decorator(csrf_exempt)
    def post(self, request, *args,**kwargs):
        #sdata={}
        data = dict()
        items=[]
        try:
            #action = request.POST['action']
            action = request.POST.get('action', None)
            if action == 'search_item':
                
                data=[]
                #prods = Item.objects.filter(item_name=request.POST['term'])
                prods = Item.objects.filter(item_name=request.POST.get('term', None)) 
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.item_name
                    data.append(item)

            else:
                data['error']='no ha ingresado una opcion'
                    
                #except Exception as e:
                #   data['error'] = str(e)
            
            data['options'] = items
        return JsonResponse(data, safe=False)  

    '''
    @method_decorator(csrf_exempt)
    def post(self, request, *args,**kwargs):
        data = dict()
        items=[]
        action = request.POST.get('action', None)

        if action:
            if action == 'search_item':
                print(request.POST.get('action', None))

                
                ojo = request.POST.get('term')
                print(ojo)

                prods = Item.objects.filter(item_name__contains=request.POST.get('term')) # Con get, si se tiene el key 'term' se obtiene su valor, si no se tiene entonces se asigna None por defecto a 'term'
                #funciona
                #prods = Item.objects.filter(item_name__contains='I')
                
                print(prods)
                #print(request.POST.get('term', None))
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.item_name
                    items.append(item)
        else:
            data['error']='no ha ingresado una opcion'

        data['options'] = items 

        return JsonResponse(data, safe=False) # al final obtendras {'options': []} o {'error': 'no ha ingresado una opcion', 'options': []}


    
    def get_success_url(self):   
        return reverse('all_sold')


 
def sold_generator(request):
    sold_data = {} 
    sold_data['sold_form'] = SoldForm()
    data['item_form'] = ItemForm()
    return render(request, 'solds/invoice1.html', data)


class InvoiceCreate(LoginRequiredMixin, CreateView):
    model = Sold
    form_class = InvoiceForm
    template_name = 'solds/new_invoice.html'
    success_url = reverse_lazy('all_sold')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'INVOICE'
        context['tittle_to'] = 'TO'
        context['tittle_from'] = 'FROM'
        context['tittle_valid_until'] = 'VALID UNTIL'
        context['tittle_issued'] = 'ISSUED'
        context['tittle_due'] = 'DUE'
        context['tittle_invoice_number'] = 'Invoice Number'
        context['tittle_description'] = 'Description'
        context['tittle_quantity'] = 'Quantity'
        context['tittle_price'] = 'Price'
        context['tittle_tax'] = 'Tax'
        context['tittle_amount'] = 'Amount'
        context['tittle_subtotal'] = 'Subtotal'
        context['tittle_total_sales_tax'] = 'Total Sales tax'
        context['tittle_amount_due'] = 'Amount'
        company = Company.objects.all()
        customers = Customer.objects.all()
        solds = Sold.objects.all()
        items = Item.objects.all()
        return {'company': company, 'solds': solds, 'items': items, 'customers': customers}
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        elements = []
        '''
        for item in self.get_queryset():
            
            
            data_item = {}
            data_item['id'] =item.id
            data_item['name'] =item.id
            data_item['sku'] =item.id
            data_item['ean'] =item.id
            data_item['status'] =item.id
            data_item['is_active'] =item.id
            data_item['price'] =item.id
            data_item['tax'] =item.id
            elements.append(data_item)
        print(elements)
        '''
        return render(request, self.template_name)


    def get_success_url(self):
        return reverse('all_sold')


class SoldUpdate(LoginRequiredMixin, UpdateView):
    model = Sold
    form_class = SoldForm
    template_name = 'solds/all_solds.html'
    success_url = reverse_lazy('all_sold')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Sold Forms'
        context['table_tittle'] = 'Edit sold'
        context['table_subtittle'] = 'Modify here your sold'
        context['action'] = 'edit'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SoldDelete(LoginRequiredMixin, DeleteView):
    model = Sold
    template_name = 'solds/delete_sold.html'
    success_url = reverse_lazy('all_sold')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Sold Forms'
        context['table_tittle'] = 'Delete sold Form'
        context['table_subtittle'] = 'Delete here your sold'
        return context

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
