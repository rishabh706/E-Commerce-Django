from django.views.generic import TemplateView
class HomePage(TemplateView):
    template_name='base.html'

class HomePage2(TemplateView):
    template_name='base2.html'
