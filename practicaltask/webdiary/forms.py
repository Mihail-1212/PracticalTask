from django.utils.translation import gettext_lazy as _
from django import forms

from . import models

class TaskEditForm(forms.ModelForm):
    """
    Form for edit and create views
    """

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Task
        fields = ['name', 'text', 'date_start']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'require': False
            }),
            'date_start': forms.DateTimeInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'id': 'datepicker-start',
                     'autocomplete': 'off',
                     'input_formats': ['%H:%M %m/%d/%Y'],
            }),
        }
