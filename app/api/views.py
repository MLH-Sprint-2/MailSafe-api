from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from django.http import HttpResponse
import os
# from rest_framework.response import Response

USERNAME = os.environ.get('USERNAME')
DOMAINS_PROVIDED = {"domains": ["swiftmegaminds.tech","hash.fyi", "hideaddress.net",
                                "mailsire.com", "secret.fyi"]
                    }

# Send to environment variable


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


def get_alias_filtered(request, DOMAIN):
    """
    Return Domain filtered by domain
    API_ENDPOINT:api/v1/alias/<domains>
    """
    # if(DOMAIN not in DOMAINS_PROVIDED):
    #     response_data = {
    #         "status": "invalid domain",
    #     }
    #     return Response(data=response_data, status=400, headers=None, content_type="application/json")

    res = request_get_util(domain=DOMAIN)
    data = []
    for x in res.json():
        if x["domain"]["name"] == DOMAIN:
            data.append(x)
    return JsonResponse(data, safe=False)
