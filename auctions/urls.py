from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("<int:listing_id>/<int:user_id>/bid", views.bid, name="bid"),
    path("<int:user_id>/new_listing", views.new_listing, name="new_listing"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category_title>", views.category, name="category"),
    path("user/<int:user_id>", views.user_listings, name="user_listings")
]
