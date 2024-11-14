from django import forms

# Events Form
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time','description', 'location']


# Partnership Opportunities
from .models import Opportunity

class PartnershipForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['job_title', 'company', 'job_description', 'qualifications', 'contact_details']

# News
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'author']

# Contact form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


# Commercial Shop
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'stock']