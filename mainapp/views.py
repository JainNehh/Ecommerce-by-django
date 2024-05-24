from django.shortcuts import render,HttpResponse,redirect
from.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def ecommerce(request):
     data=Product.objects.filter(category="Featured")
     context={
          'data':data
     }
     return render(request,"e-commerce.html",context)
def loginhandle(request):
      if request.method=="POST":
           uname=request.POST['username']
           passw=request.POST['password']
           user=authenticate(username=uname,password=passw)
           if user is not None:
                login(request,user)
                return redirect('/')
           print(user,'user>>><<<')
      return render(request,"login.html")



def logouthandle(request):
     logout(request)
     return redirect('/')




def signuphandle(request):
      if request.method=='POST':
           uname=request.POST['username']
           email=request.POST['email']
           passw=request.POST['password']
           
           
           if User.objects.filter(username=uname).first():
                messages.success(request,"Username already taken !")
           else:
                 user=User(username=uname,email=email)
                 user.set_password(passw)
                 user.save()
                 messages.success(request,"Account create successfull")
                 print(uname,email,passw)
                


          

      return render(request,"Signup.html")





def checkout(request):
     return render(request,'checkout.html')

def cart(request):
     return render(request,'cart.html')

def product_desc(request,id):
     get_product_data=Product.objects.filter(id=id)
     context={
          'data':get_product_data
     }
     return render(request,'productdescription.html',context)

def men(request):
     # data=Product.objects.all()
     data=Product.objects.filter(category="Men")
     context={
          'data':data
     }
     # for i in data:
     #      print(i.title,i.price,i.description)
     
     return render(request,'men.html',context)

def women(request):
     # data=Product.objects.all()
     data=Product.objects.filter(category="Women")
     context={
          'data':data
     }
     # for i in data:
     #      print(i.title,i.price,i.description)
     
     return render(request,'women.html',context)

def kids(request):
     # data=Product.objects.all()
     data=Product.objects.filter(category="Kids")
     context={
          'data':data
     }
     # for i in data:
     #      print(i.title,i.price,i.description)
     
     return render(request,'kids.html',context)

def about(request):
     return render(request,'aboutus.html')

def contact(request):
     return render(request,'contactus.html')