from django.contrib import admin
# admin.ModelAdmin lets you define how models appear and behave in the admin site using classes.
# So:
# models.Model → defines data structure
# admin.ModelAdmin → defines admin interface behavior
from .models import Book

#Define a custom admin class for the Book model
#This allows customization of how Book entries appear in the Django Admin panel
class productAdmin(admin.ModelAdmin):
    # Fields to display as columns in the admin list view
    list_display = ['__str__', 'title', 'price','active']
    
    # Make visit_count read-only
    readonly_fields = ('visit_count',)

    # Optional nested Meta class — specifies which model this admin configuration belongs to
    class Meta:
        model = Book

#Register the Book model with its custom admin configuration ---
# This tells Django to use productAdmin when displaying Book entries in the admin interface.
admin.site.register(Book, productAdmin)