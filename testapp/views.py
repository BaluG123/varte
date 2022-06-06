from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from . models import News,Product
from taggit.models import Tag
from django.views.generic import DetailView,DeleteView,CreateView,UpdateView
from django.core.paginator import Page,PageNotAnInteger,EmptyPage
from django.db.models import Q
from django.urls import reverse_lazy
from . import forms
from django.http import HttpResponse,HttpResponseRedirect
from attr import fields
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator

# Create your views here.

def list_view(request,tag_slug=None):
    if "q" in request.GET:
        q=request.GET['q']
        news_list=News.objects.filter(Q(title__icontains=q)|Q(body__icontains=q)|Q(titleo__icontains=q)|Q(source__icontains=q))
    else:
        news_list=News.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        news_list=news_list.filter(tags__in=[tag])
    return render(request,'testapp/news_list.html',{'news_list':news_list,'tag':tag})    

class NewsDetailView(DetailView):
    model=News

class NewsCreateView(CreateView):
    model= News
    fields=['title','titleo','link','image','imageo','video','youtube','body','tags','source','credit_link','status']

class NewsUpdateView(UpdateView):
    model=News
    fields=['title','titleo','link','image','imageo','video','youtube','body','tags','source','credit_link','status'] 

class NewsDeleteView(DeleteView):
    model= News
    success_url= reverse_lazy('newslist')
  
def signup_view(request):
    form=forms.SignUpForm()
    if request.method=='POST':
        form=forms.SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})


def Product_ListView(request,tag_slug=None):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    product_list=Product.objects.filter(
        Q(product_name__icontains=q) |
        Q(company1__icontains=q) |
        Q(company2__icontains=q) |
        Q(company3__icontains=q) |
        Q(company4__icontains=q) |
        Q(name1__icontains=q) |
        Q(name2__icontains=q) |
        Q(name3__icontains=q) |
        Q(name4__icontains=q)
    )
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag])
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages)        
    return render(request,'testapp/home.html',{'product_list':product_list,'tag':tag,'products_count':products_count})

def Pelectronic_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='electronics')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/electronics.html',{'product_list':product_list,'products_count':products_count})

def Pfashion_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='fashion')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/fashion.html',{'product_list':product_list,'products_count':products_count})  

def Pother_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='others')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/others.html',{'product_list':product_list,'products_count':products_count})     

def Psports_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='sports')
    products_count = product_list.count()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'testapp/sports.html',{'product_list':product_list,'products_count':products_count})        

class product_create_view(CreateView):
    model= Product
    fields= ['product_name','name1','image1','link1','rprice1','oprice1','off1','company1','product1','name2','image2','link2','rprice2','oprice2','off2','company2','product2','name3','image3','link3','rprice3','oprice3','off3','company3','product3','name4','image4','link4','rprice4','oprice4','off4','company4','product4','publish','tags','status']

class product_update_view(UpdateView):
    model= Product
    fields= ['product_name','name1','image1','link1','rprice1','oprice1','off1','company1','product1','name2','image2','link2','rprice2','oprice2','off2','company2','product2','name3','image3','link3','rprice3','oprice3','off3','company3','product3','name4','image4','link4','rprice4','oprice4','off4','company4','product4','publish','tags','status']

class product_delete_view(DeleteView):
    model= Product
    success_url= reverse_lazy('home')