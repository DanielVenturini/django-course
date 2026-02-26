from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

def time_viewer(request: HttpRequest) -> HttpResponse:
    if not request.headers.get('Bypass') or not request.headers.get('Bypass') == request.path:
        httpResponse = HttpResponse('Error!')
        httpResponse.status_code = 403
        return httpResponse

    from datetime import datetime

    now = datetime.now().isoformat()
    return HttpResponse(now, headers={'Bypass': 'True'})


def disk_usage_viewer(request: HttpRequest) -> HttpResponse:

    import subprocess

    context = {
        'command': 'df -h',
        'output': subprocess.getoutput('df -h').split('\n')
    }

    return HttpResponseRedirect('/server/run/df?args=-h')

def run_command_viewer(request: HttpRequest, command: str) -> HttpResponse:
    import subprocess

    context = {
        'command': command,
        'output': subprocess.getoutput(command + ' ' + request.GET.get('args')).split('\n')
    }

    return render(request, 'default-response.html', {'context': context})