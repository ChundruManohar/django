from django.shortcuts import render

# Create your views here.
def student(request):
    Student_information = {
        'name':'tarun',
        'age': 25,
        'job': 'python developer',
    }
    
    
    return render(request,'a.html',context=Student_information)
