from rest_framework import serializers
from .models import Noticia

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
        read_only_fields = ('created_at',)