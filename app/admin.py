
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post,Category,Blog_Post,LikePostAll,LikePost,ShopCategory,CarCategory

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(ShopCategory)
admin.site.register(CarCategory)
admin.site.register(Blog_Post, MarkdownxModelAdmin)
admin.site.register(LikePostAll)
admin.site.register(LikePost)