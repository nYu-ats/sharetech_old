from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from sharetech.models import Article
from sharetech.utils.ModelTemplateAdapter import ArticleAdapter
from django.http.response import JsonResponse

User = get_user_model()

class TopPageView(LoginRequiredMixin, View):
    # template_name = 'sharetech/top.html'
    # # TODO 固定値置き換え
    # __lateset_article_display_num = 10
    # __attention_article_display_num = 10
    # __follow_user_article_display_num = 10
    # __reccomend_article_display_num = 20
    
    # def get(self, request, *args, **kwargs):
    #     latest_articles_object_list = list(Article.objects.order_by('created_at')[:self.__lateset_article_display_num])
    #     # TODO 注目、おすすめ、フォローに表示する記事の抽出条件
    #     attention_article_object_list = list(Article.objects.order_by('viewed_count')[:self.__attention_article_display_num])
    #     follow_user_article_object_list = list()
    #     reccomend_article_object_list = list(Article.objects.order_by('-created_at')[:self.__reccomend_article_display_num])


    #     selected_article_list = {
    #         'latest_article' : ArticleAdapter(latest_articles_object_list).convert_to_template_context(),
    #         'attention_article' : ArticleAdapter(attention_article_object_list).convert_to_template_context(),
    #         'follow_user_article' : ArticleAdapter(follow_user_article_object_list).convert_to_template_context(),
    #         'reccomend_article' : ArticleAdapter(reccomend_article_object_list).convert_to_template_context(),
    #         }

    #     return render(request, 'sharetech/top.html', selected_article_list)
    pass

topPage = TopPageView.as_view()

# TODO 他ページでも使えるように抽象化する
class AsyncArticleLoadView(View):
    # # 固定値置き換え
    # __reccomend_article_display_num = 20
    # def get(self, request):
    #     if(request.is_ajax()):
    #         article_start_index = int(request.GET.get('index')) * self.__reccomend_article_display_num + 1
    #         article_end_index = article_start_index + self.__reccomend_article_display_num
    #         article_object_list = list(Article.objects.order_by('-created_at')[article_start_index:article_end_index])

    #         load_article = {
    #             'reccomend_article' : ArticleAdapter(article_object_list).convert_to_template_context(),
    #         }

    #         return render(request, 'sharetech/additional_article.html', load_article)
    pass

asyncArticleLoad = AsyncArticleLoadView.as_view()