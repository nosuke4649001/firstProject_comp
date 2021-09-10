from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from .models import BlogPost #, Category , PhotoPost

<<<<<<< HEAD
#admin.site.register(BlogPost)

from markdownx.admin import MarkdownxModelAdmin


admin.site.register(BlogPost, MarkdownxModelAdmin)
=======
admin.site.register(BlogPost, MarkdownxModelAdmin)

>>>>>>> b0254daaf1feb3a7a4673f4c3cbb6ebbd8bfd450
