from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect

from blog.models import Post


def post_list(request):
    # # 상위폴더(blog)
    # #  상위폴더 (djangogirls)
    # #    하위폴더 (template)
    # #       하위파일 (post_list.html)내을 read()한 결과를 httpResponse에 인자로 전달
    #
    # # 경로이동
    # # os.path.apspath(__file__) <-현재 파일의 절대경로를 리턴해준
    # # os.path.dirname
    # # os.path.join
    # # 파일열기
    # #  open
    #
    # cur_file_path = os.path.abspath(__file__)
    # parent_dir_path = os.path.dirname(cur_file_path)
    # target_file_path = os.path.join(os.path.dirname(parent_dir_path), 'templates', 'post_list.html')
    # print(cur_file_path)
    # print(parent_dir_path)
    # print(target_file_path)
    #
    # # cur_file_path = os.path.abspath(__file__)
    # # blog_dir_path = os.path.dirname(cur_file_path)
    # # path = blog_dir_path + '/../templates/post_list.html'
    # # print(path)
    # with open(target_file_path, 'rt') as f:
    #     html = f.read()
    #
    # return HttpResponse(html)

    # template를 찾을 경로에서
    # post_list.html을 찾아서
    # 그 파일을 text로 만들어서 httpResponse형태로 돌려준다
    # 위 기능을 하는 shortcut함수

    # posts = Post.objects.all()
    # posts = Post.objects.all()[::-1]  -> 이렇게 하면 post가 list 객체가 된다. QuerySet객체가 아니기 떄문에 QuerySet객체의 메소드를 사용못함
    # 아래처럼 한다면 db 자체에서 정렬 수행해서 가져옴, sql문이 달라진다.
    posts = Post.objects.order_by('-pk')
    context = dict(posts=posts)

    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    print(request)
    print(pk)

    try:
        post = Post.objects.get(pk=pk)
        print("포스트입니다", post)
        context = dict(post=post)
        return render(request, 'post_detail.html', context)
    except Post.DoesNotExist:
        return HttpResponse('<h1>없음</h1>')
    # post = get_object_or_404(Post, pk=pk)


def post_add(request):
    # print(request.POST)
    # title = request.POST['title']
    # text = request.POST['text']
    # print(title, text)
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        text = request.POST['text']
        print(title, text)

        m = Post.objects.create(
            author=request.user,
            title=title,
            text=text
        )

        result = f'title:{m.title}, create_date:{m.created_date}'
        # return HttpResponse(result)

        # post_list_url = reverse('url-name-post-list')
        # return HttpResponseRedirect(post_list_url)
        # ------ 위 두개 shortcut!!
        return redirect('url-name-post-list')

        # return HttpResponseRedirect('/posts/')
    else:
        return render(request, 'post_add.html')


def post_delete_confirm(request, pk):
    if request.method == 'POST':
        post_delete(request, pk)
        return redirect('url-name-post-list')

    else:
        post = Post.objects.get(pk=pk)
        context = dict(post=post)
        return render(request, 'post_delete_confirm.html', context)


def post_delete(request, pk):
    # pk에 해당하는 Post를 삭제한다
    # 삭제 후에는 post_list페이지로 이동
    delete_item = Post.objects.get(pk=pk)
    delete_item.delete()


def post_edit(request, pk):
    if request.method == 'POST':
        edit_item = Post.objects.get(pk=pk)
        edit_item.title = request.POST['title']
        edit_item.text = request.POST['text']
        edit_item.save()
        return redirect('url-name-post-list')
    else:
        original_item = Post.objects.get(pk=pk)
        context = dict(post=original_item)
        return render(request, 'post_edit.html', context)


def post_publish(request, pk):
    # pk에 해당하는 Post의 published_date를 업데이트
    # 요청시점의 시간을 해당 Post의 published_date에 기록할 수 있도록 한다
    # 완료후에는 post-detail로 이동
    #  결과를 볼 수 있도록, 리스트 및 디테일 화면에서 published_date도 출력하도록 한다
    item = Post.objects.get(pk=pk)
    item.publish()
    return redirect('url-name-post-detail', pk=pk)


def post_unpublish(request, pk):
    # pk에 해당하는 Post의 published_date에 None을 대입 후 save()
    # 완료후에는 post-detail로 이동
    #  결과를 볼 수 있도록, 리스트 및 디테일 화면에서 published_date도 출력하도록 한다
    item = Post.objects.get(pk=pk)
    item.published_date = None
    item.save()
    return redirect('url-name-post-detail', pk=pk)
