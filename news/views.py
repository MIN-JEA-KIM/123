from datetime import datetime, timedelta
from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import *
from django.db.models import Q, Count, F
import logging
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
        else:
            pass
    else:

        new_log = Log(ipaddr=ip, acstime=datetime.now(), url=req.get_full_path())
        new_log.save()



def author(req, p_id=1):
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

    press_query='select * from Press order by p_id'
    sel_press_query=f"""
    select p.p_id, p_name, n.n_id, cd_id, n_title, nd_img, n_input, o_link, nso_id, nso_content
    from Press p
    inner join News n on p.p_id = n.p_id
    inner join N_summarization_one nso on n.n_id = nso.n_id
    where n.p_id = {p_id} and n_input != '9999-12-31 00:00:00'
    order by n.n_input desc
    """

    press_list = Press.objects.raw(press_query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    sel_press_list = Press.objects.raw(sel_press_query)
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(sel_press_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['press_list'] = press_list
    data['sel_press_list'] = sel_press_list
    data['page_obj'] = page_obj

    response = render(req, "author.html", data)

    return response


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
        order by n.n_id desc
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', 1)  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, 10)  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

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
        order by n.n_id desc
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
        order by n.n_id desc
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
        order by n.n_id desc
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
        order by n.n_id desc
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
        order by n.n_id desc
    """
    news_list = News.objects.raw(query)  # models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    data['page_obj'] = page_obj
    data['news_list'] = news_list

    return render(req, "world.html", data)

def news_post(req, n_id):

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
    ns_c = news.ns_content
    sum_list=[]

    while(ns_c.find('\n') != -1):
        sum_list.append(ns_c[:ns_c.find('\n')])
        ns_c = ns_c[ns_c.find('\n')+1:]

    data['ns_content'] = sum_list

    n_c = news.n_content
    cont_list=[]

    # print(n_c.find('. '))
    if n_c.find('. ') == -1:
        cont_list.append(n_c)
    else:
        while(n_c.find('. ') != -1):
            cont_list.append(n_c[:n_c.find('. ')+1])
            n_c = n_c[n_c.find('. ')+2:]

    data['n_content'] = cont_list


    login_session = req.session.get('login_session')
    
    # 조회수
    try:
        article = get_object_or_404(N_Viewcount, n_id = n_id)
    except:
        article = N_Viewcount.objects.create(n_id=n_id)
    data['article'] = article
    
    if req.method == "GET":
        data['article'] = article

        n_id: str = str(article.id)

        # 로그인 한 경우
        if req.user.is_authenticated is True:
            news_post = f'hits_{req.id}'
        # 비로그인 경우
        else:
            news_post = 'hits_0'

        # 쿠키로부터 방문기록 로드
        cookie_value: str = req.COOKIES.get(news_post, '')

        # 쿠키에 cookie_hits_key 항목이 있는 경우
        if news_post != '':
            n_id_list = cookie_value.split('|')
            # 방문한 경우는 그대로 응답
            if n_id in n_id_list:
                return render(req, 'news_post.html', data)
            # 방문하지 않은 경우
            else:
                new_hits_dict = (news_post, cookie_value+f'|{n_id}')
                article.hits = F('hits') + 1
                article.save()
                article.refresh_from_db()
        # hits 가 없는 경우
        else:
            new_hits_dict = (news_post, n_id)
            article.hits = F('hits') + 1
            article.save()
            article.refresh_from_db()

        response = render(req, 'news_post.html', data)

        # 만료시간 설정
        midnight_kst = datetime.replace(datetime.utcnow() + timedelta(days=1, hours=9), hour=0, minute=0, second=0)
        midnight_kst_to_utc = midnight_kst - timedelta(hours=9)

        response.set_cookie(*new_hits_dict,
                             expires=midnight_kst_to_utc,
                             secure=True,
                             httponly=True,
                             samesite='Strict')
        return response

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
            print("login")

            # data['login_massage'] = login(req)
            # data['session_id_check'] = False
            login_massage, session_user_check = login(req)
            data['login_massage'] = login_massage
            data['session_user_check'] = session_user_check
	        
        elif 'scroll' in req.POST.keys():
            logger.info(f"POST log [IPaddr = {ip}, scroll = {req.POST['scroll']}, deltaTime = {req.POST['deltaTime']}]")

        # elif req.session.get('user'):
        elif req.session.get('user', 'test'):
            print("logout")
            logout(req)
            data['session_user_check'] = False

    else : # GET
        logger.info(f"GET log [IPaddr = {ip},  url = {req.get_full_path()}]]")
        check = req.session.get('user', "test")
        if check == "test": # session값이 없는 경우
            data['session_user_check'] = False
        else:               # session 값이 있는 경우  == 이미 로그인을 한 상태
            data['session_user_check'] = True
            data['login_massage'] = "화형!!!"

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
        where c_id = {c_id} and n_input != '9999-12-31 00:00:00' and nd_img is not null and nd_img !='None'
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

    #전송 받은 이메일 비밀번호 확인
    u_id = req.POST.get('id')
    psw = req.POST.get('password')

    #유효성 처리
    res_data={}
    if not (u_id and psw):
        res_data = ("모든 칸을 다 입력해주세요.",False)

    else:
        query = f"select id, password from memberinfo where id = '{u_id}'"
        # 기존(DB)에 있는 Memberinfo 모델과 같은 값인 걸 가져온다.
        user = Memberinfo.objects.raw(query)

        # 비밀번호가 맞는지 확인한다.
        f_password = user[0].password
        f_id = user[0].id

        if f_password == psw:
            #응답 데이터 세션에 값 추가. 수신측 쿠키에 저장됨
            req.session['user'] = f_id, f_password

            res_data = ("환영합니다.", True)
            
        elif f_id != u_id:
            res_data = ("없는 아이디 입니다.", False)

        else:
            res_data = ("비밀번호가 틀렸습니다.", False)

    return res_data


def logout(req):
    # print(req.session['user'])
    req.session.clear()

    return redirect('/')