from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def time_viewer(request: HttpRequest) -> HttpResponse:
    if not request.headers.get('Bypass') or not request.headers.get('Bypass') == request.path:
        httpResponse = HttpResponse('Error!')
        httpResponse.status_code = 403
        return httpResponse

    from datetime import datetime

    now = datetime.now().isoformat()
    return HttpResponse(now, headers={'Bypass': 'True'})


def disk_usage_viewer(request: HttpRequest) -> HttpResponse:
    # if not request.headers.get('Bypass') or not request.headers.get('Bypass') == request.path:
    #     httpResponse = HttpResponse('Error!')
    #     httpResponse.status_code = 403
    #     return httpResponse

    import subprocess

    context = {
        'command': 'df -h',
        'output': subprocess.getoutput('df -h').split('\n')
    }

    return render(request, 'default-response.html', {'context': context})

#     return HttpResponse(
#         output,
#         headers={
#             'Bypass': 'True',
#             'Content-Type': 'text/html',
#         }
#     )


# def disk_usage_template_viewer(request: HttpRequest) -> HttpResponse: