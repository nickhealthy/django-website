from django.urls import path    
from . import views

app_name = 'polls' # URL 패턴의 이름이 충돌나는 것을 방지하기 위한 namespace 정의
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
