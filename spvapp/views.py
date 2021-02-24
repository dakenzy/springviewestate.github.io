from django.shortcuts import render
from . forms import ResidentsForm, OccupantsForm, StaffForm


# Create your views here.

# SpringView Estate Lists
def residents_list(request):
    return render(request, 'spvapp/residents_list.html')


def occupants_list(request):
    return render(request, 'spvapp/occupants_list.html')


def staff_list(request):
    return render(request, 'spvapp/staff_list.html')


# SpringView Estate Registration Forms
def residents_form(request):
    residents = ResidentsForm()
    return render(request, 'spvapp/residents_form.html', {'residents': residents})


def occupants_form(request):
    occupants = OccupantsForm()
    return render(request, 'spvapp/occupants_form.html', {'occupants': occupants})


def staff_form(request):
    staff = StaffForm()
    return render(request, 'spvapp/staff_form.html', {'staff': staff})


def spv_delete(request):
    return
