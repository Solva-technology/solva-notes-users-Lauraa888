from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Встроенные auth маршруты (login/logout/password reset)
    path("auth/", include("django.contrib.auth.urls")),

    # Регистрация пользователя
    path(
    "auth/",
    include(("users_app.urls", "users_app"), namespace="users_app"),
),

    # Основные заметки
    path("", include("notes_app.urls")),
]