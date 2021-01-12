from django import forms
from pharmacy.models import Pharmacy
from pharmacy.models import Employee
from pharmacy.models import Tablet






class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = "__all__"

class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = ['tid','tname','tdate','tquantity','tprice']
