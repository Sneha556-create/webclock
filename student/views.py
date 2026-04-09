from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def student_info(request):
    context = {
        'name': 'Snehapriya Roy',          # Replace with your name
        'register_number': 'RA2411027010068',   # Replace with your register number
        'department': 'Data Science and Business Systems',           # Replace with your department
        'university': 'SRMIST'         # Replace with your university
    }
    return render(request, 'student_info.html', context)
