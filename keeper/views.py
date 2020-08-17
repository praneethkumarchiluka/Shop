from django.shortcuts import render,redirect
from .models import items
from .forms import Itemsform
from django.db.models import Sum
import pandas as pd
# Create your views here.
def home(request):
    
    if request.method != 'POST':
        
        print(request.method)
        form=Itemsform()
    else:
        a=request.POST.get('item')
        b=request.POST.get('quantity')
        c=request.POST.get('rate')
        name=request.POST.get('fname')
        items.objects.create(itemname=a,quantity=b,rate=c)
        return render(request,'home.html',{'name1':name})
    context={'form':form}
    print('prani',form.errors)
    return render(request,'home.html',context)

def total(request):
    item=[]
    quan=[]
    rate=[]
    data=pd.DataFrame(columns=['itemname','quantity','rate'])
    a=items.objects.all()
    b=items.objects.count()
    c=items.objects.aggregate(Sum('rate'))
    d=items.objects.values('itemname','quantity','rate')
    for i,j in c.items():
        total=j
    for i in d:
        item.append(i['itemname'])
        rate.append(i['rate'])
        quan.append(i['quantity'])
    data['itemname']=item
    data['quantity']=quan
    data['rate']=rate
    name=request.POST.get('fname')

    return render(request,'total.html',{'del':a,'count':b,'total':total})

def edit(request,id):
    val=items.objects.get(id=id)
    if request.method == 'POST':
        a=request.POST.get('id')
        d=request.POST.get('item')
        b=request.POST.get('quantity')
        c=request.POST.get('rate')
        items.objects.filter(id=a).update(itemname=d,quantity=b,rate=c)
        return redirect('keeper:total')
    return render(request,'edit.html',{'del':val})

def delete(request,id):
    val=items.objects.get(id=id)
    val.delete()
    return redirect('keeper:total')

def remove(request):
    val=items.objects.all()
    val.delete()
    a="Success"
    return redirect('keeper:home')


from django.views.generic import View
from .render import Render


class Pdf(View):

    def get(self, request):
        a=items.objects.all()
        b=items.objects.count()
        c=items.objects.aggregate(Sum('rate'))
        name=request.GET.get('fname')
        for i,j in c.items():
            total=j
        params = {
            'del':a,'count':b,'total':total,'name':name,
            'request': request
        }
        return Render.render('pdf1.html', params)

#from django.http import HttpResponse
#from django.template.loader import render_to_string
#from weasyprint import HTML
#import tempfile
#def export(request):
#    response = HttpResponse(content_type='application/pdf')
#    response['Content-Disposition'] = 'attachement; filename=Bandi kistaiah.pdf'
#    response['Content-Transfer-Encoding']='binary'
#    a=items.objects.all()
#    b=items.objects.count()
#    c=items.objects.aggregate(Sum('rate'))
#    for i,j in c.items():
#        total=j
#    html_string=render_to_string('pdf1.html',{'del':a,'count':b,'total':total})
#    html=HTML(string=html_string)
#    result=html.write_pdf()
#    with tempfile.NamedTemporaryFile(delete=True) as output:
#        output.write(result)
#        output.flush()
#        output=open(output.name,'rb')
#        response.write(output.read())
#    return response
