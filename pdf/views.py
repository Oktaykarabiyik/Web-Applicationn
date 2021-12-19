from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pdf/list.html')
def detail(request):
    return render(request,'pdf/detail.html')
def search(request):
    return render(request,'pdf/search.html')