from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from users.services.user_action_service import UserActionService
from users.services.user_service import UserService


class UserView(ModelViewSet):
    service = UserService

    def create(self, request, *args, **kwargs):
        response = self.service.create_user(request.data)
        return response

    def list(self, request, *args, **kwargs):
        response = self.service.get_users()
        return response

    def retrieve(self, request, *args, **kwargs):
        response = self.service.get_user(user_id=kwargs.get('pk'))
        return response

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        response = self.service.update_user(
            request.data,
            user_id=kwargs.get('pk'),
            partial=partial
        )
        return response

    def partial_update(self, request, *args, **kwargs):
        response = self.service.update_user(
            request.data,
            user_id=kwargs.get('pk'),
            partial=True
        )
        return response

    def destroy(self, request, *args, **kwargs):
        response = self.service.delete_user(user_id=kwargs.get('pk'))
        return response


class UserActionView(CreateModelMixin, GenericViewSet):

    service = UserActionService

    def create(self, request, *args, **kwargs):
        response = self.service.create_user_action(request.data)
        return response
