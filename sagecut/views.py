from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'sagecut/index.html')

def book(request):
    return render(request,'sagecut/book.html')
