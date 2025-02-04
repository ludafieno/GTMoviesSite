from django.shortcuts import render

def index(request):
    return render(request, 'movieSite/index.html')
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'movieSite/about.html',{'template_data': template_data})
