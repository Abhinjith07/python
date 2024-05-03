from django import forms

from new_app.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields =("title","subject")