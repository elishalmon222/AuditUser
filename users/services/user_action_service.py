from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from users.data_access.user_action_data_access import UserActionDataAccess
from users.serializers import UserActionSerializer
from users.utils import get_validated_data


class UserActionService:

    data_access = UserActionDataAccess

    @classmethod
    def create_user_action(cls, data, for_delete=False):
        if for_delete:
            cls.data_access.create_user_action(**data)
            return
        try:
            validated_data = get_validated_data(data, UserActionSerializer)
        except ValidationError as validation_error:
            return Response(validation_error.detail, status=status.HTTP_400_BAD_REQUEST)
        user_action = cls.data_access.create_user_action(**validated_data)
        serializer = UserActionSerializer(user_action)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


