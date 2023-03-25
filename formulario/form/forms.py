from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field
from .models import Forms

class DateInput(forms.DateInput):
    input_type = "date"
class formularioView(forms.ModelForm):
    class Meta:
        model = Forms
        
        fields = '__all__'
        widgets = {
            'nascimento': DateInput()
        }
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        #ADICIONANDO CLASS PARA ESTILIZAR:
        self.helper.label_class = 'col-sm-6'
        #ADICIONANDO BOTÃO ENVIAR:
        self.helper.add_input(Submit('btn btn-primary', 'Enviar'))
        #ADICIONANDO CLASS PARA ESTILIZAR:
        self.helper.label_class = 'col-form-label'
        #TIRANDO O FIELD REQUIRED
        self.fields['curso'].required = False
        self.fields['instituicao'].required = False
        self.fields['celular'].required = False
        self.fields['instagram'].required = False

        