from django.contrib.auth.models import AnonymousUser
from jose import jwt

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS
)

import datetime

def get_auth_id(sub):
    sub = sub[sub.rfind("|")+1:]
    sub = sub[sub.rfind(".")+1:]
    return sub

def get_token_auth_header(request):
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    token = auth.split()[1]
    return token

def is_authenticated(request):
    try :
        token = get_token_auth_header(request)
        claims = jwt.get_unverified_claims(token)
        return claims['exp'] > datetime.datetime.now().toordinal()
    except AttributeError:
        return request.user.is_authenticated

def is_admin(request):
    try :
        token = get_token_auth_header(request)
        claims = jwt.get_unverified_claims(token)
        sub = get_auth_id(claims['sub'])
        return sub == "105081646106925972448"
        # TODO : Move to ENV
    except AttributeError:
        return request.user.is_superuser

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return is_authenticated(request)
        
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        is_owner = False
        try :
            is_owner = is_owner or obj.customer.auth_id == request.user
        except AttributeError:
            is_owner = is_owner or obj.auth_id == request.user
        return is_owner and is_authenticated(request) 

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return is_authenticated(request) and is_admin(request)