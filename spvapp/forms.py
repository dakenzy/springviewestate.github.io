from django import forms
from . models import Residents, Occupants, Staff


class ResidentsForm(forms.ModelForm):

    class Meta:
        model = Residents
        fields = '__all__'
        labels = {
            'firstname': 'First Name',
            'id_number': 'ID. Number',
            'mobile_number': 'Mobile Number',
            'hse_number': 'Hse. Number'
        }

    def __init__(self, *args, **kwargs):
        super(ResidentsForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['hse_number'].empty_label = "Select"


class OccupantsForm(forms.ModelForm):

    class Meta:
        model = Occupants
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'hse_number': 'Hse. Number'
        }

    def __init__(self, *args, **kwargs):
        super(OccupantsForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['hse_number'].empty_label = "Select"


class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = '__all__'
        labels = {
            'firstname': 'First Name',
            'id_number': 'ID. Number',
            'mobile_number': 'Mobile Number'
        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['position'].empty_label = "Select"
