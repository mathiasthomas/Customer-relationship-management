from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()
    total_customers = customer.count()
    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()

    context = {'order':order,'customer':customer, 'total_customers':total_customers,
    'total_orders':total_orders, 'delivered':delivered, 'delivered':delivered }
    return render (request, 'accounts/dashboard.html',context )

    context = {'orders':orders,'customer':customer,'total_customers':total_customers}

def products(request):
    products = Product.objects.all()
    return render (request, 'accounts/products.html',{'products':products})

def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()

	context = {'customer':customer, 'orders':orders}
	return render (request, 'accounts/customer.html')
    