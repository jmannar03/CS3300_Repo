from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic

# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
    studentActivePortfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_Active=True)
    print("Active portfolio query set:", studentActivePortfolios)
    return render(request, 'portfolio_app/index.html', {'studentActivePortfolios': studentActivePortfolios})
  # return render( request, 'portfolio_app/index.html')

class StudentListView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student


class ProjectListView(generic.DetailView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project