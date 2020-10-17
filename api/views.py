from datetime import datetime
from rest_framework.views import APIView
from django.http import JsonResponse
from .apps import ApiConfig


class DistrictsView(APIView):
    def get(self, request):
        district = request.GET.get('district', None)
        date = request.GET.get('date', str(datetime.date(datetime.now())))
        # запрос вида api/districts/
        if district is None:
            districts = ApiConfig.districts
            response = {}
            response["date"] = date
            response["districts"] = {}
            for district in districts:
                vector = ApiConfig.vectorizer.transform([district])
                prediction = ApiConfig.regressor.predict(vector)[0]
                response["districts"][district] = prediction

        # запрос вида api/districts/?district=26
        else:
            # формируем данные, на основе которых будет прогноз
            vector = ApiConfig.vectorizer.transform([district])
            # прогноз
            prediction = ApiConfig.regressor.predict(vector)[0]
            # ответ пока захардкодил
            response = {
                "id": district,
                "date": date,
                "name": "Lefortovo",
                "danger_level": prediction,
                "propagation_speed": {
                    "0-18 years": 500,
                    "18-60 years": 100,
                    "60-100 years": 30,
                    "total": 630,
                },
                "recommendation": "Какая-то рекомендация",
                }
        return JsonResponse(response)
