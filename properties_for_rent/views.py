from django.shortcuts import render
from .models import Listing

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
    