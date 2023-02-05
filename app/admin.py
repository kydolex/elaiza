
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post,Maker,Car,Item

admin.site.register(Post)
admin.site.register(Maker)
admin.site.register(Car)
admin.site.register(Item)