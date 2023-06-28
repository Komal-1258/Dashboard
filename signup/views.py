from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
dob=''
gender=''
add=''
state=''
em=''
pwd=''
# Create your views here.
def signupaction(request):
    global fn,ln,dob,gender,add,state,em,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root", passwd="Komal12582#",database="website")
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=='FirstName':
                fn=value
            if key=='LastName':
                ln=value
            if key=='DOB':
                dob=value
            if key=='Gender':
                gender=value
            if key=='Address':
                add=value
            if key=='State':
                state=value
            
            if key=="Email":
                em=value
            if key=="Password":
                pwd=value
        
        c="insert into  users values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,dob,gender,add,state,em,pwd)
        cursor.execute(c)
        m.commit()
       
    
    return render(request,'signup.html')
