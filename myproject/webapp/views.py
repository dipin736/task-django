from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .models import Submission
from django import forms

# Define a form class for submissions
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['name', 'email']

def home(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'webapp/index.html', {'current_time': current_time})

def submit_form(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the data to the database
            return HttpResponseRedirect(reverse('submissions'))  # Redirect to submissions page
    else:
        form = SubmissionForm()  # Create an empty form for GET request
    return render(request, 'webapp/submit.html', {'form': form})

def submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'webapp/submissions.html', {'submissions': submissions})
