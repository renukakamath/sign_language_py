from flask import * 
from database import* 
import uuid
from newpredict import*
from newcnn import *


api=Blueprint('api',__name__)

@api.route('/logins')
def logins():
	data={}
	u=request.args['username']
	p=request.args['password']
	q1="select * from login where username='%s' and `password`='%s'"%(u,p)
	print(q1)
	res=select(q1)
	if res:
		data['data']=res
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)


@api.route('/Userregistration')
def Userregistration():
	data={}
	f=request.args['fname']
	l=request.args['lname']
	
	pl=request.args['place']
	
	ph=request.args['phone']
	e=request.args['email']
	u=request.args['username']
	p=request.args['password']
	q="select * from login where username='%s' "%(u)
	res=select(q)
	if res:
		data['status']='already'
	else:
		q="insert into login values(NULL,'%s','%s','pending')"%(u,p)
		lid=insert(q)
		r="insert into user values(NULL,'%s','%s','%s','%s','%s','%s')"%(lid,f,l,pl,ph,e)
		uid=insert(r)

		q="update subscription set user_id='%s' where status='pending'"%(uid)
		update(q)
		print(r)
		data['status']="success"
	return str(data)

@api.route('/Farmer_upload_image',methods=['get','post'])
def Farmer_upload_image():
	data={}
	imgg=request.files['image']
	path='static/uploads/'+str(uuid.uuid4())+imgg.filename
	imgg.save(path)
	log_id=request.form['log_id']
	print("Starting Application...")
	# from newpredict import predict 	
	outs=predictcnn(path)
	print(outs)
		
	# if outs==0:
	# 	ss="0"
	# if outs==1:
	# 	ss="1"
	# if outs==2:
	# 	ss="2"
	# if outs==3:
	# 	ss="3"	
	# if outs==4:
	# 	ss="4"
	# if outs==5:
	# 	ss="5"
	# if outs==6:
	# 	ss="6"
	# if outs==7:
	# 	ss="7"
	# if outs==8:
	# 	ss="8"	
	# if outs==9:
	# 	ss="9"
	if outs==0:
		ss="a"
	if outs==1:
		ss="b"
	if outs==2:
		ss="c" 
	if outs==3:
		ss="d" 
	if outs==4:
		ss="e"
	if outs==5:
		ss="f" 
	if outs==6:
		ss="g" 
	if outs==7:
		ss="h"
	if outs==8:
		ss="i" 	
	if outs==9:
		ss="j" 	
	if outs==10:
		ss="k"
	if outs==11:
		ss="l"  
	if outs==12:
		ss="m" 
	if outs==13:
		ss="n" 
	if outs==14:
		ss="o" 
	if outs==15:
		ss="p" 
	if outs==16:
		ss="q" 
	if outs==17:
		ss="r" 	
	if outs==18:
		ss="s" 
	if outs==19:
		ss="t" 
	if outs==20:
		ss="u" 
	if outs==21:
		ss="v" 
	if outs==22:
		ss="w" 
	if outs==23:
		ss="x"
	if outs==24:
		ss="y"
	if outs==25:
		ss="z"	
				

	types="image"

	q="insert into uploadvideo values(null,'%s',curdate(),'%s')"%(path,types)
	id=insert(q)
	q="insert into uploadimage values(null,(select user_id from user where login_id='%s'),'%s','%s')"%(log_id,id,ss)
	insert(q)
	data['status']="success"
	data['method']="Farmer_upload_image"
	return str(data)


@api.route('/viewimg',methods=['get','post'])
def viewimg():
	data={}
	log_id=request.args['log_id']
	q="select * from uploadvideo inner join uploadimage using(uploadvideo_id) where user_id=(select user_id from user where login_id='%s')" %(log_id)
	print(q)
	res=select(q)
	print(res)
	data['data']=res
	data['status']="success"
	data['method']="viewimg"
	return str(data)



@api.route('/Viewsub',methods=['get','post'])
def Viewsub():
	data={}
	
	q="select * from subscription"
	res=select(q)
	print(res)
	data['data']=res
	data['status']="success"
	data['method']="Viewsub"
	return str(data)


@api.route('/okk',methods=['get','post'])
def okk():
	data={}
	uid=request.args['uid']
	
	q="update subscription set status ='subscribe'  where user_id='%s'"%(uid)
	update(q)

	q="update login set usertype='user'  where login_id=(select login_id from user where user_id='%s')"%(uid)
	update(q)
	print(res)
	data['data']=res
	data['status']="success"
	data['method']="Viewsub"
	return str(data)


@api.route('/Uploadvideo',methods=['get','post'])
def Uploadvideo():
	data={}
	lid=request.form['lid']

	video=request.files['video']
	path="static/uploads/"+str(uuid.uuid4())+video.filename
	video.save(path)
	cap = cv2.VideoCapture(path)
	# Check if camera opened successfully
	if (cap.isOpened()== False):
		print("Error opening video  file")
		
		# Read until video is completed
	framecount = 0
	while(cap.isOpened()):
	# Capture frame-by-frame
		ret, frame = cap.read()
		if ret == True:
			framecount =framecount+ 1
			if framecount == 20:
				framecount = 0
				paths="static/uploads/"+str(uuid.uuid4())+".jpg"
				# Display the resulting frame
				cv2.imshow('Frame', frame)
				cv2.imwrite(paths, frame)
				

				outs=predictcnn(paths)

				if outs==0:
					ss="a"
				if outs==1:
					ss="b"
				if outs==2:
					ss="c" 
				if outs==3:
					ss="d" 
				if outs==4:
					ss="e"
				if outs==5:
					ss="f" 
				if outs==6:
					ss="g" 
				if outs==7:
					ss="h"
				if outs==8:
					ss="i" 	
				if outs==9:
					ss="j" 	
				if outs==10:
					ss="k"
				if outs==11:
					ss="l"  
				if outs==12:
					ss="m" 
				if outs==13:
					ss="n" 
				if outs==14:
					ss="o" 
				if outs==15:
					ss="p" 
				if outs==16:
					ss="q" 
				if outs==17:
					ss="r" 	
				if outs==18:
					ss="s" 
				if outs==19:
					ss="t" 
				if outs==20:
					ss="u" 
				if outs==21:
					ss="v" 
				if outs==22:
					ss="w" 
				if outs==23:
					ss="x"
				if outs==24:
					ss="y"
				if outs==25:
					ss="z"	

				print(outs)
				# val=val.replace("'","''")

				q="insert into uploadvideo values(null,'%s',curdate(),'video')"%(path)
				ids=insert(q)

				print(q)
				q="insert into frames value(null,'%s','%s','%s')" %(ids,paths,ss)
				fid=insert(q)

				q="insert into uploadimage  values(null,(select user_id from user where login_id='%s'),'%s','%s')"%(lid,ids,ss)
				insert(q)

				print(q)
				# Press Q on keyboard to  exit
				if cv2.waitKey(25) & 0xFF == ord('q'):
					break
				else:
					break
	cap.release()
	cv2.destroyAllWindows()

	data['status']="success"
	return str(data)