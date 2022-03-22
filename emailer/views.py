import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """
    View for index
    """
    return HttpResponse('<h3>Emailing api, use \'/api\' route</h3>')

# Note: csrf_exempt is used just to make sending POST requests easy
# it shouldn't be used in actual production code, as it is not safe
@csrf_exempt
def email_api(request):
    """
    Takes a GET/POST request and emails the user "welcome {username}" message.
     - Request body should "username" and "send_to_" field defined
    """
    try:
        data = json.loads(request.body)
        send_email(data["username"], data["send_to"])

        return HttpResponse('Success, mail sent!')
    except:
        return HttpResponse('Invalid request body')

def send_email(username, send_to):
    """
    Emails the welcome message template emails to "send_to".
    """
    # Email content
    subject = f"Welcome {username}!"
    message = f"Welcome {username}"
    html_message = render_to_string("welcome.html", context={
        "username": username.title()
    })

    send_mail(
        subject=subject,
        message=message,
        from_email="yashwantjodha1@gmail.com",
        recipient_list=[f"{send_to}"],
        html_message=html_message)