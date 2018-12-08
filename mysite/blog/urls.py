from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('gallery/', views.gallery,name='gallery'),
    path('services/', views.services,name='services'),
    path('base/', views.base,name='base'),
    #path('base/', views.base,name='base'),
   

    path('feedback/', views.feedback,name='feedback')
   #path('admin/', admin.site.urls),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)