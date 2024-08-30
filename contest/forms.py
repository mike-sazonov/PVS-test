from django import forms
from contest.models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        labels = {
            'name': 'Name',
            'email': 'Email',
            'code': 'Code',
        }