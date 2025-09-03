from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406437331',
        'name': 'Keisha Vania Laurent',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
