from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

__all__ = (
    'ingredients_create',
)


def ingredients_create(request):
    return HttpResponse('aa')
