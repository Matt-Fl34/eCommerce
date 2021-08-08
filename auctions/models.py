from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self): 
        return self.title


class ListingManager(models.Manager):
    def create_listing(self, category, title, description, image, user, bid, date, end_date):
        listing = self.create(category=category, title=title, description=description, image=image, user=user, bid=bid, date=date, end_date=end_date)
        return listing



class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings", blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=350)
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings", blank=True, null=True)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(blank=True, null=True)

    objects = ListingManager()    

    def __str__(self):
        return self.title



class BidManager(models.Manager):
    def create_bid(self, listing, amount, user):
        bid = self.create(listing=listing, amount=amount, user=user)
        return bid



class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids", blank=True, null=True)

    objects = BidManager()

    def __str__(self):
        return f"{self.user} (${self.amount}) Listing:{self.listing}" 



class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()  



