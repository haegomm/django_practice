from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    context = {
        'name': '가은이',
        'foods' : ['pizza', 'banana', 'milktea'],
    }
    return render(request, 'greeting.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    department = request.GET.get('department')
    name = request.GET.get('name')

    if department == '대전 2반':
        if name == '이가은':
            message = '포도당서리꾼 이시군요!'
        else:
            message = '교육생 이시군요!'
    else:
        message = '다른 반 이시군요!'

    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def show(request, name):
    context = {
        'name': name
    }
    return render(request, 'show.html', context)