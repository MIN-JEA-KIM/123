from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from django.contrib import auth

# -2022.01.24 park_jong_won
import logging
logger = logging.getLogger('news')

# -2022.02.07 park_jong_won add {def scrollLog, import datetime} del {def log}
from datetime import datetime


def scrollLog(req):

    x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = req.META.get('REMOTE_ADDR')


    if req.method == 'POST':
        if 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")
            # form = req.POST
            # logger.info(f"POST log [IPaddr = {req.META.get('REMOTE_ADDR')}, scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
            new_scroll_data = ScrollData(ipaddr=ip, acstime=datetime.now(), url=req.get_full_path(), staytime=req.POST['deltaTime'], scroll=req.POST['scroll'])
            new_scroll_data.save()
            print("save scroll_data")
        else:
            pass
    else:
        # logger.info("GET log")
        new_log = Log(ipaddr=ip, acstime=datetime.now(), url=req.get_full_path())
        new_log.save()
        print("save log_data")

    print(f"HTTP_X_FORWARDED_FOR = {req.META.get('HTTP_X_FORWARDED_FOR')}, REMOTE_ADDR = {req.META.get('REMOTE_ADDR')}, HTTP_X_REAL_IP = {req.META.get('HTTP_X_REAL_IP')}")


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
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

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

    # return render(req, "index.html", {'banner': ns})

    return render(req, "world.html", {'page_obj': page_obj, 'news_list': news_list})


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
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")

    query = f"""
        select n.n_id, n.n_title, n.nd_img, nc.n_content, n.o_link, ns_content
        from News n 
        inner join N_content nc on n.n_id = nc.n_id 
        inner join N_summarization ns on n.n_id = ns.n_id
        where n.n_id ={n_id} 
    """
    
    news = News.objects.raw(query)[0]  # models.py Board 클래스의 모든 객체를 board_list에 담음

    return render(req, "news_post.html", {'news': news})


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
	    
            query = f"select id, password from memberinfo where id = '{req.POST['id']}'"
            user = Memberinfo.objects.raw(query)
            
            try:
                f_password = user[0].password

                if req.POST['password'] == f_password:
                    data['login_massage'] = "환영합니다."
                else:
                    data['login_massage'] = "비밀번호를 잘못 입력하셨습니다."
            except:
                 data['login_massage'] = "없는 ID 입니다."
	        
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
