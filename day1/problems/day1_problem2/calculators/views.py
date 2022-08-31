from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    fir = request.GET.get('fir')
    sec = request.GET.get('sec')
    
    mns = int(fir)-int(sec) 
    mul = int(fir)*int(sec)
    if sec == '0':
        na = '계산할 수 없습니다.'
    else:
        na = int(int(fir)/int(sec))
    
    context = {
        'fir':fir,
        'sec':sec,
        'mns':mns,
        'mul':mul,
        'na':na
        
    }
    
    return render(request, 'catch.html', context)