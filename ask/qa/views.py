from django.shortcuts import render
from .models import Answer, Question
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import AskForm, AnswerForm
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def popular_list(request):
    qs = Question.objects.all()
    qs = qs.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular_list') + '?page='

    return render(request, 'qa/popular_list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def new_question_list(request):
    qs = Question.objects.all()
    qs = qs.order_by('-added_at')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('new_question_list') + '?page='

    return render(request, 'qa/new_question_list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = Answer.objects.filter(question_id=pk)
    form = AnswerForm(request.POST)
    return render(request, 'qa/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form,
       # 'pk': pk,
    })

def add_answ(request):
    if request.method=='POST':
        form = AnswerForm(request.POST)

        if request.user.is_authenticated():
            pass
        else:

            if form.is_valid():
                post = form.save(commit=False)
                post.author = User(id=1)
                post.added_at = timezone.now()
                post.save()
                url = reverse('question_detail', args=[post.question_id])

                return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'qa/ad_answ.html', {'form': form})
