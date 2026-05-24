from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')
admin.site.register(Category, CategoryAdmin)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'status', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured','status')