from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse

def time_viewer(request: HttpRequest) -> HttpResponse:
    if not request.headers.get('Bypass') or not request.headers.get('Bypass') == request.path:
        return HttpResponse('Error!', status=403)

    from datetime import datetime

    now = datetime.now().isoformat()
    return HttpResponse(now, headers={'Bypass': 'True'})


def disk_usage_viewer(request: HttpRequest) -> HttpResponseRedirect:

    import subprocess

    context = {
        'command': 'df -h',
        'output': subprocess.getoutput('df -h').split('\n')
    }

    redirect_url = f"{reverse('generic-command', args=['df'])}?args=-h"
    return redirect(redirect_url, 'df/?args=-h', permanent=False)


def run_command_viewer(request: HttpRequest, command: str) -> HttpResponse:
    import subprocess

    command += '' if not request.GET.get('args') else ' ' + request.GET.get('args')

    context = {
        'command': command,
        'output': subprocess.getoutput(command).split('\n')
    }

    return render(request, 'default-response.html', {'context': context})

def update_root_password(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'submit.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(f'request with name {name} and password {password}')
        return HttpResponse('Done')