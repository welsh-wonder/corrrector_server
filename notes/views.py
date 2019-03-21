from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from django.contrib import messages
from . import models
from . import forms

User = get_user_model()

class CreateNote(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('title', 'content')
    model = models.Note

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteNote(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Note
    select_related = ('user')
    success_url = reverse_lazy('notes:all')

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Nota eliminada")
        return super().delete(*args, **kwargs)

class SingleNote(generic.DetailView):
    model = models.Note

    def get_queryset(self):
        return super().get_queryset()

    #def get_queryset(self):
     #   return super().get_queryset().filter(user__username__iexact=self.kwargs.get('username'))

class ListNotes(generic.ListView):
    model = models.Note
    template_name = 'authentication/home.html'
    
    '''def get_queryset(self):
        try:
            self.note_user = User.objects.prefetch_related('notes').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.note_user.notes.all()'''
    
    def get_queryset(self):
        self.note_user = user=self.request.user
        if self.request.user.is_authenticated:
            return models.Note.objects.filter(user=self.note_user)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["note_user"] = self.note_user
        return context
