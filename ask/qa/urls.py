from django.conf.urls import url
from .views import login_u, new_question_list, popular_list, question_detail, add_answ,ask, signup, welcom
#from django.contrib.auth.views import login_u, logout


urlpatterns = [
    url(r'^$', popular_list, name='popular_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    #url(r'^popular/', popular, name='popular'),
    url(r'^ask/', ask, name='add_ask'),
    url(r'^welcom/', welcom, name='add_ask'),
    #url(r'^answer/', question_answer, name='question_answer'),
   #  url(r'^answer/', answer_st, name='answer11'),
     #url(r'^answers/', answer_list, name='answers'),
    url(r'^signup/', signup, name='signup'),
    url(r'^login/', login_u, name='login'),
   # url(r'^logout/', user_logout, name='logout'),
    url(r'^new/', new_question_list, name='new_question_list'),
     url(r'^ad_answ/', add_answ, name='add_answ'),
]
