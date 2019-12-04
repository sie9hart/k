from django import forms
from libra.models import Books
from libra.models import Cust

c={}
c=Books.objects.values_list('bookname', 'bookname')
c2=Cust.objects.values_list('custname', 'custname')




        




        

    
class Book_Form(forms.Form):
        bookname=forms.CharField(label='bookname',max_length=25)
        isbn=forms.IntegerField(label='isbn')
        available=forms.BooleanField(initial=False)
class Cust_Form(forms.Form):
        custname=forms.CharField(label='custname',max_length=25)
        custid=forms.IntegerField(label='custid')
class Borrow_Form(forms.Form):
        custname=forms.ChoiceField(choices=c2)
        bookname=forms.ChoiceField(choices=c)
