from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from classroom.models import Student, Subject, Domaine, User, Universite

# Email Adress

class Subscribe(forms.Form):
    Email = forms.EmailField()
    
    def __str__(self):
        return self.Email




















# Subject
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'




class DomaineForm(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = '__all__'



#StudentSignUpForm

class StudentSignUpForm(UserCreationForm):
    email= forms.EmailField()

    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    domaine = forms.ModelMultipleChoiceField(
        queryset=Domaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
      
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        student.domaine.add(*self.cleaned_data.get('domaine'))
        student.adresse_email =user.email
       
        return user


class ProfileUpdateForm(forms.ModelForm):
    composante = forms.ModelMultipleChoiceField(
        queryset= Universite.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='University', )
    
    fonction = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='function', )

    CHOICES = (('Mrs', 'Mrs',), ('Mr', 'Mr',))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label=' ')

    class Meta:

          model = Student
          fields = ['choice_field','prenom','name', 'adresse_email','numero_telephone','composante', 'fonction', 'autre', 'domaine', 'name_adre', 'adresse_email_adre']     

