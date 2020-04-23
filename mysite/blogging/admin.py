from django.contrib import admin
from blogging.models import Post, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ["posts"]

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, CommentInline]
