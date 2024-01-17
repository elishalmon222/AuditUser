from users.consts import MAX_USER_ACTION_ROWS
from users.models import User, UserAction, ArchivedUserAction


class UserActionDataAccess:

    @classmethod
    def create_user_action(cls, user, action):
        user_action = UserAction.objects.create(user=user, action=action)
        if UserAction.objects.count() > MAX_USER_ACTION_ROWS:
            user_action_to_archive = UserAction.objects.earliest('created_at')
            ArchivedUserAction.objects.create(
                user=user_action_to_archive.user,
                action=user_action_to_archive.action
            )
            user_action_to_archive.delete()
        return user_action
