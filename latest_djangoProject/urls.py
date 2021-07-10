"""latest_djangoProject URL Configuration

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
from new_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('',views.display_list_view.as_view(),name='home'),
    path('create/',views.display_create_view.as_view(template_name ='new_app/dispaly_create.html'),name='create'),
    path('detail/<int:pk>',views.display_detail_view.as_view(),name='detail'),
    path('update/<int:pk>',views.display_update_view.as_view(template_name= 'new_app/display_update.html'),name='update'),
    path('delete/<int:pk>',views.display_delete_view.as_view(template_name= 'new_app/display_confirm_delete.html'),name='delete')

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
