from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django import forms
from ..decorators import student_required
from ..forms import StudentSignUpForm,DomaineForm, SubjectForm, Subscribe
from ..models import Student, Subject, Domaine, User
from ..forms import ProfileUpdateForm
from django.db.models import Q
from itertools import chain
from django.shortcuts import render
from django_school.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
    # Create your views here.
    #DataFlair #Send Email
def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})




















class FlyerView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'flyer.html'






class profile(CreateView):
    model = Student
    form_class = ProfileUpdateForm
    template_name = 'inscription.html'
    

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        messages.success(self.request, 'The projet was created with success!' )
        return redirect('confirmation', quiz.pk)









#Subject et mots Clés 

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'classroom/informations/subject_add_form.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        return redirect('subject_add')




class StudentListView(ListView):
    template_name = 'confirmation.html'
    def get_queryset(self):
        self.quiz = get_object_or_404(Student, pk=self.kwargs['pk'])
        return Student.objects.filter(pk = self.quiz.pk)








#Nom de Domaines 
class DomaineCreateView(CreateView):
    model = Domaine
    form_class = DomaineForm
    template_name = 'classroom/informations/domaine_add_form.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        return redirect('domaine_add')



#StudentSignUp

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        
        login(self.request, user)
        return redirect('students:profile')



class PotentielleListView(ListView):
    model = Student
    ordering = ('created_at', )
    context_object_name = 'quizzes'
    template_name = 'students.html'

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset
