from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class PropertyAPIList(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    
    
class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer  
    permission_classes = [IsAuthenticated]  