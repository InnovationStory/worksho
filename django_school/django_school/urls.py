from django.urls import include, path
from django.contrib import admin

from classroom.views import classroom, students, teachers

import notifications.urls

urlpatterns = [
    path('', include('classroom.urls')),
     path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),

]
