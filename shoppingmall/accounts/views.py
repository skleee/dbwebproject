from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpResponse
from .models import Buyer, Seller
from django.contrib.auth.decorators import login_required

#SIGNUP for BUYER
def buyersignup(request):
    if request.method =="POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1']
                    )
                buyer = Buyer(user = user)
                buyer.address = request.POST['address']
                buyer.is_buyer = True
                buyer.save()    
                messages.add_message(request, messages.SUCCESS, '구매자 가입을 환영합니다')
                return redirect('home')
            except Exception as e:
                print(e)
                messages.add_message(request, messages.ERROR, '이미 존재하는 아이디입니다')
                return redirect('buyersignup')
                # user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        messages.add_message(request, messages.ERROR, '비밀번호가 일치하지 않습니다')
    return render(request, 'buyersignup.html')

#SIGNUP for SELLER
def sellersignup(request):
    if request.method =="POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1']
                    )
                seller = Seller(user = user)
                seller.is_seller = True
                seller.save()
                messages.add_message(request, messages.SUCCESS, '판매자 가입을 환영합니다')
                return redirect('home')
            except Exception as e:
                print(e)
                messages.add_message(request, messages.ERROR, '이미 존재하는 아이디입니다')
                return redirect('sellersignup')
        messages.add_message(request, messages.ERROR, '비밀번호가 일치하지 않습니다')
    return render(request, 'sellersignup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, '로그인을 환영합니다')
        else:
            messages.add_message(request, messages.ERROR, '로그인에 실패했씁니다')
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, '로그아웃되었습니다')
        return redirect('home')
    return render(request, 'home.html')