from django import forms
from django.contrib.auth.models import User
import re
from django.core.exceptions import ObjectDoesNotExist

class Addimg(forms.Form):
	img = forms.ImageField()