from notice.models import Noticia
from rest_framework import viewsets, permissions
from .serializer import NoticeSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NoticeSerializer