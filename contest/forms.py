from django import forms
from contest.models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'