# listings/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ListingListAPIView(APIView):
    """
    API view to retrieve a list of sample travel listings.
    """
    def get(self, request, format=None):
        """
        Returns a list of sample listings.
        """
        listings = [
            {"id": 1, "title": "Beachfront Villa", "location": "Maldives"},
            {"id": 2, "title": "Mountain Cabin", "location": "Swiss Alps"},
            {"id": 3, "title": "City Apartment", "location": "Paris"}
        ]
        return Response(listings, status=status.HTTP_200_OK)
