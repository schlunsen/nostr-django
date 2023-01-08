from django.shortcuts import render
from django.http import JsonResponse
from .models import Nip05User
from .serializers import Nip05UserSerializer


def well_known(request):
    users = Nip05User.objects.all()
    name = request.GET.get('name')
    if name:
        users = users.filter(name=name)

    names_dict = {}
    for u in users:
        names_dict[u.name] = u.pub_key

    data = {
        "names": names_dict
    }
    if name:
        data['relays'] = {
            users.first().pub_key: [x.url for x in users.first().relays.all()]

        }
    return JsonResponse(data, safe=False)


