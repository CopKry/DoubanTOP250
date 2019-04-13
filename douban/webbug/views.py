from django.shortcuts import render
# Create your views here.
from django.db import connection

def index(request):
    cursor=connection.cursor()
    cursor.execute("select * from t_douban")
    rows=cursor.fetchall()
    return render(request,'index.html',{'content':rows})
