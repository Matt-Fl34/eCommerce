from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from datetime import datetime

from .models import User, Listing, Bid, Category


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    bids = Bid.objects.filter(listing=listing)
    top_bid_user = bids.last().user
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bids": bids,
        "bid_count": len(bids)-1,# -1 to compensate for the fact that the first 'bid' was set by the user who created the listing, there should be 0 bids at the start
        "top_bid_user": top_bid_user,
    })


def bid(request, listing_id, user_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        current_bid = listing.bid
        user = User.objects.get(pk=user_id)
        new_bid = float(request.POST["bid"])
        top_bid_user = Bid.objects.filter(listing=listing).last().user

        # check that user isn't bidding on their own listing
        if user == listing.user:
            messages.info(request,"You are not allowed to bid on your own listing.")
            return HttpResponseRedirect(reverse("listing", args=(listing_id,))) 

        # check that user doesn't already have the highest bid    
        if user == top_bid_user:
            messages.info(request, "You already hold the highest bid on this item.")        
            return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

        # check if new bid is higher than current bid
        if new_bid > current_bid:
            # create new Bid object and update Listing.bid field to reflect new highest bid
            bid = Bid.objects.create_bid(listing, new_bid, user)
            Listing.objects.filter(pk=listing_id).update(bid=new_bid)
        else:
            messages.info(request, "Your bid must be higher than the current bid.")
            return HttpResponseRedirect(reverse("listing", args=(listing_id,)))    

    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))


def new_listing(request, user_id):
    if request.method == "POST":
        category = Category.objects.get(title=request.POST["category"])
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        user = User.objects.get(pk=user_id)
        bid = request.POST["bid"]
        date = datetime.now()
        end_date = request.POST["end_date"]

        # check that the end date is later than the current date
        if end_date < str(date):
            messages.info(request, "End date must be later than the current date.")
            return HttpResponseRedirect(reverse("new_listing", args=(user_id,)))

        # create new listing object
        listing = Listing.objects.create_listing(category, title, description, image, user, bid, date, end_date)
        # create new bid object
        bid = Bid.objects.create_bid(listing, bid, user)
        return HttpResponseRedirect(reverse("listing", args=(listing.id,)))
    
    return render(request, "auctions/new_listing.html", {
        "categories": Category.objects.all()
    })        

def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })

def category(request, category_title):
    category = Category.objects.get(title=category_title)
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "category": category
    })

def user_listings(request, user_id):
    listing_user = User.objects.get(pk=user_id)
    listings = Listing.objects.filter(user=listing_user)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "listing_user": listing_user
    })    