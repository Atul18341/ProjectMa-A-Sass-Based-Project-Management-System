from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import F

from .models import Semester,MCE_CSE_Faculties,MCE_Student_Records
Members = (("#","--------"),("1 Member","1 Member"),("2 Members","2 Members"),("3 Members","3 Members"),("4 Members","4 Members"))
class ProjectForm(forms.ModelForm):
    Group_Name=forms.ModelChoiceField(queryset=MCE_Student_Records.objects.all(), to_field_name="Group_Name")
    Mentor_Teacher = forms.ModelChoiceField(
        queryset=MCE_CSE_Faculties.objects.filter(project_count__lt=F('project_alloted')), to_field_name="faculty_name")

    class Meta:
        model=MCE_Student_Records
        fields=('Group_Name','Mentor_Teacher','Project_Name','Project_Abstract','Technologies_to_be_used')
        widgets = {
            'Group_Name': forms.TextInput(attrs={'placeholder': 'Group Name'}),
            'Group_Representative_Name': forms.TextInput(attrs={'placeholder': 'Group Representative Name'}),
            'Member1_Name': forms.TextInput(attrs={'placeholder': 'Member-1 Name'}),
            'Project_Name': forms.TextInput(attrs={'placeholder': 'Project Name'}),
            'Project_Abstract': forms.Textarea(
                attrs={'placeholder': 'Paste your Project Abstract Here', 'rows': 7, 'cols': 60}),
            'Technologies_to_be_used': forms.Textarea(
                attrs={'placeholder': 'Write Technologies you are planning to use', 'rows': 7, 'cols': 60})
        }

        labels = {
        'Group_Name':'',
        'Group_Representative_Name':'',
        'Project_Name':'',

        }
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("username","password")

class GroupDetailsForm(forms.ModelForm):
    Semester = forms.ModelChoiceField(queryset=Semester.objects.all(), to_field_name="semester")
    Group_Name = forms.CharField()
    Group_Type = forms.ChoiceField(choices=Members)
    Group_Representative_Name = forms.CharField()
    Group_Type = forms.ChoiceField(choices=Members)
    Member2_Name = forms.CharField(required=False, label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'Member-2 Name'}))
    Member2_Roll = forms.IntegerField(required=False, label='',
                                      widget=forms.NumberInput(attrs={'placeholder': 'Member-2 Roll'}))
    Member3_Name = forms.CharField(required=False, label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'Member-3 Name'}))
    Member3_Roll = forms.IntegerField(required=False, label='',
                                      widget=forms.NumberInput(attrs={'placeholder': 'Member-3 Roll'}))
    Member4_Name = forms.CharField(required=False, label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'Member-4 Name'}))
    Member4_Roll = forms.IntegerField(required=False, label='',
                                      widget=forms.NumberInput(attrs={'placeholder': 'Member-4 Roll'}))
    class Meta:
        model=MCE_Student_Records
        fields=('Semester','Group_Name','Group_Representative_Name','Group_Type','Member1_Name','Member1_Roll','Member2_Name','Member2_Roll','Member3_Name','Member3_Roll','Member4_Name','Member4_Roll')
        widgets = {
            'Group_Name': forms.TextInput(attrs={'placeholder': 'Group Name'}),
            'Group_Representative_Name': forms.TextInput(attrs={'placeholder': 'Group Representative Name'}),
            'Member1_Name': forms.TextInput(attrs={'placeholder': 'Member-1 Name'}),
            'Project_Name': forms.TextInput(attrs={'placeholder': 'Project Name'}),
        }

        labels = {
        'Group_Name':'',
        'Group_Representative_Name':'',
        'Member1_Name': '',

        }

class ProjectReportPPTForm(forms.ModelForm):
    Group_Name = forms.ModelChoiceField(queryset=MCE_Student_Records.objects.all(),to_field_name="Group_Name")
    class Meta:
        model=MCE_Student_Records
        fields=("Group_Name","Project_Report","Project_PPT")
