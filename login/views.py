from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root", passwd="Komal12582#",database="website")
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="Email":
                em=value
            if key=="Password":
                pwd=value
        
        c=" select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
       
    
    return render(request,'login.html')
