from django.http import Http404
from django.views.generic.edit import FormView

from .forms import ParticipantForm
from .models import Participant


class ContestView(FormView):
    form_class = ParticipantForm
    template_name = 'contest/contest.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

