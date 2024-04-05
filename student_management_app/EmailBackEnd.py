# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=arguments-differ
# pylint: disable=no-else-return

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend



class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
    