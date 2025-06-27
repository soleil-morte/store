from django.shortcuts import render,redirect
from .models import *
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
class ProductDetail(DetailView):
    model = Products
    template_name = 'product.html'
    context_object_name = 'product'

class Fullinfo(DetailView):
    model = News
    template_name = 'fullinfo.html'
    context_object_name = 'fullinfo'

def Index(request):
    context = {
        'category':Category.objects.all(),
        'product':Products.objects.all()
    }

    if 'q' in request.GET:
        q = request.GET['q']
        context['product'] = Products.objects.filter(
            Q(name__icontains=q)|
            Q(category__name__icontains=q)
        )
        context['q'] = q 


    return render(request, 'index.html', context)

def Cart(request):
    context = {
        'product':Products.objects.all(),
        'order_item':Order.objects.filter(user=request.user, is_ordered=False).first()
    }
    return render(request, 'cart.html', context)


def Blog(request):
    if request.method == 'POST':
        r = request.POST
        name = r['name']
        image = r['image']
        review = r['review']
        text = r['text']
        News.objects.create(name=name, image=image, text=text, review=review)

        return redirect('/main/blog/')

    context = {
        'news': News.objects.all()
    }
    return render(request, 'blog.html', context)


def Store(request):
    context = {
        'category':Category.objects.all(),
        'product':Products.objects.all().filter(category__id = 1),
        'product_1':Products.objects.all().filter(category__id = 2),
        'product_2':Products.objects.all().filter(category__id = 3),
        'product_3':Products.objects.all().filter(category__id = 4),
    }
    return render(request, 'store.html', context)



def AddProduct(request):

    if request.method == 'POST':
        discount = request.POST['discount']
        # is_new = request.POST['is_new']
        image = request.POST['image']
        category = request.POST['category']
        name = request.POST['name']
        price = request.POST['price']
        new_price = request.POST['new_price']
        text = request.POST['text']
        Products.objects.create(discount=discount,image=image,category_id=category , name=name,price=price,new_price=new_price,text=text)

        return redirect('/main/addproduct/')

    context={
        'category':Category.objects.all()
    }



    return render(request,'addproduct.html',context)



def Sms(request):
    if request.method == 'POST':
        r = request.POST
        first_name=r['first_name']
        last_name = r['last_name']
        job = r['job']
        text = r['text']

        Contact.objects.create(first_name=first_name,last_name=last_name,job=job,text=text)
        return redirect('/main/contact/')

    return render(request,'contact.html')


def Categories(request):
    if request.method == 'POST':
        r = request.POST
        name = r['name']
        image = r['image']

        Category.objects.create(name=name,image=image)
        return redirect('/main/index/')
    
    return render(request,'categories.html')


def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/main/index/')
    else:
        form = UserCreationForm()
    
    context={
        'form':form
    }

    return render(request, 'registration/register.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST['usernamne']
        password = request.POST['password']
        form = authenticate(request, username=username, password=password)
        if form is not None:
            login(request,form)
            return redirect('main/index/')
        return render(request, 'registration/login.html')
    

def Logout(request):
    logout(request)
    return redirect('/main/index/')


@login_required(login_url='/main/auth-login/') 
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)

    order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)

    if not item_created:
        order_item.quantity += 1
        order_item.total_price = float(order_item.quantity)*float(order_item.product.price)
        order_item.save()

    return redirect('/main/index/')


def Delete(request, id):
    delete = OrderItem.objects.get(id=id)

    delete.delete()

    return redirect('/main/cart/')


def Increase(request, id):
    order = OrderItem.objects.get(id=id)
    order.quantity+=1
    # order1=OrderItem.objects.get(client=request.user)
    order.total_price+=order.product.price
    order.save()

    return redirect('/main/cart/')


def Decrease(request, id):
    order = OrderItem.objects.get(id=id)
    if order.quantity>1:
        order.quantity-=1
    # order1=OrderItem.objects.get(client=request.user)
        order.total_price-=order.product.price
        order.save()

    return redirect('/main/cart/')