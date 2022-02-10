from django.shortcuts import render

def index(req):

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
            # raw = f"select * from News n inner join N_content nc on n.n_id = nc.n_id where n_input != '9999-12-31 00:00:00' and nd_img is not null and nd_img !='None' order by n_input desc limit 4"
            # NC = N_content.objects.raw(raw)
            raw = f"select * from login where id = '{username}'"
            # us = login.objects.get(username=raw[0].id)
            print (raw)

            # if check_password(password, us.password):
            #     pass
            # else:
            #     res_data['error'] = '비밀번호가 틀렸습니다.'

        return render(req, 'login.html', res_data)

# Create your views here.
