from django.contrib import admin

# Register your models here.
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'description', 'location')
    list_filter = ('date',)
    search_fields = ('name', 'description')

admin.site.register(Event, EventAdmin)

# For Opportunities
from .models import Opportunity

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'job_description', 'qualifications', 'contact_details', 'date_posted')
    search_fields = ('job_title', 'job_description')
    list_filter = ('date_posted',)

admin.site.register(Opportunity, OpportunityAdmin)


# News
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)

admin.site.register(News, NewsAdmin)

# Commercial Shop
from .models import Product
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'description', 'price', 'stock', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('name',)

admin.site.register(Product, ProductAdmin)