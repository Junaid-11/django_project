from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.contrib.auth import authenticate, login
import random
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ProfileView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSer


class ProductView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSer

#OTP Validation
def register(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')

        check_profile = Profile.objects.filter(mobile=mobile).first()

        if check_profile:
            return Response({'Message': 'User Already Exists'})

        user = User(username=username)
        user.set_password(user.password)
        user.save()
        otp = str(random.randint(1000, 9999))
        profile = Profile(mobile=mobile, otp=otp)
        profile.save()
        request.session['mobile'] = mobile
        context={"Message":"OTP has been send to the given Mobile Number"}
        return render(request,context)
    return Response({'Message':'None'})


def otp(request):
    mobile = request.session['mobile']
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()

        if otp == profile.otp:
            return Response({'Message':'Success'})
        else:
            return Response({'message': 'Wrong OTP','mobile': mobile})
    return Response({"Message":"None"})


def login_attempt(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')

        user = Profile.objects.filter(mobile=mobile).first()

        if user is None:
            return Response({'message': 'User not found'})

        otp = str(random.randint(1000, 9999))
        user.otp = otp
        user.save()
        request.session['mobile'] = mobile
        return redirect('login_otp')
    return render(request)


def login_otp(request):
    mobile = request.session['mobile']
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()

        if otp == profile.otp:
            user = User.objects.get(id=profile.user.id)
            login(request, user)
            context={"Message":"Login Successfull"}
            return render(context)
        else:
            context={'message': 'Wrong OTP'}
            return render(context)

    return render(request, context)


