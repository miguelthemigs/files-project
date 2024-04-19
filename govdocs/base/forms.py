from django import forms
from .models import InputLog, Document, User  # Ajuste os imports conforme necessário

class InputLogForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(InputLogForm, self).__init__(*args, **kwargs)
        # Check conditions and set label accordingly
        if True:
            self.fields['input_content'].label = ''

    class Meta:
        model = InputLog
        fields = '__all__' 
        exclude = ['input_id', 'user', 'doc_id', 'input_type','input_score']

class TagForm(forms.Form):
    tag = forms.CharField(max_length=100)