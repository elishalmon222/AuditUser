from django.contrib import admin

from users.models import User, UserAction, ArchivedUserAction


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    fields = (
        'username',
        'email',
        'first_name',
        'last_name',
        'gender',
        'is_deleted'
    )

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'gender',
        'is_deleted'
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    ordering = ('id',)


class BaseUserActionAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'action',
        'created_at'
    )
    list_display = (
        'user',
        'action',
        'created_at'
    )
    readonly_fields = ('created_at',)
    raw_id_fields = ('user',)


@admin.register(UserAction)
class UserActionAdmin(BaseUserActionAdmin):
    pass


@admin.register(ArchivedUserAction)
class ArchivedUserActionAdmin(BaseUserActionAdmin):
    pass
