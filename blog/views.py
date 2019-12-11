import os
from django.http import HttpResponse


# Create your views here.
def post_list(request):
    # 상위폴더(blog)
    #  상위폴더 (djangogirls)
    #    하위폴더 (template)
    #       하위파일 (post_list.html)내요ㅕㅇ을 read()한 결과를 httpResponse에 인자로 전달

    # 경로이동
    # os.path.apspath(__file__) <-현재 파일의 절대경로를 리턴해ㅈㅁ
    # os.path.dirname
    # os.path.join
    # 파일열기
    #  open

    cur_file_path = os.path.abspath(__file__)
    parent_dir_path = os.path.dirname(cur_file_path)
    target_file_path = os.path.join(os.path.dirname(parent_dir_path), 'templates', 'post_list.html')
    print(cur_file_path)
    print(parent_dir_path)
    print(target_file_path)

    # cur_file_path = os.path.abspath(__file__)
    # blog_dir_path = os.path.dirname(cur_file_path)
    # path = blog_dir_path + '/../templates/post_list.html'
    # print(path)
    with open(target_file_path, 'rt') as f:
        html = f.read()

    return HttpResponse(html)
