from typing import AnyStr
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request

from .models import SalesItem
from .serializers import SalesItemSerializer

class SalesItemViewSet(viewsets.ModalViewSet):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer

    def list(self, request: Request, *args: tuple[Any], **kwargs: dict[str, Any]) -> Response:
        user_account_id = request.query_params.get('user_account_id')

        queryset = (
            SalesItem.objects.all()
            if user_account_id is None
            else SalesItem.objects.filter(user_account_id=user_account_id)
        )

        serialzer = SalesItemSerializer(queryset, many=True)
        return Response(serialzer.data)