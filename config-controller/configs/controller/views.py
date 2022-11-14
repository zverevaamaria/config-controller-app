from decimal import Decimal

from django_filters.rest_framework import DjangoFilterBackend
from psycopg2 import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone


from controller.models import Config
from controller.serializers import ConfigSerializer


class ConfigViewSet(ModelViewSet):
    queryset = Config.objects.filter(is_deleted=False)
    serializer_class = ConfigSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service']


    def destroy(self, request, *args, **kwargs):
        config = self.get_object()
        if config.service is None or len(config.service) <= 0:
            try:
                config.is_deleted = True
                config.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except IntegrityError:
                content = {'error': 'IntegrityError'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif len(config.service) > 0:
            content = {'detail': 'config is used by service:' + config.service + ' you can delete this config only if service is null'}
            return Response(content, status=status.HTTP_409_CONFLICT)


    def update(self, request, *args, **kwargs):
        config = self.get_object()
        serializer = self.get_serializer(config, data=request.data, partial=True)
        if serializer.is_valid():
            config.version += Decimal('0.01')
            config.updated_at = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            content = {"message": "failed", "details": serializer.errors}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)





