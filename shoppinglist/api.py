from rest_framework.viewsets import ModelViewSet
from .serializers import ShoppingListSerializer
from .models import ShoppingList


class ShoppingListViewSet(ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
