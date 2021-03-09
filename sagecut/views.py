from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm, NewUser
from .models import customer
#login imp's
from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'sagecut/index.html')

def book(request):
    book_form = NewUser()
    if request.method == 'POST':
      book_form = NewUser(request.POST)
      if book_form.is_valid():
            book_form.save(commit=True)
            return home(request)
      else:
            print('Error form invalid')

    return render(request,'sagecut/book.html',{'book_form':book_form})





@login_required
def special(request):
    return HttpResponse('Logged IN ')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def reservations(request):
    customer_list = customer.objects.order_by('first_name')
    date_dict = {'access_records':customer_list}
    return render(request,'sagecut/reservations.html',context = date_dict)


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user


        else:
                print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form= UserProfileInfoForm()

    return render(request,'sagecut/register.html',{
                            'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered,})






def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Your Account Has Been Deactivated")
        else:
            print("Login Failed")
        return HttpResponse("invalid login")
    else:
        return render(request,'sagecut/login.html',{})
