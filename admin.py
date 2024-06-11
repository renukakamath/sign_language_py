from flask import *
from database import *




admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
    return render_template('adminhome.html')


@admin.route('/admin_manage_Subscription',methods=['get','post'])
def admin_manage_Subscription():
    data={}
    if 'btn' in request.form:
        policy=request.form['policy']
        amount=request.form['amt']
        no_days=request.form['no_days']
        
    
        q="insert into subscription values (null,'%s','%s','%s','0','pending')"%(policy,amount,no_days)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_Subscription"))

    data={}
    q="select * from subscription"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from subscription where subscription_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            policy=request.form['policy']
            amount=request.form['amount']
            no_days=request.form['no_days']

            q="update subscription set subscription='%s', amount='%s', planfor='%s' where subscription_id='%s' "%(policy,amount,no_days,pid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_Subscription"))
    if action == "delete":
        q="delete from subscription where subscription_id='%s' "%(pid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_Subscription"))
    return render_template('admin_manage_Subscription.html',data=data) 










@admin.route('/admin_view_user',methods=['get','post'])
def admin_view_user():
    data={}
    q="select * from user"
    res=select(q)
    data['res']=res 


    if "action" in request.args:
        action=request.args['action']
        uid=request.args['uid']

    else:
        action=None

    if action=='delete':
        q="delete from user where user_id='%s'"%(uid)
        delete(q)
        return redirect(url_for('admin.admin_view_user'))
    return render_template('admin_view_user.html',data=data)



@admin.route('/admin_view_image',methods=['get','post'])
def admin_view_image():
    data={}
    q="SELECT * FROM `uploadimage`  INNER JOIN `uploadvideo`  USING (`uploadvideo_id`) INNER JOIN `user` USING (user_id) "
    res=select(q)
    data['res']=res 
    return render_template('admin_view_image.html',data=data)




@admin.route('/viewsub',methods=['get','post'])
def viewsub():
    data={}
    uid=request.args['uid']
    q="SELECT * FROM `subscription` INNER JOIN `user` USING (user_id) WHERE user_id= '%s'"%(uid)
    res=select(q)
    data['sub']=res 
    return render_template('viewsub.html',data=data)