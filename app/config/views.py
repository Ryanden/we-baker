from django.shortcuts import redirect


def index(request):
    # return HttpResponse('index')
    # return HttpResponseRedirect('/posts/')
    return redirect('products:product-list')
