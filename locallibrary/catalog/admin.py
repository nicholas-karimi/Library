from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language



class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    list_display = ('title', 'author', display_genre)
     
    inlines = [BooksInstanceInline]


class AuthorAdmin(admin.ModelAdmin):
    
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
        }),
        ('Books', {
            'fields': ('title', 'author')
        }),
    )


# Register the Admin classes for BookInstanceAdmin using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    # section the detail view of the BI
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    ) #-> None -> depicts no title for the section - > Availabilty -> Title for the status section



# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Language)
admin.site.register(Genre)
