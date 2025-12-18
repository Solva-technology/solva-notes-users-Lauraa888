from django.urls import path, include
from .views import (
    notes_list,
    note_detail,
    note_create,
    note_edit,
    note_delete,
    my_notes, 
)

urlpatterns = [
    # Главная страница со списком заметок
    path("", notes_list, name="notes_list"),

    # Заметки (детальная)
    path("notes/<int:note_id>/", note_detail, name="note_detail"),

    path("my/", my_notes, name="my_notes"),

    # --- CRUD ---
    path("notes/create/", note_create, name="note_create"),
    path("notes/<int:note_id>/edit/", note_edit, name="note_edit"),
    path("notes/<int:note_id>/delete/", note_delete, name="note_delete"),
    
  # Подключение аутентификации и регистрации из users_app
    path('auth/', include('users_app.urls')),  
]