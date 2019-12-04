from django.db import models

class Books(models.Model):
    bookname=models.CharField(max_length=25)
    isbn=models.IntegerField(null=True,blank=True)
    available = models.BooleanField(default=False)
    def __str__(self):
        return '{} {}'.format(self.bookname, self.isbn)
class Cust(models.Model):
      custname=models.CharField(max_length=25)
      custid=models.IntegerField(null=True,blank=True)
      def __str__(self):
        return '{} {}'.format(self.custname, self.custid)
class Borrow1(models.Model):
    custname=models.CharField(max_length=25)
    bookname=models.CharField(max_length=25)
    isbn=models.IntegerField(null=True,blank=True)
    custid=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(self.custname, self.bookname)
    
       
        
    

      


