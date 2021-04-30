from django.apps import AppConfig


class BlogAdminConfig(AppConfig):
    default_site = 'blog.admin.BlogAdminArea'
    




class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
