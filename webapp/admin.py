from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Book, Author, Category, Lending



admin.site.register(Category)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'authors_list',
        'categories_list',
        'reading_status',
        'cover_image',
    ]

    list_filter = [
        'authors',
        'categories',
        'reading_status',
        'last_reading',
    ]

    actions = [
        'mark_as_read',
    ]

    def authors_list(self, obj):
        return ', '.join([author.name for author in obj.authors.all()])

    def categories_list(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    def cover_image(self, obj):
        if bool(obj.cover) == True:
            return mark_safe('<img width="80" height="auto" src="{}">'.format(obj.cover.url))

    authors_list.__name__ = 'Autores'
    categories_list.__name__ = 'Categorias'
    cover_image.__name__ = 'Foto'

    @admin.action(description='Marcar como lido(s)')
    def mark_as_read(self, request, queryset):
        queryset.update(reading_status='read')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'categories_list',
        'photo_image',
    ]

    list_filter = [
        'categories',
    ]

    def categories_list(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    def photo_image(self, obj):
        if bool(obj.photo) == True:
            return mark_safe('<img width="80" height="auto" src="{}">'.format(obj.photo.url))

    categories_list.__name__ = 'Categorias'
    photo_image.__name__ = 'Foto'

@admin.register(Lending)
class LendingAdmin(admin.ModelAdmin):
    list_display = [
        'book',
        'status',
        'date',
        'estimated_return_date',
    ]

    list_filter = [
        'status',
        'date',
    ]

    actions = [
        'mark_as_returned',
    ]

    @admin.action(description='Marcar como devolvido(s)')
    def mark_as_returned(self, request, queryset):
        queryset.update(status='returned')
