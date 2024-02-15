from django.contrib import admin
from .models import Post
from .models import Comentario
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 pass
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
 pass
# Register your models here.
