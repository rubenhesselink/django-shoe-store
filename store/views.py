from django.shortcuts import render
from .models import Shoe


def listing_view(request):
    shoe = Shoe.objects.all().order_by('-date_added')

    return render(request, 'store/shoe-listing.html', {'shoes':shoe})