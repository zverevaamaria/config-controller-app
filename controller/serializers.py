from rest_framework.serializers import ModelSerializer

from controller.models import Config


class ConfigSerializer(ModelSerializer):
    class Meta:
            model = Config
            fields = ('id', 'service', 'data', 'version')
