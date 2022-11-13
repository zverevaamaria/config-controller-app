from django_filters.rest_framework import DjangoFilterBackend
from psycopg2 import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from controller.models import Config
from controller.serializers import ConfigSerializer


class ConfigViewSet(ModelViewSet):
    queryset = Config.objects.filter(is_deleted=False)
    serializer_class = ConfigSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service']


    def destroy(self, request, *args, **kwargs):
        config = self.get_object()
        if len(config.service) > 0:
            content = {'error_message': 'config is used by ' + config.service}
            return Response(content, status=status.HTTP_409_CONFLICT)
        elif len(config.service) <= 0:
            try:
                config.is_deleted = True
                config.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except IntegrityError:
                content = {'error': 'IntegrityError'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)





