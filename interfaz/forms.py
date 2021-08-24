from interfaz.models import ingredientes
from django.forms import ModelForm, fields, widgets

class IngredientesForm(ModelForm):
    class Meta:
        model = ingredientes
        fields = '__all__'