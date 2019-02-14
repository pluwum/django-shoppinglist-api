from rest_framework.viewsets import ModelViewSet
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer, ShoppingListDetailSerializer
from .models import ShoppingList, ShoppingListItem
from rest_framework.response import Response


class ShoppingListViewSet(ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def retrieve(self, request, pk=None):
        serializer = ShoppingListDetailSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ShoppingListItemViewSet(ModelViewSet):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
