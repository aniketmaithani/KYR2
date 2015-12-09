from .models import MemberOfParliament
from rest_framework import viewsets
from .serializers import MemberOfParliamentSerializer


class MemberOfParliamentViewSet(viewsets.ModelViewSet):

    '''
    API Endpoint that allows MP to be viewed or edited
    '''

    queryset = MemberOfParliament.objects.all().order_by('name_of_the_mp')
    serializer_class = MemberOfParliamentSerializer
