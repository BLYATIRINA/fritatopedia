from django.shortcuts import render

# Create your views here.
def index(request):
    dic = {
        'title': 'BAMBAM',
        'values': ['penis', 'zalupa',
                   'kawasaki', 'cago'
                   'krico', 'estriper']
           }
    return render(request, 'main/index.html', dic)

