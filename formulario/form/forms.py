from django import forms
from crispy_forms.helper import FormHelper
from .models import Forms

class formularioView(forms.ModelForm):
    
    class Meta:
        model = Forms
        fields = ('nome','nascimento', 'curso', 'instituicao', 'email', 'celular', 'instagram')
        render_required_fields = False
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class = 'col-sm-6'
        