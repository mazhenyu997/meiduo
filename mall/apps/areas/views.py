from .serializers import AreaSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Area


class AreaModelViewSet(ReadOnlyModelViewSet):

    # queryset = Area.objects.all()/
    # serializer_class = AreaSerializer
    def gt_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)

        else:
            return Area.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AreaSerializer
        else:
            return AreaSerializer





