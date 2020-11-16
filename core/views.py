from django.shortcuts import render,redirect
from core.models import Product,Flavour,Order,OrderItem
from django.shortcuts import get_object_or_404
from django.http import JsonResponse,HttpResponseNotFound
from django.conf import settings
from django.core.mail import EmailMultiAlternatives    
from django.template.loader import render_to_string
from django.conf import settings

import random
import json
from twilio.rest import Client


def index(request):
    return render(request,"index.html",{"qs":Product.objects.all()})

def search(request):
    return render(request,"search.html")

def search_ajax(request):
    query = request.GET.get("query")
    if query:
        s = Flavour.objects.filter(name__istartswith = query)
        data = []
        for i in s.all():
            data.append([i.pk,i.image.url,i.name,i.description,i.price,i.parent.pk])
        return JsonResponse({"data":data})
    return JsonResponse({"data":"wrong"})

def product(request,pk):
    obj = get_object_or_404(Product,pk = pk)
    return render(request,"flavours.html",{"product":obj})

def flavour(request,pk,fpk):
    obj = get_object_or_404(Product,pk = pk)
    fla = get_object_or_404(Flavour,pk = fpk,parent= obj)
    return render(request,"flavour.html",{"flavour":fla,"product":obj})

def order(request):
    return render(request,"review.html")

def track(request):
    return render(request,"order-status.html")

def track_ajax(request):
    query = request.GET.get("query")
    if query:
        s = Order.objects.filter(order_id = query)
        if s:
            return JsonResponse({"found":True,"data":s[0].status})
        else:
            return JsonResponse({"found":False})
    return JsonResponse({"data":"wrong"})

def contact(request):
    return render(request,"checkout.html")

def select_area(request):
    return render(request,"area.html")

def thankyou(request,id):
    return render(request,"thankyou.html",{"id":id})


def confirm(request):
    if request.method == "POST":
        data = request.POST.get("ST")
        if data:
            try:
                data = json.loads(data)
            except:
                print("Invalid Json")
                data = {}
            
            if data.get("name") and data.get("email") and data.get("phone") and data.get("area") and data.get("street") and data.get("house") and data.get("cart"):
                specific_directions = data.get("specific_directions") if data.get("specific_directions") else ''
                phone = data['phone']

                if phone.startswith("0"):
                    phone = phone[1:]

                if phone.startswith("971"):
                    phone = '+' + phone
                
                if not phone.startswith("+971"):
                    phone = '+971' + phone

                o = Order(
                    name = data['name'],
                    email = data['email'],
                    phone = phone,
                    area = data['area'],
                    country = data['country'],
                    shipping = data['shipping'],
                    street = data['street'],
                    house = data['house'],
                    specific_directions = specific_directions)

                if len(data.get("cart")) >0:
                    o.save()
                    for i in data['cart']:
                        f = Flavour.objects.filter(pk = i['pk'])
                        if f and i['quantity'] > 0:
                            f = f[0]
                            o1 = OrderItem.objects.create(flavour_linked = f,quantity = i['quantity'],user_order = o)
                        else:
                            o.delete()
                            print("Invalid Flavour")
                            return HttpResponseNotFound('')
                    
                    total = 0
                    for i in o.orderitem_set.all():
                        total += i.quantity * i.flavour_linked.price
                    o.subtotal = total 
                    o.total = total + data['shipping']
                    o.status = 'In Progress'
                    o.order_id = ''.join([random.choice("0123456789") for i in range(6)])
                    o.save()

                    body = render_to_string("email_template.html",{"items":o.orderitem_set.all(),"shipping":o.shipping,"total":o.total})
                    msg = EmailMultiAlternatives("ملخص طلبكم من بسكوتي", body, to= [o.email])
                    msg.attach_alternative(body, "text/html")
                    try:
                        msg.send()
                    except:
                         print("Error While Sending Email")
                    # msg.send()

                    client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
                    try:
                        message = client.messages \
                            .create(
                                body=f"نشكر لكم اختياركم بسكوتي، تم تأكيد طلبكم ، رقم {o.order_id} بقيمة AED{o.total} .",
                                from_='+14637772322',
                                to=o.phone
                            )
                        print(message.sid)
                    except:
                        print("error while sending msg")
                    return redirect("core:thankyou",id=o.order_id)                             
                else:
                    print("invalid cart")
            else:
                print("Invalid Data")
    return render(request,"place-order.html")
