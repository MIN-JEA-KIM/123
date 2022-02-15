#추천
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.decorators.http import require_POST
from django.http import JsonResponse
#######################################################
from datetime import date, datetime, timedelta
from django.http import HttpResponse 
from email.policy import default
from itertools import product
from multiprocessing import context
from re import template
from urllib import request, response
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from datetime import datetime
import logging

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
        new_scroll_data = ScrollData(ipaddr=req.META.get('REMOTE_ADDR'), acstime=datetime.now(), url=req.get_full_path(), staytime=req.POST['deltaTime'], scroll=req.POST['scroll'])
        new_scroll_data.save()
    else:
        new_log = Log(ipaddr=req.META.get('REMOTE_ADDR'), acstime=datetime.now(), url=req.get_full_path())
        new_log.save()

    print(f"HTTP_X_FORWARDED_FOR = {req.META.get('HTTP_X_FORWARDED_FOR')}, REMOTE_ADDR = {req.META.get('REMOTE_ADDR')}, HTTP_X_REAL_IP = {req.META.get('HTTP_X_REAL_IP')}")
    return context

def author(req):

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

    context = {
    }

    return render(req, "author.html", context)


def politics(req): # 정치

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

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

    context = {'page_obj': page_obj, 'news_list': news_list}

    return render(req, "politics.html", context)


def economy(req): # 경제

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

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

    return render(req, "economy.html", {'page_obj': page_obj, 'news_list': news_list})


def society(req): # 사회

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

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

    return render(req, "society.html", {'page_obj': page_obj, 'news_list': news_list})


def life(req): # 생활문화

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

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

    return render(req, "life.html", {'page_obj': page_obj, 'news_list': news_list})


def IT(req): # IT/과학

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

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

    return render(req, "IT.html", {'page_obj': page_obj, 'news_list': news_list})


def world(req): # 세계

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

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

    return render(req, "world.html", {'page_obj': page_obj, 'news_list': news_list})


def travel(req):

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

    context = {

    }

    return render(req, "travel.html", context=context)

# #Ip 가져오기
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[-1].strip()
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

def news_post(req, n_id):

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

    query = f"""
        select n.n_id, n.n_title, n.nd_img, nc.n_content, n.o_link, ns_content
        from News n 
        inner join N_content nc on n.n_id = nc.n_id 
        inner join N_summarization ns on n.n_id = ns.n_id
        where n.n_id ={n_id} 
    """
    news = News.objects.raw(query)[0]

    article = get_object_or_404(N_content, pk=n_id) 
    
    context = {
        'news': news,
        'article': article
    }

    response = render(req, 'news_post.html', context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    #expire_date = expire_date.replace(hour=23, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = 60*60*24*30 

    cookie_value = req.COOKIES.get('news_post', '_')

    if f'_{n_id}_' not in cookie_value:
        cookie_value += f'{n_id}_'
        response.set_cookie('news_post', value=cookie_value, max_age=max_age, httponly=True)
        article.hits += 1
        article.save()

    return response
    #return render(req, "news_post.html", {'news': news, 'view': view})
    

@require_POST
def recommend(req):
    if req.method == 'POST':
        ip = request.ip # ip를 가져온다.
        n_id = request.POST.get('pk', None)
        r_count = N_content.objects.get(pk = n_id)

        if r_count.recommend.filter(id = ip.id).exists(): #이미 해당 유저가 likes컬럼에 존재하면
            r_count.recommend.remove(ip) #likes 컬럼에서 해당 유저를 지운다.
            message = 'ip o'
        else:
            r_count.recommend.add(ip)
            message = 'recommned'

    context = {'recommend.count' : r_count.total_recommend, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')
    # dic 형식을 json 형식으로 바꾸어 전달한다.
     
def index(req):

    scrollLog(req)

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {ip}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]")

    raw = f"select * from News n inner join N_content nc on n.n_id = nc.n_id where n_input != '9999-12-31 00:00:00' and nd_img is not null and nd_img !='None' order by n_input desc limit 4"
    NC = N_content.objects.raw(raw)

    query100 = want_category(100)
    news_list100 = News.objects.raw(query100) #models.py Board 클래스의 모든 객체를 board_list에 담음
    query101 = want_category(101)
    news_list101 = News.objects.raw(query101)
    query102 = want_category(102)
    news_list102 = News.objects.raw(query102)
    query103 = want_category(103)
    news_list103 = News.objects.raw(query103)
    query104 = want_category(104)
    news_list104 = News.objects.raw(query104)
    query105 = want_category(105)
    news_list105 = News.objects.raw(query105)

    # news_list100 페이징 처리
    page100 = req.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator100 = Paginator(news_list100, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj100 = paginator100.page(page100) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    page101 = req.GET.get('page', '1')
    paginator101 = Paginator(news_list101, '10')
    page_obj101 = paginator101.page(page101)

    page102 = req.GET.get('page', '1')
    paginator102 = Paginator(news_list102, '10')
    page_obj102 = paginator102.page(page102)

    page103 = req.GET.get('page', '1')
    paginator103 = Paginator(news_list103, '10')
    page_obj103 = paginator103.page(page103)

    page104 = req.GET.get('page', '1')
    paginator104 = Paginator(news_list104, '10')
    page_obj104 = paginator104.page(page104)

    page105 = req.GET.get('page', '1')
    paginator105 = Paginator(news_list105, '10')
    page_obj105 = paginator105.page(page105)

    context = {
        'banners': NC, 
        'page_obj100':page_obj100, 'news_list100':news_list100, 
        'page_obj101':page_obj101, 'news_list101':news_list101, 
        'page_obj102':page_obj102, 'news_list102':news_list102, 
        'page_obj103':page_obj103, 'news_list103':news_list103, 
        'page_obj104':page_obj104, 'news_list104':news_list104, 
        'page_obj105':page_obj105, 'news_list105':news_list105
    }
    return render(req, "index.html", context)


def want_category(c_id):
    
    query = f"""
        select n.n_id, p_id, n.cd_id, n_title, nd_img, n_input, o_link, nso_id, nso_content, c_id 
        from News n 
        inner join N_summarization_one nso on n.n_id = nso.n_id 
        inner join N_category_detail det on n.cd_id = det.cd_id
        where c_id = {c_id} and n_input != '9999-12-31 00:00:00'
        order by n_input desc"""
    return query
