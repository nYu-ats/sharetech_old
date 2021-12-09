from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    '''
    ランディングページ
    BasePageCommonView クラスを継承していないのでリダイレクトされない
    '''
    # ランディングページテンプレート
    template_name = 'sharetech/landing.html'

landing_page = LandingPageView.as_view()
