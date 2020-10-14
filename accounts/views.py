import requests
from django.contrib.sites.shortcuts import get_current_site
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
        recommendations = form_personal_recommendations(request, profile)
        if recommendations != profile.recommendations:
            profile.recommendations = recommendations
            profile.save()
        profile = UserProfile.objects.filter(user=self.request.user)
        serializer = self.serializer_class(profile, many=True)
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

def form_personal_recommendations(request, profile):
    recommendations = "Не рекомендуется выходить из дома"
    data = requests.get(
        'http://' + str(get_current_site(request)) + '/api/districts/?district=' + profile.location).json()
    if data["propagation_speed"]["60-100years"] > 500:
        if profile.age >= 60:
            return recommendations


def send_sms(phone, recommendations, mainsms=None):
    project = 'firstproject__1'  # Имя проекта
    api_key = '296e1b8d69f949747ec706657cca3cf4'  # API-ключ

    sms = mainsms.SMS(project, api_key)  # Создаём объект

    # отправка SMS на указанный номер или номера "recipients", с указанным текстом "text"
    sms.sendSMS("79645161910",
                "C новым годом Кирилл Андреевич, да, да. Это отправил бот!")



