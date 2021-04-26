from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
class BookstoreAdminArea(admin.AdminSite):
    site_header = 'BookStore Admin Area'

bookstore_site = BookstoreAdminArea(name='BookstoreAdmin')


