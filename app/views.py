from django.shortcuts import render

# Create your views here.
def builtin_filter(request):
    d={'data':'Hi pYthOn hOW aRe yOu','c':1000000000}
    return render(request,'builtin_filter.html',d)

def userdefined_filter(request):
    d={'data':'mY nAmE is AbbU bAKaR'}
    return render(request,'userdefined_filter.html',d)