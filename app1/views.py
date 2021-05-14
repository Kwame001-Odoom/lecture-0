from django.shortcuts import render
from django.http import HttpResponse, Http404,JsonResponse
from .forms import *
import datetime, re
# Create your views here.


def main(request):
    now = datetime.datetime.utcnow()
    #day = datetime.datetime.date()
    return HttpResponse(f"Hello World, the current time is {now}")


def about(request):
    return HttpResponse('About Us | SAJAT.')


def page(request):
    context = {
        'msgs': ['We are here', 'We are getting started','We are live']
    }
    return render(request, 'index.html',context)


def form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            note = request.POST['note']
            email = request.POST['email']
            dict = {
                'form': FeedbackForm()
            }

            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag= True
                errormsg= 'Title Should Be In Capital!'
                Errors.append(errormsg)

            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = 'Not a Valid Email!'
                Errors.append(errormsg)

                #return render(request, 'form2.html', dict)

            if errorflag != True:
                dict['success'] = True
                dict['successmsg'] = 'Form Submitted'
                '''print(title)
                print(note)
                #var = str('Form Submitted by ' + str(request.method))
                #return HttpResponse(var)
                return HttpResponse(f'Form submitted by {request.method}.')'''
            dict['error'] = errorflag
            dict['errors'] = Errors
            return render(request, 'form2.html', dict)

        else:
            context = {
                'form': form
            }
            return render(request, 'form2.html', context)

    elif request.method == 'GET':
        form = FeedbackForm()
        context = {
            'form': form
        }
    return render(request, 'form2.html',context)


def error_404(request, exception):
    return render(request, '404.html')
