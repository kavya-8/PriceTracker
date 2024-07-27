from django.shortcuts import render, redirect
from .forms import PriceTrackForm
from .price_tracker import track_price

def index(request):
    if request.method == 'POST':
        form = PriceTrackForm(request.POST)
        if form.is_valid():
            product_link = form.cleaned_data['product_link']
            email = form.cleaned_data['email']
            desired_price = form.cleaned_data['desired_price']
            track_price(product_link, desired_price, email)
            return redirect('success')
    else:
        form = PriceTrackForm()
    return render(request, 'index.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def login(request):
    if request.method == 'POST':
        # Handle login logic here
        return redirect('index')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        return redirect('index')
    return render(request, 'signup.html')