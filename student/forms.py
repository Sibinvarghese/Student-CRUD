from django import forms
from .models import Student
class StudentForms(forms.ModelForm):
    class Meta:
        model=Student
        fields=('fname','lname','phnumber','age','course')
        labels={
            'fname':'First Name',
            'lname':'Last Name',
            'phnumber':'Mobile Number',
            'age':'Age',
            'course':'Course'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForms,self).__init__(*args,**kwargs)
        self.fields["course"].empty_label="Select The Course"