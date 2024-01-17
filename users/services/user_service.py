from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response

from users.consts import Action
from users.data_access.user_data_access import UserDataAccess
from users.models import User
from users.serializers import UserSerializer
from users.services.user_action_service import UserActionService


def get_validated_data(data, serializer_class, context=None, partial=False):
    serializer = serializer_class(data=data, partial=partial, context=context)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data


class UserService:

    data_access = UserDataAccess
    user_action_service = UserActionService

    @classmethod
    def create_user(cls, data):
        try:
            validated_data = get_validated_data(data, UserSerializer)
        except ValidationError as validation_error:
            return Response(validation_error.detail, status=status.HTTP_400_BAD_REQUEST)
        user = cls.data_access.create_user(validated_data)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @classmethod
    def get_users(cls):
        users = cls.data_access.get_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @classmethod
    def get_user(cls, user_id):
        try:
            user = cls.data_access.get_user(user_id)
        except User.DoesNotExist:
            return Response('user does not exists', status=status.HTTP_404_NOT_FOUND)
        # user = cls.get_user_by_id(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @classmethod
    def update_user(cls, data, user_id, partial):
        try:
            user = cls.data_access.get_user(user_id)
        except User.DoesNotExist:
            return Response('user does not exists', status=status.HTTP_404_NOT_FOUND)
        # user = cls.get_user_by_id(user_id)
        try:
            validated_data = get_validated_data(data, UserSerializer, context={'update': True}, partial=partial)
        except ValidationError as validation_error:
            return Response(validation_error.detail, status=status.HTTP_400_BAD_REQUEST)
        user = cls.data_access.update_user(user, validated_data)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @classmethod
    def get_user_by_id(cls, user_id):
        try:
            user = cls.data_access.get_user(user_id)
        except User.DoesNotExist:
            raise NotFound(f'user does not exists.')
        return user

    @classmethod
    def delete_user(cls, user_id):
        try:
            user = cls.data_access.get_user(user_id, is_deleted=False)
        except User.DoesNotExist:
            return Response('user does not exists', status=status.HTTP_404_NOT_FOUND)
        cls.data_access.delete_user(user)
        cls.user_action_service.create_user_action({'user': user, 'action': Action.DELETED}, for_delete=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
