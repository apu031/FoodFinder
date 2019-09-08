from django.forms import ModelForm
from .models import DropDownModel

# Mind the name of your form!!

class DropDownModelForm(ModelForm):
   class Meta:
       model = DropDownModel
       fields = ['cities', 'food_categories']