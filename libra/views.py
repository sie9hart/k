from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from libra.models import Books 
from libra.models import Cust
from libra.models import Borrow1
from libra.forms import Book_Form
from libra.forms import Cust_Form
from libra.forms import Borrow_Form
from django.contrib import messages

def server(request):
   
    
    return render(request,'ll.html')
def Book(request):
   
    f={}
    li2=Books.objects.all()
    f['my_list2']=li2
    return render(request,'books.html',context=f)
def cust(request):
   
    f={}
    li2=Cust.objects.all()
    f['my_list2']=li2
    return render(request,'custs.html',context=f)
  

   
   
def sform(request):
    k={}
    k['forms']=Book_Form
     
    if request.method =="POST":
        form=Book_Form(request.POST)
        if form.is_valid():
            new_book=Books()
            xx=form.cleaned_data['isbn']
            s=Books.objects.filter(isbn=xx).exists()
            if s:
               messages.warning(request, 'this book is registered .')  

            else:  
               new_book.bookname=form.cleaned_data['bookname']
               new_book.available=forms.cleaned_data['available']
               new_book.isbn=form.cleaned_data['isbn']
               new_book.save()
    return render(request,'f.html',context=k)

def sform2(request):
    k={}
    k['forms']=Cust_Form
     
    if request.method =="POST":
        
        form=Cust_Form(request.POST)
        if form.is_valid():

            new_cust=Cust()
            s2=Cust.objects.filter(custid=xxx).exists()
            xxx=form.cleaned_data['custid']
            if s2:
                messages.warning(request, 'this cust is registered .')  
            else:
                new_cust.custname=form.cleaned_data['custname']
            
                new_cust.custid=form.cleaned_data['custid']
                new_cust.save()
    return render(request,'a.html',context=k) 





def sform3(request):
    
    
    

            
    k={}
    k['forms']= Borrow_Form
    
     
    
    if request.method =="POST":
        form=Borrow_Form(request.POST)
        if form.is_valid():
            new_b=Borrow1()
            new_cust=Cust()
            new_book=Books()
            xx=new_book.bookname=form.cleaned_data['bookname']
            xxx=new_cust.custname=form.cleaned_data['custname']
            xw=new_b.custname=form.cleaned_data['custname']
            

            x=new_b.bookname=form.cleaned_data['bookname']
            s=Books.objects.filter(bookname=xx).exists()
            s2=Cust.objects.filter(custname=xxx).exists()

            new_book.isbn=form.cleaned_data['bookname']
                
            if  Borrow1.objects.filter(bookname=x).exists() :
                if Borrow1.objects.filter(custname=xw).exists():
                    post = Books.objects.get (bookname=xx)    
                    if Books.objects.filter(available=True).exists():
                            post.available = False
                            Borrow1.objects.filter(bookname=x).delete()
                            post.save()
                            messages.success(request, 'return success')
                    
                else:
                             messages.error(request, 'this is not who borrow the book')
                    

                            
                    
                            
                            
                            
            else :           
                post = Books.objects.get (bookname=xx)
                if Books.objects.filter(available=False).exists():
                        post.available = True
                        post.save()
                       
                        new_b.save()
                        messages.success(request, 'booking succss')
                

    return render(request,'h.html',context=k) 


def Borrows(request):
   
    f={}
    li2=Borrow1.objects.all()
    f['my_list2']=li2
    return render(request,'Borrow.html',context=f)  
    
                                                                    

    
     
    
   
                    
           