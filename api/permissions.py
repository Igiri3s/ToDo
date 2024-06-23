from rest_framework.permissions import BasePermission
import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from users.models import User

class IsAuthenticatedCustom(BasePermission):
    def has_permission(self, request, view):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')

        request.user = User.objects.filter(id=payload['id']).first()
        if request.user is None:
            raise AuthenticationFailed('User not found')

        return True
