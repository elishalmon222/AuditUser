from rest_framework.routers import DefaultRouter

from users.views import UserView, UserActionView

router = DefaultRouter()

router.register('users', UserView, basename='users')
router.register('user_actions', UserActionView, basename='user_actions')

urlpatterns = router.urls
