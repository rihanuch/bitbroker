from rest_framework.response import Response
from rest_framework import viewsets
from api.permissions import (
    is_owner
)
from api.v1.serializers.transaction_serializer import TransactionSerializer, Transaction


class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()

    serializer_class = TransactionSerializer
    permission_classes = [
        is_owner.IsOwner
    ]

    def list(self, request):
        queryset = self.request.user.transactions.all()
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
