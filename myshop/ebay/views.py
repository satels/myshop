from django.http import HttpResponse
from djsms.core import send_message


def complete(request):
    data = send_message('+79687298907', 'Hello, Ivan!', fail_silently=True)
    return HttpResponse(str(data))
