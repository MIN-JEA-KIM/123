
from email.policy import default
from itertools import product
from multiprocessing import context
from re import template
from urllib import response
from django.http import JsonResponse
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
# class PostView(View):
#     def get(self,request,view_count):
#         if not N_content.objects.filter(id = view_count).exists():
#             return JsonResponse({'MESSAGE' : 'DOES_NOT_EXIST_POST'}, status = 404)

#         view = N_content.objects.get(id = view_count)

#         IPaddr = get_client_ip(request)

#         if not Log.objects.filter(access_ip= IPaddr).exists():
#             view.counting += 1 
#             view.save()
            
#             Log.objects.create(access_ip = IPaddr)

#         return JsonResponse({"view" : view}, status = 200)

def scrollLog(req):
    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')

    if req.method == 'POST':
        # form = req.POST
        # logger.info(f"POST log [IPaddr = {req.META.get('REMOTE_ADDR')}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
        new_scroll_data = ScrollData(ipaddr=ip, acstime=datetime.now(), url=req.get_full_path(), staytime=req.POST['deltaTime'], scroll=req.POST['scroll'])
        new_scroll_data.save()
        print("save scroll_data")
    else:
        # logger.info("GET log")
        new_log = Log(ipaddr=ip, acstime=datetime.now(), url=req.get_full_path())
        new_log.save()
        print("save log_data")

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


    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "author.html", context=context)


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

    # return render(req, "index.html", {'banner': ns})

    return render(req, "politics.html", {'page_obj': page_obj, 'news_list': news_list})


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

    # return render(req, "index.html", {'banner': ns})

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

    # return render(req, "index.html", {'banner': ns})

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

    # return render(req, "index.html", {'banner': ns})

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

    # return render(req, "index.html", {'banner': ns})

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

    # return render(req, "index.html", {'banner': ns})

    return render(req, "world.html", {'page_obj': page_obj, 'news_list': news_list})


def travel(req):

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        logger.info(f"POST log [IPaddr = {req.META.get('REMOTE_ADDR')}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
    else:
        logger.info(f"GET log [IPaddr = {req.META.get('REMOTE_ADDR')}]")

    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "travel.html", context=context)

def get_client_ip(request): #Ip 가져오기
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

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

    view = get_object_or_404(N_content, pk=n_id)
    lp = req.session.get('lp')

    # 조회수
    ip = get_client_ip(req)
    cnt = ViewCount.objects.filter(ip=ip, view_count=view).count()
    if cnt == 0:
        qc = ViewCount(ip=ip, view_count=view)
        qc.save()
        if view.view_count:
            view.view_count += 1
        else:
            view.view_count = 1
        view.save()

  
    query = f"""
        select n.n_id, n.n_title, n.nd_img, nc.n_content, n.o_link, ns_content, view_count
        from News n 
        inner join N_content nc on n.n_id = nc.n_id 
        inner join N_summarization ns on n.n_id = ns.n_id
        where n.n_id ={n_id} 
    """
    news = News.objects.raw(query)[0]

    context = {
        'news': news,
        'view': view
    }

    #return render(req, "news_post.html", {'news': news, 'view': view})
    return render(req, 'news_post.html', context)

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
