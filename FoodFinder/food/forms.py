from django.forms import ModelForm, forms
from .models import DropDownModel, ParsedData


# Mind the name of your form!!

class DropDownModelForm(ModelForm):
    class Meta:
        model = DropDownModel
        fields = ['cities']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ch = [(query['city'], query['city']) for query in ParsedData.objects.order_by('city').values('city').distinct()]
        self.fields['cities'].choices = ch
