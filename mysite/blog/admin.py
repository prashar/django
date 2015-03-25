from django.contrib import admin
from blog.models import Post 

class PostAdmin(admin.ModelAdmin):
	list_display=('title','created')

# Register your models here.
# admin.site.register(Post,PostAdmin)
admin.site.register(Post)