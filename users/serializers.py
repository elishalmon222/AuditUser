from rest_framework import serializers as rfs

from users.models import User, UserAction


class UserSerializer(rfs.ModelSerializer):

    def __init__(self, *args, **kwargs):
        if context := kwargs.get('context', {}):
            if context.get('update') is True:
                self.fields['username'].read_only = True
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )


class UserActionSerializer(rfs.ModelSerializer):
    class Meta:
        model = UserAction
        fields = ('user', 'action')
