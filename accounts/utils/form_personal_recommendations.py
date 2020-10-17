import requests

def form_personal_recommendations(request, profile):
    recommendations = "Какие-то рекомендации"
    return recommendations
    data = requests.get(
        'http://' + str(get_current_site(
            request)) + '/api/districts/?district=' + profile.district + 'okrug=' + profile.okrug).json()