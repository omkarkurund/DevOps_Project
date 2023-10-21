from django.shortcuts import render
from datetime import datetime
from Restaurant_App.models import *
from math import ceil
# Create your views here.

#home page
def index(request):
    return render(request,'index.html')

#Contact page
def contact(request):
    if request.method == "POST":
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        desc=request.POST.get('decr')
        contact = Contact(f_name=f_name,l_name=l_name,email=email,phone_no= phone_no,desc= desc,date= datetime.today())
        contact.save()

    
    
    return render(request,'contact.html')


def menu(request):
    items=Categories.objects.all()
    print(items)
    n=len(items)
    n_slides= n//4 + ceil((n/4)-(n//4))
    param={"no_of_slides":n_slides,"item":items,"range":range(1,n_slides)}
    return render(request,'menu.html',param)


def qrcode(request):
    # prod=Veg_Item.objects.all()
    # print(item)
    # n=len(item)
    # n_slides= n//4 + ceil((n/4)-(n//4))
    # # param={"no_of_slides":n_slides,"item":items,"range":range(1,n_slides)}
    # allItems= [[item,range(1,n_slides,n_slides)], 
    #            [item,range(1,n_slides,n_slides)]]
    # params={"allItems":allItems}
    allItems=[]
    catItems= Categories.objects.values('category', 'id')
    cats= {i["category"] for i in catItems}
    for cat in cats:
        item=Categories.objects.filter(category=cat)
        n = len(item)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allItems.append([item, range(1, nSlides)])

    params={'allItems':allItems }
    return render(request,'qc_food_order.html',params)


# def signupuser(request):
#     if request.method == "POST":
#         name = request.POST["name"]
#         email = request.POST["uemail"]
#         password= request.POST["pass"]
        
#         user = User_Data.objects.create_user(name, email, password)
#         user.save()
#         messages.success(request, "Your Account Created Successfully")
#         return redirect('/login/')
#     return render(request,'signup.html')

# def loginuser(request):
#     if request.method == "POST":
#         uname= request.POST["uname"]
#         password = request.POST["pass"]
#         user = authenticate(username=uname, password=password)
#         if user is not None:
#             # A backend authenticated the credentials
#             login(request,user)
#             messages.success(request, "Your are Login Successfully")
#             return redirect('/')
#         else:
#             # No backend authenticated the credentials
#             return render(request,'login.html') 

#     return render(request,'login.html')