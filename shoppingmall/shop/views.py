from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count, F #WHERE, OR 조건 등 복잡한 SQL 쿼리문을 사용하기 위해 Q 객체를 import

from .models import Product
from accounts.models import Buyer, Seller

def home(request):
    products = Product.objects
    sort = request.GET.get('sort','')
    #정렬
    if sort == "new":
        products = products.order_by('-pub_date')
    elif sort == "expen":
        products = products.order_by('-price')
    elif sort == "cheap":
        products = products.order_by('price')
    elif sort == "popular":
        products = products.order_by('-stocksold')
    return render(request, 'home.html', {'products': products})

#세부정보
def detail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product':product_detail})

#카테고리/브랜드 필터링
def filter(request, f, select):
    sort = request.GET.get('sort','')
    if f=="category":
        products = Product.objects.filter(category=select)
        #정렬
        if sort == "new":
            products = products.order_by('-pub_date')
        elif sort == "expen":
            products = products.order_by('-price')
        elif sort == "cheap":
            products = products.order_by('price')
        elif sort == "popular":
            products = products.order_by('-stocksold')
    elif f == "brand":
        products = Product.objects.filter(brand=select)
        if sort == "new":
            products = products.order_by('-pub_date')
        elif sort == "expen":
            products = products.order_by('-price')
        elif sort == "cheap":
            products = products.order_by('price')
        elif sort == "popular":
            products = products.order_by('-stocksold')
    else:
        if select == "10000":
            products = Product.objects.filter(price__lt = 10000) #field__lt(less than)
            if sort == "new":
                products = products.order_by('-pub_date')
            elif sort == "expen":
                products = products.order_by('-price')
            elif sort == "cheap":
                products = products.order_by('price')
            elif sort == "popular":
                products = products.order_by('-stocksold')
        elif select =="50000":
            products = Product.objects.filter(price__gte = 10000, price__lt = 50000) #gte(greater than or equal)
            if sort == "new":
                products = products.order_by('-pub_date')
            elif sort == "expen":
                products = products.order_by('-price')
            elif sort == "cheap":
                products = products.order_by('price')
            elif sort == "popular":
                products = products.order_by('-stocksold')
        elif select =="100000":
            products = Product.objects.filter(price__gte = 50000, price__lt = 100000)
            if sort == "new":
                products = products.order_by('-pub_date')
            elif sort == "expen":
                products = products.order_by('-price')
            elif sort == "cheap":
                products = products.order_by('price')
            elif sort == "popular":
                products = products.order_by('-stocksold')
        else:
            products = Product.objects.filter(price__gte = 100000)
            if sort == "new":
                products = products.order_by('-pub_date')
            elif sort == "expen":
                products = products.order_by('-price')
            elif sort == "cheap":
                products = products.order_by('price')
            elif sort == "popular":
                products = products.order_by('-stocksold')
    return render(request, 'home.html', {'products':products})

def searchitem(request):
    try:
        word = request.GET.get('searching')
    except:
        word = None
    #field__icontains: 대소문자 구분하지 않고 해당 문자열 포함한 경우 return 
    if word is not None and len(word) != 0:
        products = Product.objects.filter(Q(pname__icontains = word) | Q(brand__icontains = word)) 
    return render(request, 'search.html', {'word':word, 'products':products})

def buy(request):
    products = Product.objects.filter(stock__gt = 0)
    if request.method == "POST":
        products = Product.objects
        buyitems = request.POST.getlist('buyitems')      
        buyer = Buyer.objects.get(user=request.user)
        
        index = 0
        for x in buyitems:
            buyer.pids.add(Product.objects.get(pid=buyitems[index]))
            
            items = Product.objects.get(pid=buyitems[index])
            items.stock -= 1
            items.stocksold += 1
            items.save()
            index +=1

        messages.add_message(request, messages.SUCCESS, '구매가 완료되었습니다')
        return render(request, 'home.html', {'products': products})
    return render(request, 'buy.html', {'products':products})


def mypage(request):
    buyer = Buyer.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'buyer':buyer})    