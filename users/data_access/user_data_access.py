from users.models import User


class UserDataAccess:

    @classmethod
    def create_user(cls, data):
        user = User.objects.create(**data)
        return user

    @classmethod
    def get_users(cls):
        users = User.objects.all()
        return users

    @classmethod
    def get_user(cls, user_id, is_deleted=None):
        query_filter = {'id': user_id}
        if is_deleted is not None:
            query_filter['is_deleted'] = is_deleted
        user = User.objects.get(**query_filter)
        return user

    @classmethod
    def update_user(cls, user, data):
        for field, value in data.items():
            setattr(user, field, value)
        user.save()
        return user

    @classmethod
    def delete_user(cls, user):
        user.is_deleted = True
        user.save()
