from django.contrib import admin
from django.utils.html import format_html
from .models import MainCategory, SubCategory, Product


# SubCategory Admin
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')  # Display name and image in the admin list
    search_fields = ('name',)  # Allow searching by subcategory name

    def get_image(self, obj):
        if obj.image:  # Check if the image exists
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;"/>',
                obj.image.url
            )
        return 'No Image'
    get_image.short_description = 'Image'


# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subcategories', 'main_category', 'type', 'get_image')
    list_filter = ('subcategories', 'main_category', 'type')  # Updated fields for filtering
    search_fields = ('name', 'description')

    def get_subcategories(self, obj):
        """Fetch all subcategories associated with the product."""
        return ', '.join([subcategory.name for subcategory in obj.subcategories.all()])
    get_subcategories.short_description = 'Subcategories'

    def get_image(self, obj):
        if obj.image:  # Check if the image exists
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;"/>',
                obj.image.url
            )
        return 'No Image'
    get_image.short_description = 'Image'


# MainCategory Admin
@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Display name and slug
    search_fields = ('name',)  # Allow searching by main category name


# Register Product with the custom admin
admin.site.register(Product, ProductAdmin)