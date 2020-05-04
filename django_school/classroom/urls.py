from django.urls import include, path

from .views import classroom, students

urlpatterns = [
    path('', students.FlyerView.as_view(), name='home'),
    path('application/', students.profile.as_view(), name='application'),
    path('confirmation/<int:pk>/', students.StudentListView.as_view(), name='confirmation'),
    path('resultats/', students.PotentielleListView.as_view(), name='registration'),
    path('subscribe/', students.subscribe, name = 'subscribe'),
]
