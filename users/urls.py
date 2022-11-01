from django.urls import path

from users.views import CreateUserView

urlpatterns = [
    path('create-user', CreateUserView.as_view(), name='create_user'),
]
