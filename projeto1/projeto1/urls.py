from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from outraapp import views
from outraapp.views import register, login_view, logout_view, create_post, edit_post, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create_post/', create_post, name='create_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
