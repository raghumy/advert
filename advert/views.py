from rest_framework import viewsets
from advert.models import Advertiser
from advert.serializers import AdvertSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route

class AdvertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Advertiser.objects.all()
    serializer_class = AdvertSerializer

    def list(self, request):
        print("Advertiser {}".format(request.user.id))
        queryset = Advertiser.objects.all()
        serializer = AdvertSerializer(queryset, many=True)
        return Response(serializer.data)
