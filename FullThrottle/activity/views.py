from django.http import JsonResponse
from .models import ActivityPeriod
from django.contrib.auth.models import User


def index(request):
    """
    Configuring view to respond to the api call to fetch data from django.
    :param request:
    :return:
    """
    users_list = []
    user_object = {}
    final_object = {}
    users = User.objects.all()
    for user in users:
        user_object['id'] = user.id
        user_object['real_name'] = user.username
        user_object['activity_periods'] = [{'start_time': value.start_time, 'end_time': value.end_time} for value in ActivityPeriod.objects.filter(pk=user.id)]
        users_list.append(user_object)
    final_object['members'] = users_list
    final_object['ok'] = True
    return JsonResponse(final_object, safe=False)
