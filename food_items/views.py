import json

from rest_framework.generics import DestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import FoodItem
from .serializers import FoodModelSerializer


class FoodItemsView(ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodModelSerializer


class FoodItemsDestroyView(DestroyAPIView):
    queryset = FoodItem.objects
    serializer_class = FoodModelSerializer

    def destroy(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        food_item = self.get_queryset().get(pk=data["pk"])
        food_item.delete()

        return Response(True)
