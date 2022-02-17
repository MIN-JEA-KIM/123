from telnetlib import AUTHENTICATION
from unittest import result
from django.shortcuts import render, redirect
from datetime import date, datetime, timedelta
from django.http import HttpResponse, JsonResponse 
from email.policy import default
from itertools import product
from multiprocessing import context
from re import template
from urllib import request, response
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.contrib import auth
import logging
from datetime import datetime
from django.views.decorators.http import require_POST
import json

# -2022.01.24 park_jong_won
logger = logging.getLogger('news')

# -2022.02.07 park_jong_won add {def scrollLog, import datetime} del {def log}
def scrollLog(req):

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')


    if req.method == 'POST':
        if 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")

            new_scroll_data = ScrollData(ipaddr=ip, acstime=datetime.now(), url=req.get_full_path(), staytime=req.POST['deltaTime'], scroll=req.POST['scroll'])
            new_scroll_data.save()
            print("save scroll_data")
        else:
            pass
    else:

        new_log = Log(ipaddr=ip, acstime=datetime.now(), url=req.get_full_path())
        new_log.save()
        print("save log_data")

    print(f"HTTP_X_FORWARDED_FOR = {req.META.get('HTTP_X_FORWARDED_FOR')}, REMOTE_ADDR = {req.META.get('REMOTE_ADDR')}, HTTP_X_REAL_IP = {req.META.get('HTTP_X_REAL_IP')}")


def author(req):
    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    context = {
        # "post_latest": post_latest
    }

    return render(req, "author.html", context=context)


def politics(req): # 정치
    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select * 
        from News n 
        inner join N_category_detail ncd on n.cd_id = ncd.cd_id 
        inner join N_summarization_one nso on n.n_id = nso.n_id
        where ncd.c_id = 100
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['page_obj'] = page_obj
    data['news_list'] = news_list

    return render(req, "politics.html", data)


def economy(req): # 경제
    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select * 
        from News n 
        inner join N_category_detail ncd on n.cd_id = ncd.cd_id 
        inner join N_summarization_one nso on n.n_id = nso.n_id
        where ncd.c_id = 101
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['page_obj'] = page_obj
    data['news_list'] = news_list

    return render(req, "economy.html", data)


def society(req): # 사회
    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select * 
        from News n 
        inner join N_category_detail ncd on n.cd_id = ncd.cd_id 
        inner join N_summarization_one nso on n.n_id = nso.n_id
        where ncd.c_id = 102
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['page_obj'] = page_obj
    data['news_list'] = news_list

    return render(req, "society.html", data)


def life(req): # 생활문화
    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select * 
        from News n 
        inner join N_category_detail ncd on n.cd_id = ncd.cd_id 
        inner join N_summarization_one nso on n.n_id = nso.n_id
        where ncd.c_id = 103
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['page_obj'] = page_obj
    data['news_list'] = news_list

    return render(req, "life.html", data)


def IT(req): # IT/과학
    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select * 
        from News n 
        inner join N_category_detail ncd on n.cd_id = ncd.cd_id 
        inner join N_summarization_one nso on n.n_id = nso.n_id
        where ncd.c_id = 104
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['page_obj'] = page_obj
    data['news_list'] = news_list

    return render(req, "IT.html", data)


def world(req): # 세계
    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select * 
        from News n 
        inner join N_category_detail ncd on n.cd_id = ncd.cd_id 
        inner join N_summarization_one nso on n.n_id = nso.n_id
        where ncd.c_id = 105
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['page_obj'] = page_obj
    data['news_list'] = news_list

    return render(req, "world.html", data)

# #Ip 가져오기
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

def news_post(req, n_id, pk):

    data = {}
    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        if 'id' in req.POST.keys() :
	    
            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select n.n_id, n.n_title, n.nd_img, nc.n_content, n.o_link, ns_content
        from News n 
        inner join N_content nc on n.n_id = nc.n_id 
        inner join N_summarization ns on n.n_id = ns.n_id
        where n.n_id ={n_id} 
    """
    news = News.objects.raw(query)[0]  # models.py Board 클래스의 모든 객체를 board_list에 담음
    data['news'] = news

    # news summarization, news content 줄 바꿈 처리
    print(news.ns_content)
    print("============")
    print(news.n_content)

    
    login_session = req.session.get('login_session')
    
    article = get_object_or_404(N_content, id=pk)
    data['article'] = article

    # if req.session.get('login_session') is None:
    #     cookie_name = 'news_post'
    # else:
    #     cookie_name = f'news_post:{req.session["login_session"]["id"]}'
    
    if Memberinfo.user.id == login_session:
        data['user'] = True
    else:
        data['user'] = False

    response = render(req, "news_post.html", data)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    #expire_date = expire_date.replace(hour=23, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = 60*60*24*30 

    cookie_value = req.COOKIES.get('news_post', '_')

    if f'_{pk}_' not in cookie_value:
        cookie_value += f'{pk}_'
        response.set_cookie('news_post', value=cookie_value, max_age=max_age, httponly=True)
        article.hits += 1
        article.save()

    return response

def recommend(request):
    pk = request.POST.get('pk', None)
    n_rec = get_object_or_404(N_content, pk=pk)
    user = request.user

    if n_rec.recommend.filter(id=user.id).exists():
        n_rec.recommend.remove(user)
        message = '추천 취소'
    else:
        n_rec.recommend.add(user)
        message = '추천'

    context = {'recommend_count':n_rec.count_recommend_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

def index(req):
    data = {}

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')
    
    if req.method == 'POST':
        if 'id' in req.POST.keys() :

            data['login_massage'] = login(req)
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")

    else : # GET
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")
        
    raw = f"select * from News n inner join N_content nc on n.n_id = nc.n_id where n_input != '9999-12-31 00:00:00' and nd_img is not null and nd_img !='None' order by n_input desc limit 4"
    NC = N_content.objects.raw(raw)

    query = []
    news_list = []
    j = 0
    for i in range(100, 106):
        query.append(want_category(i))
        raw_db = News.objects.raw(query[j])
        news_list.append(raw_db)
        exec(f"data['news_list{i}'] = raw_db")
        exec(f"page{i} = req.GET.get('page', '1')")
        exec(f"paginator{i} = Paginator(news_list[{j}], '10')")
        exec(f"page_obj{i} = paginator{i}.page(page{i})")
        exec(f"data['page_obj{i}'] = page_obj{i}")
        j += 1

    data['banners'] = NC
    return render(req, "index.html", data)



def want_category(c_id):
    
    query = f"""
        select n.n_id, p_id, n.cd_id, n_title, nd_img, n_input, o_link, nso_id, nso_content, c_id 
        from News n 
        inner join N_summarization_one nso on n.n_id = nso.n_id 
        inner join N_category_detail det on n.cd_id = det.cd_id
        where c_id = {c_id} and n_input != '9999-12-31 00:00:00'
        order by n_input desc"""
    return query




def memberinfo(req):
    # memberinfo 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if req.method == 'POST':
        # password 와 password1에 입력된 값이 같다면
        if req.POST['password'] == req.POST['password1'] :
            
            query = f"select id, email from memberinfo where id = '{req.POST['id']}' or email = '{req.POST['email']}'"
            
            id_email = Memberinfo.objects.raw(query)
            try:
                if id_email != None:

                    f_id = id_email[0].id
                    f_email = id_email[0].email

                    if req.POST['id'] == f_id :

                        return render(req, 'memberinfo.html', {'error' : "같은 아이디가 있음"})

                    if req.POST['email'] == f_email:

                        return render(req, 'memberinfo.html', {'error' : "같은 이메일이 있음"})
            except:
                # 객체를 새로 생성
                user = Memberinfo(id=req.POST['id'], password=req.POST['password'], name=req.POST['name'], birth=req.POST['birth'], sex=req.POST['sex'], email=req.POST['email'], phone=req.POST['phone'])
                # DB 저장
                user.save()

                return render(req, 'memberinfo.html', {'save' : "가입완료"})
        else:   
            
            return render(req, 'memberinfo.html', {'error' : "비밀번호 다름"})
    else:

        return render(req, 'memberinfo.html')


def login(req): # 로그인
    if req.method == 'POST':
        u_id = req.POST['id']
        u_password = req.POST['password']

        query = f"select id, password from memberinfo where id = '{u_id}'"
        user = Memberinfo.objects.raw(query)
            
        try:
            f_password = user[0].password

            if u_password == f_password:
                return "환영합니다."
            else:
                return "비밀번호를 잘못 입력하셨습니다."
        except:
                return "없는 ID 입니다."