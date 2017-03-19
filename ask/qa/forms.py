from django import forms
from django.db import models
from .models import Question, Answer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AskForm(forms.ModelForm):


    class Meta:
        model = Question
        fields = ('title', 'text')





class AnswerForm(forms.ModelForm):


    class Meta:
        model = Answer
        fields = ('text', 'question')
