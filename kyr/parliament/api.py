# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import MemberOfParliament
from rest_framework import generics
from .serializers import MemberOfParliamentSerializer
from rest_framework.permissions import AllowAny


class MemberOfParliamentViewSet(generics.ListAPIView):

    '''
    API Endpoint that allows MP's Parliament Related Details to be viewed
    '''

    permission_classes = (AllowAny, )
    queryset = MemberOfParliament.objects.all()
    serializer_class = MemberOfParliamentSerializer
