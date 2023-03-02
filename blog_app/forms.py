from django.forms import ModelForm, EmailInput
import blog_app.models as m
from django.utils.translation import gettext_lazy as _


class Subscribe(ModelForm):
    class Meta:
        model = m.Subscribe
        fields = "__all__"
        labels = {"email": _("")}
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Enter Your Email'}),
        }

