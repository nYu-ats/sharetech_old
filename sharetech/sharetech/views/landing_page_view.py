from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    '''
    ランディングページ
    '''
    # ランディングページテンプレート
    template_name = 'sharetech/landing.html'

landing_page = LandingPageView.as_view()
