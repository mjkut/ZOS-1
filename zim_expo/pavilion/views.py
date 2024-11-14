from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
# For Events
from django.shortcuts import render, redirect
from.forms import EventForm
from .models import Event
# For Opportunities
from .models import Opportunity  # Import Opportunity model
from .forms import PartnershipForm
# For News
from .models import News
from .forms import NewsForm
# For Contact
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
# For Shop
from .forms import ProductForm
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def footer(request):
    return render(request, 'footer.html')

# Nav pages
def tourism(request):
    return render(request, 'experience_zim/tourism.html')

def map(request):
    return render(request, 'experience_zim/map.html')

# Exhibits
def art(request):
    return render(request, 'exhibits/art_craft.html')

def music(request):
    return render(request, 'exhibits/music.html')

def interactive(request):
    return render(request, 'exhibits/interactive.html')

# Opportunities
def industries(request):
    return render(request, 'opportunities/industries.html')

def investment(request):
    return render(request, 'opportunities/investment.html')

def partnerships(request):
    opportunities = Opportunity.objects.all() # Fetch all opportunities from the database
    partnership_form = PartnershipForm()

    if request.method == "POST" and request.user.is_staff:
        partnership_form = PartnershipForm(request.POST)
        if partnership_form.is_valid():
            partnership_form.save()
            return redirect('partnerships')
        else:
            partnership_form = PartnershipForm()

    return render(request, 'opportunities/partnerships.html', {'opportunities': opportunities, 'partnership_form': partnership_form})

#============== Events pages===================#

          # Schedule page
def schedule(request):
    events = Event.objects.all()  # Fetch all events
    event_form = EventForm()
    
    if request.method == "POST" and request.user.is_staff:
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('schedule')
        else:
            event_form = EventForm()

    return render(request, 'events/schedule.html', {'events': events, 'event_form': event_form})

 # Live Stream
def live(request):
    return render(request, 'events/live_streaming.html')

# News 
def news(request):
    news_items = News.objects.all().order_by('-date_posted')  # Fetch all news items from the database
    news_form = NewsForm()

    if request.method == "POST" and request.user.is_staff:  # Check if the user is an admin
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news_form.save()
            return redirect('news')  # Redirect to the news page after submission
        else:
            news_form = NewsForm()

    return render(request, 'news.html', {'news_items': news_items, 'news_form': news_form})

# Contact View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            # Set your personal email address here
            personal_email = 'youremail@example.com'  # Replace this with your personal email address

            # Send the email to your personal email address
            send_mail(
                f"New Inquiry from {name}: {subject}",
                message,
                from_email,
                [personal_email],  # This is the personal email where the inquiry will be sent
                fail_silently=False,
            )
            return redirect('contact')  # Redirect to contact page after sending the message
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Our Future
def future(request):
    return render(request, 'future.html')

# Commercial Shop
def shop(request):
    products = Product.objects.all()
    product_form = ProductForm()

    if request.method == "POST" and request.user.is_staff:
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('products')
        else:
            product_form = ProductForm()

    return render(request, 'products.html', {'products': products, 'product_form': product_form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'yourapp/product_detail.html', {'product': product})