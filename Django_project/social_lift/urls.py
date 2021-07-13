from django.urls import path
from . import views
urlpatterns = [
    path("index", views.HomePage),
    path("birthday", views.WishingExpress, name="wishexp"),
    path("multipost", views.MultiPost, name="mpost"),
    path("info", views.Info, name="infomation"),
]
