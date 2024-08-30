from pyexpat.errors import messages

from django.http import Http404
from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import ParticipantForm
from .models import Participant


class ContestView(FormView):
    form_class = ParticipantForm
    template_name = 'contest/contest.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Спасибо за участие!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Participant.objects.all()
        return context