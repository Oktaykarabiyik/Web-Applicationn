from typing import List
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from .forms import Pdf_kayitForm
from .models import Pdf_kayit

# Create your views here.
liste =  list()

def login(request,pk):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        liste.append(username)
        user= auth.authenticate(username= username, password= password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS,'Oturum Açıldı')
            pk=user.id
            return render(request,'pages/index.html',{'pk':pk})
        else:
            messages.add_message(request,messages.ERROR,'Kullanıcı Adı veya şifre hatalı')
            return redirect('login')

    else:
        return render(request,'user/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Oturumunuz kapatıldı.')
        return redirect('index')


def about(request):
    context={}
    if request.method=='POST':
        uploaded_file=request.FILES['dosya']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
    return render(request,'pages/about.html',context)

def pdf_list(request):
    username=liste[0]
    pdfs=Pdf_kayit.objects.filter(kullanici_adi=request.user)
    return render(request,'pdf_list.html',{
        'pdfs':pdfs
    })
def upload_pdf(request):
    if request.method=='POST':
        form=Pdf_kayitForm(request.POST,request.FILES)
        print(request.user)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form=Pdf_kayitForm()
    return render(request,'upload_pdf.html',{
        'form':form
    })
def delete_pdf(request,pk):
    if request.method=='POST':
        pdf=Pdf_kayit.objects.get(pk=pk)
        pdf.delete()
    return redirect('pdf_list')