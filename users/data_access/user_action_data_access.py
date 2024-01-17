from users.consts import MAX_USER_ACTION_ROWS
from users.models import UserAction, ArchivedUserAction
from django.db import transaction


class UserActionDataAccess:

    @classmethod
    @transaction.atomic()
    def create_user_action(cls, user, action):
        """
        This function is atomic and locks User Action table
        so every time one row is inserted and one row removed.
        """
        user_action = UserAction.objects.create(user=user, action=action)
        user_actions = UserAction.objects.select_for_update()
        if user_actions.count() > MAX_USER_ACTION_ROWS:
            user_action_to_archive = user_actions.earliest('created_at')
            ArchivedUserAction.objects.create(
                user=user_action_to_archive.user,
                action=user_action_to_archive.action
            )
            user_action_to_archive.delete()
        return user_action

