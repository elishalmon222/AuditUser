from django.contrib.auth.models import AbstractUser
from django.db import models

from users.consts import Gender, Action


class User(AbstractUser):
    gender = models.CharField(choices=Gender.CHOICES, max_length=8)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class AbstractUserAction(models.Model):
    action = models.CharField(choices=Action.CHOICES, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserAction(AbstractUserAction):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')

    class Meta:
        db_table = 'user_action'
        verbose_name = 'User Action'
        verbose_name_plural = 'User Actions'

    def __str__(self):
        return f'{self.user} - {self.action}'


class ArchivedUserAction(AbstractUserAction):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='archived_actions')

    class Meta:
        db_table = 'archived_user_action'
        verbose_name = 'Archived User Action'
        verbose_name_plural = 'Archived User Actions'

    def __str__(self):
        return f'{self.user} - {self.action}'
