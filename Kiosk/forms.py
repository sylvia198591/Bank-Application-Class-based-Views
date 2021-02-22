from django.forms import ModelForm
from Kiosk.models import *
from django  import forms
class DateInput(forms.DateInput):
    input_type = 'date'
class Accountcreateform(ModelForm):

    class Meta:
        # Accno = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
# ))
#         Name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
        model = Account
        fields = ["Name","Accno","Dfield",  "Amount", "Type" ]
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'Accno': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }


    # def __init__(self, *args, **kwargs):
    #     super(Accountcreateform, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['Name'].widget.attrs['readonly'] = True
    #
    # def clean_sku(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         return instance.Name
    #     else:
    #         return self.cleaned_data['Name']

    def clean(self):
        cleaned_data=super().clean() #mandatory
        Name=cleaned_data.get("Name")
        Accno = cleaned_data.get("Accno")
        Dfield = cleaned_data.get("Dfield")
        Amount = cleaned_data.get("Amount")

        Trans_type = cleaned_data.get("Type")


class Addtranstypeform(ModelForm):

    class Meta:
        model=Trans_type
        fields=['Trans_symbol','Type']
        def clean(self):
            cleaned_data = super().clean()
            Trans_symbol = cleaned_data.get("Trans_symbol")
            Trans_type = cleaned_data.get("Type")

class ViewAccountform(ModelForm):

    class Meta:
        model=Account
        fields=['Accno']
        def clean(self):
            cleaned_data = super().clean()
            Accno = cleaned_data.get("Accno")
            # Trans_type = cleaned_data.get("Type")
class Adddatewiseform(ModelForm):
    print("ddd")
    Startdate = forms.CharField(widget=DateInput)
    Enddate = forms.CharField(widget=DateInput)

    class Meta:
        model=Account
        fields=['Startdate','Enddate']
        widgets = {
            'Startdate': DateInput(),
            'Enddate': DateInput(),
        }
        def clean(self):
            cleaned_data = super().clean()
            print("d error")
            Accno = cleaned_data.get("Accno")
            Startdate = cleaned_data.get("Startdate")
            Enddate = cleaned_data.get("Enddate")
# class ItemForm(ModelForm):

class Addtransferform(ModelForm):
    # print("ddd")
    Accno = forms.IntegerField()
    Accnoto = forms.IntegerField()
    Amount = forms.IntegerField()


    class Meta:
        model=Account
        fields=['Accno','Accnoto','Amount']
        # widgets = {
        #     'Startdate': DateInput(),
        #     'Enddate': DateInput(),
        # }
        def clean(self):
            cleaned_data = super().clean()
            print("d error")
            Accno = cleaned_data.get("Accno")
            Accnoto = cleaned_data.get("Accnoto")
            Amount = cleaned_data.get("Amount")
            # Accno = cleaned_data.get("Accno")
            # Startdate = cleaned_data.get("Startdate")
            # Enddate = cleaned_data.get("Enddate")