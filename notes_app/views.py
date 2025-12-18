from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Note, Category, Status
from .forms import NoteForm

def notes_list(request):
    notes = Note.objects.select_related("author", "status", "category").all()
    statuses = Status.objects.all()
    categories = Category.objects.all()
    # Пример фильтрации, если у тебя есть query params
    return render(request, "notes_list.html", {
        "notes": notes,
        "statuses": statuses,
        "categories": categories,
    })

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "note_detail.html", {"note": note})

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user   # автоматически
            note.save()
            return redirect("notes_list")
    else:
        form = NoteForm()
    return render(request, "note_form.html", {"form": form})

@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.author and not request.user.is_staff:
        raise PermissionDenied("Доступ запрещен")
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, "note_form.html", {"form": form, "note": note})

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.author and not request.user.is_staff:
        raise PermissionDenied("Доступ запрещен")
    if request.method == "POST":
        note.delete()
        return redirect("notes_list")
    return render(request, "note_confirm_delete.html", {"note": note})

@login_required
def my_notes(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, "notes_list.html", {
        "notes": notes,
    })
