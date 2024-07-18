from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from core.models.request_history import RequestHistory
from api.serializers.request_history import RequestHistorySerializer
from api.pagination import ListedPagination


class TownsStatistic(GenericAPIView, mixins.ListModelMixin):
    model = RequestHistory
    queryset = RequestHistory.objects.all()
    serializer_class = RequestHistorySerializer
    pagination_class = ListedPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
