from . import views
from django.urls import path

urlpatterns = [
    path("", views.index,  name="ShopHome"),
    path("about/", views.about,  name="AboutUs"),
    path("contact/", views.contact,  name="ContactUs"),
    path("tracker/", views.tracker,  name="TrackingStatus"),
    path("search/", views.search,  name="Search"),
    path("productview/", views.productView,  name="ProductView"),
    path("checkout/", views.checkout,  name="Checkout"),
    path("login/", views.login,  name="Login"),
    path("register/", views.register,  name="Register"),
    path("cart/", views.cart,  name="Cart"),
    

]
