from django.urls import path

from .views import FoodItemsDestroyView, FoodItemsView

urlpatterns = [
    path("", FoodItemsView.as_view(), name="baseFood"),
    path("delete/", FoodItemsDestroyView.as_view(), name="destroyFood"),
]
