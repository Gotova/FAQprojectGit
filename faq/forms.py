from django import forms
from .models import *


class HotelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'hotel_Main_Img']
