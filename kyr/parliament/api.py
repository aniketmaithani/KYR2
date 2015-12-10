# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import MemberOfParliament
from rest_framework import viewsets
from .serializers import MemberOfParliamentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class MemberOfParliamentViewSet(viewsets.ModelViewSet):

    '''
    API Endpoint that allows MP to be viewed or edited
    '''

    permission_classes = (AllowAny, )
    queryset = MemberOfParliament.objects.all().order_by('name_of_the_mp')
    serializer_class = MemberOfParliamentSerializer

    def retrieve(self, request, pk=None):
        queryset = MemberOfParliament.objects.all().order_by('name_of_the_mp')
        serializer = MemberOfParliamentSerializer(queryset)
        return Response(serializer.data)