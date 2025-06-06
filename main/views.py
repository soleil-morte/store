from django.shortcuts import render,redirect
from .models import *
from django.views.generic import DetailView

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
    return render(request, 'index.html', context)


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