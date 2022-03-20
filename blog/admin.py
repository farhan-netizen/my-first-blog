from django.contrib import admin
from .models import Post

class PostAdminModel(admin.ModelAdmin):
    search_fields=('title',)


admin.site.register(Post, PostAdminModel)