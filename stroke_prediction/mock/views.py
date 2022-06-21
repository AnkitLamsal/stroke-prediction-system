from .utils_1 import random_forest_model
from django.shortcuts import render
from django.http import HttpResponse
from .models import Model
from .forms import model_form
# Create your views here.
def index(request):
    context = {}
    if request.method == "GET":
        form = model_form()
        context['form'] = form
    elif request.method == "POST":
        form = model_form(request.POST)
        context['form'] = form
        if(form.is_valid()):
            print(form.cleaned_data)
            # context['cleaned'] = form.cleaned_data
            forest = random_forest_model()
            forest.clean_form(form.cleaned_data)
            forest.preprocess()
            forest.display()
            prediction = forest.predict()
            context['prediction'] = statement(prediction[0])
    return render(request,'index.html',context)
    # elif request.method == "POST":
        
def statement(prediction):
    if(prediction == 0.0):
        return "The Person with above features did not have Stroke."
    elif(prediction == 1.0):
        return "The Person with above features had Stroke."