"""localnews4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('',views.list_view,name="newslist"),
    path('<int:pk>',views.NewsDetailView.as_view(),name="detail"),
    path('tag/(?p<tag_slug>[-\w]/$',views.list_view,name="news_tag"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',views.signup_view,name="signup"),
    path('update/<int:pk>',views.NewsUpdateView.as_view(),name="update"),
    path('delete/<int:pk>',views.NewsDeleteView.as_view(),name="delete"),
    path('create/',views.NewsCreateView.as_view(),name="create"),
    path('marketplace/',views.Product_ListView,name="home"),
    path('fashion/',views.Pfashion_view,name="fashion"),
    path('electronics/',views.Pelectronic_view,name="electronic"),
    path('tag/(?p<tag_slug>[-\w]/$',views.Product_ListView,name="product_tag"),
    path('tag/(?p<tag_slug>[-\w]/$',views.Pelectronic_view,name="product_tag"),
    path('tag/(?p<tag_slug>[-\w]/$',views.Pfashion_view,name="product_tag"),
    path('addp/',views.product_create_view.as_view(),name="addproduct"),
    path('updatep/<int:pk>',views.product_update_view.as_view(),name="updateproduct"),
    path('deletep/<int:pk>',views.product_delete_view.as_view(),name="deleteproduct"),
    path('others/',views.Pother_view,name="others"),
    path('sports/',views.Psports_view,name="sports")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)