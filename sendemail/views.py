from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core import mail
from logging import getLogger

logger = getLogger(__name__)


# Create your views here.
def send_email(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'sendmail.html')
    elif request.method == 'POST':
        # Send message.
        ans = mail.send_mail(
            'Subject here11111',
            'Here is the message.1111',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        logger.info(f'邮件发送成功：{ans}')
        return HttpResponse('请查看终端是否有邮件发送成功的提示信息。')
