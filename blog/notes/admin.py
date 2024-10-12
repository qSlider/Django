from django.contrib import admin
from .models import Post
from .models import Author
from .models import Note, Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Note)
admin.site.register(Category)