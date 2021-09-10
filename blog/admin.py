from django.contrib import admin

# Register your models here.
from .models import BlogPost #, Category , PhotoPost

#admin.site.register(BlogPost)

from markdownx.admin import MarkdownxModelAdmin


admin.site.register(BlogPost, MarkdownxModelAdmin)
