from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get(self, request):
        profile = UserProfile.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = UserProfile.objects.filter(user=self.request.user).first()
        data = request.data
        serializer = self.serializer_class(instance=profile, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            profile_saved = serializer.save()
        return Response({
            "success": "Profile '{}' updated successfully".format(profile.id)
        })
