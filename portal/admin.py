from django.contrib import admin
from .models import Contact,currentevents,links,news,Register

# Register your models here.
admin.site.register(Contact)
admin.site.register(currentevents)
admin.site.register(links)
admin.site.register(news)
admin.site.register(Register)
# admin.site.register(Imageupload