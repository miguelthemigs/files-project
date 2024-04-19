from django import forms
from .models import InputLog, Document, User  # Ajuste os imports conforme necessário

class InputLogForm(forms.ModelForm):
    class Meta:
        model = InputLog
        fields = ['doc_id', 'user_id', 'input_type', 'input_content']
        widgets = {
            'doc_id': forms.HiddenInput(),
            'user_id': forms.HiddenInput(),
            'input_type': forms.HiddenInput(),
        }
