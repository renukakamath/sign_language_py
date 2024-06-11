from flask import *
from database import *


public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')


@public.route('/login',methods=['post','get'])
def login():

    if 'btn' in request.form:
        uname=request.form['uname']
        pasw =request.form['pasw']

        q="select * from login where username='%s' and password='%s'"%(uname,pasw)
        res=select(q)


        if res:
            session['loginid']=res[0]["login_id"]
            utype=res[0]["usertype"]
            if utype == "admin":
                flash("Login Success")
                return redirect(url_for("admin.adminhome"))
            elif utype == "user":
                q="select * from user where login_id='%s'"%(session['loginid'])
                val=select(q)
                if val:
                    session['uid']=val[0]['user_id']
                    flash("Login Success")
                    return redirect(url_for("user.userhome"))

               
            
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("Invalid Username or Password!")
            return redirect(url_for("public.login"))


    return render_template("login.html")

@public.route('/user_registration' ,methods=['post','get'])
def user_registration():
    
    if "tutor" in request.form:
        f=request.form['fname']
        l=request.form['lname']
        p=request.form['phone']
        e=request.form['email']
        pl=request.form['place']
        u=request.form['uname']
        pwd=request.form['pwd']

        q="insert into login values(null,'%s','%s','user')"%(u,pwd)
        id=insert(q)
        
        q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,f,l,pl,p,e)
        uid=insert(q)
        print(q)
        q="insert into subscription values(null,'0','0','0','%s')"%(uid)
        insert(q)

        flash('insert successfully');
        return redirect(url_for('public.admin_manage_Subscription',uid=uid))


                
    return render_template('user_registration.html')


@public.route('/admin_manage_Subscription',methods=['get','post'])
def admin_manage_Subscription():
    data={}
    if 'btn' in request.form:
        policy=request.form['policy']
        amount=request.form['amount']
        no_days=request.form['no_days']
        uid=request.args['uid']
        
    
        q="update subscription set subscription='%s',amount='%s',planfor='%s' where user_id='%s' "%(policy,amount,no_days,uid)
        update(q)
        flash("Successfully Added")
        return redirect(url_for("public.login"))

   
    return render_template('admin_manage_Subscription.html',data=data) 




