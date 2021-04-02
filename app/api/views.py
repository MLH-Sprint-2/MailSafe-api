from django.shortcuts import render
import requests
from django.http import JsonResponse
import json


# with open('./config.json') as config_file:
#     config = json.load(config_file)
DOMAINS = {"domain": ["hash.fyi", "hideaddress.net",
                      "mailsire.com", "secret.fyi"]
           }


def get_aliases(request):
    """
    Returns all the Aliases
    API_ENDPOINT:api/v1/aliases
    """
    res = requests.get(
        "https://api.forwardemail.net/v1/domains/hideaddress.net/aliases", auth=("48f734d41b6ccd608e021093", ''))
    return JsonResponse(res.json(), safe=False)


def get_domains(request):
    """Return all the domains
       API_ENDPOINT:api/v1/aliases
    """
    return JsonResponse(DOMAINS)


def get_alias_filtered(request):
    """Return Domain filtered by domain
       API_ENDPOINT:api/v1/aliases/<domains>"""
    pass
