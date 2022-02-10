from django.shortcuts import render
from login.models import login

def login_page(req):

    if req.method == 'GET':
        return render(req, 'login.html')

    elif req.method == 'POST':
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        print(username, password)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'

        else:
            raw = f"select * from login where id = '{username}'"
            us = login.objects.raw(raw)

            if password == us:
                pass

            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'

        return render(req, 'login.html', res_data)

# Create your views here.
