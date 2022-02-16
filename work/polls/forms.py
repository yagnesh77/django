from django.forms import ModelForm
from .models import Question

class ContactForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']