from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import *


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


# def create_project(request):
#   if request.method == 'POST':
#         form = NewProjectForm(request.POST)
#         if form.is_valid():
#             # create a new `Band` and save it to the db
#             band = form.save()
#             # redirect to the detail page of the band we just created
#             # we can provide the url pattern arguments as arguments to redirect function
#             return redirect('http://127.0.0.1:8000/project/add/', band.id)
#   else:
#     form = NewProjectForm
#     return render( request, 'portfolio_app/create_form.html',{'form': form})
    
def add_project(request):
    form = ProjectForm
    if request.method == 'POST':
        #print('Printing POST: ',request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'portfolio_app/create_form.html',context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)

    form = ProjectForm(instance=project)
    if request.method == 'POST':
        #print('Printing POST: ',request.POST)
      form = ProjectForm(request.POST,instance=project)
      if form.is_valid():
         form.save()
         return redirect('/')
    context = {'form':form}
    return render(request, 'portfolio_app/create_form.html',context)

def delete_project(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')
    context = {'item':project}
    return render(request, 'portfolio_app/delete_project.html',context)

def view_portfolio(request):
    #portfolio = Portfolio.objects.get(id=pk)

    #context = {'item':portfolio}
    return render(request, 'portfolio_app/view_portfolio.html')

def update_Portfolio(request,pk):
    portfolio=Portfolio.objects.get(id=pk)
    form = PortfolioForm(instance=portfolio)
    if request.method == 'POST':
        #print('Printing POST: ',request.POST)
      form = PortfolioForm(request.POST,instance=portfolio)
      if form.is_valid():
         form.save()
         return redirect('/')
    context = {'form':form}
    return render(request, 'portfolio_app/create_form.html',context)

    