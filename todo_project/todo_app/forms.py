from django import forms
from.models import task_table
class task_form(forms.ModelForm):
    class Meta:
        model=task_table
        fields=['t_name','priority','date']