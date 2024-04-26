from django.shortcuts import render,redirect
from .models import Listing
from .forms import ListingForm

def listing_list(request):
    # Retrieve all listings from the database
    listings = Listing.objects.all()
    
    # Define the context dictionary with the queryset
    context = {
        'listings': listings
    }
    # Render the template with the context
    return render(request, 'listings.html', context)
def listing_retrieve(request,pk):
    listing = Listing.objects.get(id=pk)
    context = {
         "listing":listing
    }
    return render(request,"listing.html",context)
    import requests
def listing_create(request):
    form = ListingForm()  # Create an instance of the form
    if request.method == "POST":
        form = ListingForm(request.POST)  # Bind data to the form
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the form data to the database
            return redirect("/")  # Redirect to the homepage after successful form submission

    context = {
        "form": form  # Pass the form to the template context
    }
    return render(request, "listing_create.html", context)  # Render the template with the form