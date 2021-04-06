from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from django.http import HttpResponse
import os
from rest_framework import viewsets
from .models import Aliases
from .serializers import AliasesSerializers
# from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


USERNAME = os.environ.get('USERNAME')
DOMAINS_PROVIDED = {"domains": ["swiftmegaminds.tech", "hash.fyi", "hideaddress.net",
                                "mailsire.com", "secret.fyi"]
                    }


# Utility function
def request_get_util(domain=''):
    FORWARD_EMAIL_ENDPOINT = f"https://api.forwardemail.net/v1/domains/{domain}/aliases"
    return requests.get(FORWARD_EMAIL_ENDPOINT, auth=(USERNAME, ''))


def get_aliases(request):
    """
    Returns all the Aliases
    API_ENDPOINT:api/v1/aliases
    """
    res = request_get_util()
    return JsonResponse(res.json(), safe=False)


def get_domains(request):
    """
    REDUNDANT
    Return all the domains
    API_ENDPOINT:api/v1/aliases/domains
    """
    return JsonResponse(DOMAINS_PROVIDED)


@csrf_exempt
def get_alias_filtered(request, DOMAIN):
    """
    Return Domain filtered by domain
    API_ENDPOINT:api/v1/alias/<domains>
    """
    if (request.method == 'GET'):
        res = request_get_util(domain=DOMAIN)
        data = []
        for x in res.json():
            respose_dict = {"name": x["name"],
                            "domain": x["domain"]["name"],
                            "id": x["id"],
                            "recipients": [x["recipients"]],
                            "is_enabled": True}
            data.append(respose_dict)
        return HttpResponse(json.dumps(data))
    elif (request.method == 'POST'):
        res = request_get_util(domain=DOMAIN)
        return JsonResponse(res.json(), safe=False)


def create_alias(request, DOMAIN):
    """
    Returns a POST request
    ENDPOINT : https://api.forwardemail.net/v1/domains/hideaddress.net/aliases
    """
    res = request_get_util(domain=DOMAIN)
    if res.status_code == 200:
        print("addedd the alias")

    return JsonResponse(res.json())
    # If succesfull add the Alias to Database as well


# This is a DRF class which will do POST, GET, FETCH, PATCH on our Alias Model all without adding anything
# Pretty powerfull imo though kinda abstracts everything bit too much
# Keeping this for reference
# Note: should set permission to admin only later
# ENDPOINT: api/v1/users -> will return all the aliases if GET is used
class AliasesViewSet(viewsets.ModelViewSet):
    serializer_class = AliasesSerializers

    def get_queryset(self):
        """Function only for Admin purposes"""
        return Aliases.objects.all()
