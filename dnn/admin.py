from django.contrib import admin

# Register your models here.
from django import forms
from dnn.models import NNModel


class NNForm(forms.ModelForm):
    class Meta:
        model = NNModel
        exclude = ["nn"]


class NNAdmin(admin.ModelAdmin):
    list_display = ["coords", "nn"]
    form = NNForm


admin.site.register(NNModel, NNAdmin)
