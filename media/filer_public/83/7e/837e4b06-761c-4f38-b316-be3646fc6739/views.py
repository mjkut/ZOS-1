from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def footer(request):
    return render(request, 'footer.html')

# Nav pages
