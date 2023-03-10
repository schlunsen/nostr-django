from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from .models import Nip05User, Wallet, Payment
from .serializers import Nip05UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, viewsets
from rest_framework.views import APIView

class Nip05UserViewSet(viewsets.ModelViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Nip05User.objects.all()
    serializer_class = Nip05UserSerializer
    lookup_field = 'name'
    


@csrf_exempt
def create_registration(request):
    username = request.POST.get('username', "test")
    pub_key = request.POST.get('pub_key', "test")
    wallet = Wallet.objects.first()
    amount = 2500
    payment = Payment.objects.create(
        username=username, pub_key=pub_key, wallet=wallet)
    payment.generate_invoice(amount=amount)
    data = {
        "payment_id": payment.id,
        "lnurl": payment.lnurl,
        "amount": amount,
        "management_code": payment.management_code,
        "domain": settings.DOMAIN,
        "username": payment.username
    }
    return JsonResponse(data, safe=False)


def well_known(request):
    users = Nip05User.objects.all()
    name = request.GET.get('name',)
    if name:
        p = Payment.objects.filter(username=name).filter(
            paid_at__isnull=True).last()
        if p:
            p.confirm_payment()
        users = users.filter(name=name)

    names_dict = {}
    for u in users:
        names_dict[u.name] = u.hex_key or u.pub_key

    data = {
        "names": names_dict
    }

    if name and users:

        data['relays'] = {
            users.first().hex_key: [x.url for x in users.first().relays.all()]

        }
    return JsonResponse(data, safe=False)
