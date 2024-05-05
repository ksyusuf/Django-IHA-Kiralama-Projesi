from django.urls import path
from . import views

# http://127.0.0.1:8000/            => homepage
# http://127.0.0.1:8000/index       => homepage
# http://127.0.0.1:8000/blogs       => blogs
# http://127.0.0.1:8000/blogs/3     => blog-details

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),

    path("ihalar", views.ihalar, name="ihalar"),

    # path("rentables/", views.rentables, name="rentables"),
    path("rentable-detail/<int:id>", views.rentable_detail, name="rentable_detail"),
    #
    path("renteds", views.renteds, name="renteds"),
    # path("rented-detail/<int:id>", views.rented_detail, name="rented-detail"),

    path("renting/<int:id>", views.renting, name="renting"),

    path("rent-update/<int:id>", views.rent_update, name="rent-update"),
    path("rent-delete", views.rent_delete, name="rent-delete")
]