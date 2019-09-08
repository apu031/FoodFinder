from django.forms import ModelForm
from .models import DropDownModel, ParsedData


# Mind the name of your form!!

class DropDownModelForm(ModelForm):
    class Meta:
        model = DropDownModel
        fields = ['cities', 'food_categories']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cities'].queryset = ParsedData.objects.values('city')
