from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.

API_KEY = 1


def get_aliases(request):
    res = requests.get(
        f"https://www.thecocktaildb.com/api/json/v1/{ API_KEY }/search.php?s=margarita")
    return JsonResponse(res.json())
