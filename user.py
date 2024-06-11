from flask import *
from database import *
import uuid
from newpredict import*





user=Blueprint('user',__name__)

@user.route('/userhome',methods=['get','post'])
def userhome():
    return render_template('userhome.html')
@user.route('/user_uploadimage',methods=['get','post'])
def user_uploadimage():
	data={}
	if "btn" in request.form:
		imgg=request.files['imgg']
		path='static/uploads/'+str(uuid.uuid4())+imgg.filename
		imgg.save(path)
		types=request.form['type']
		print("Starting Application...")
		from newpredict import predict 
		res=uploadimage(path)
		
		outs=uploadimage(path)

		
		
		q="insert into uploadvideo values(null,'%s',curdate(),'%s')"%(path,types)
		id=insert(q)
		q="insert into uploadimage values(null,'%s','%s','%s')"%(session['uid'],id,outs)
		insert(q)


		return redirect(url_for('user.user_uploadimage'))
	return render_template('user_uploadimage.html')



def ocrgenerate(path):
    print("path===",path)
    image = cv2.imread(path)
    # print(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Store grayscale image as a temporary file to apply OCR
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

    # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))

    print("OCR Text is " + text.strip())
    # val=text.strip().split('D')
    # atte=val[0].split(',')
    # print(atte[0],atte[1])
    # # print(val[1])
    return  text.strip()



# @api.route('/teacher_uploadvideos',methods=['post','get'])
# def teacher_uploadvideos():
#     data={}
#     # q="select * from videos inner join teacher using (teacher_id) inner join subject using (subject_id)"
#     # res=select(q)
#     # data['videoview']=res

#     # if "uploadvideo" in request.form:
#     #     i=request.files['i']
#     #     sid=request.args['sid']
#     #     tid=session['teacher_id']

#     #     path="static/videos"+str(uuid.uuid4())+i.filename
#     #     print('////////////////////////',path)
#     #     i.save(path)
       
#     #     q="insert into videos values(null,'%s','%s','%s',curdate(),'upload')"%(tid,sid,path)
#     #     insert(q)



#     if "upload" in request.form:
        
#         sid=request.args['sid']
#         tid=session['teacher_id']
#         video=request.files['video']
#         path="static/videos/"+str(uuid.uuid4())+video.filename
#         video.save(path)
#         q="insert into videos values(null,'%s','%s','%s',curdate(),'upload')"%(tid,sid,path)
#         insert(q)
#     # if "action" in request.args:
#     #   action=request.args['action']
        
#     # else:
#     #   action=None
#     if "vid" in request.args:
#         paths=request.args['path']
#         vid=request.args['vid']

#         cap = cv2.VideoCapture(paths)
   
#         # Check if camera opened successfully
#         if (cap.isOpened()== False): 
#           print("Error opening video  file")
           
#         framecount = 0
#         # Read until video is completed
#         while(cap.isOpened()):
              
#           # Capture frame-by-frame
#             ret, frame = cap.read()
#             if ret == True:
#                 framecount =framecount+ 1
#                 if framecount == 20:
#                     framecount = 0
#                     path="static/farmes/"+str(uuid.uuid4())+".jpg"
#                     # Display the resulting frame
#                     cv2.imshow('Frame', frame)
#                     cv2.imwrite(path, frame)
#                     val=ocrgenerate(path)
#                     print(val)
#                     val=val.replace("'","''")
#                     q="select * from farmes where frames like '%s'" %(val)
#                     res=select(q)
#                     print(res)
#                     fid=0
#                     if res:
#                         fid=res[0]['farme_id']
#                     else:
#                         q="insert into farmes value(null,'%s','%s','%s')" %(vid,path,val)
#                         fid=insert(q)

#                     splitvalue=val.split(' ')
#                     print(splitvalue)
#                     stopwords=['am','i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']
                    
#                     result = ""

#                     for i in splitvalue:
#                         i = i.strip();
#                         if i in stopwords:
#                             pass
#                         else:
#                             result = result + " "+i
                            
                                
#                     print("result is:",result)
#                     print(len(result))
#                     splitresult=result.split(' ')
#                     print(splitresult)
#                     print(len(splitresult))
                    
                    

#                     for i in range(1,len(splitresult)):
#                         q="insert into `keyword` values(null,'%s','%s')"%(fid,splitresult[i])
#                         print(q)
#                         insert(q)

#                     # Press Q on keyboard to  exit
#                     if cv2.waitKey(25) & 0xFF == ord('q'):
#                         break
           
#           # Break the loop
#             else: 
#                 break
           
#         # When everything done, release 
#         # the video capture object
#         cap.release()
           
#         # Closes all the farmes
#         cv2.destroyAllWindows()

#     if "vids" in request.args:
#         vid=request.args['vids']
#         q="select * from farmes where video_id='%s'" %(vid)
#         res=select(q)
#         data['frame']=res

#     # if action=="generateocr":

#     #   val=ocrgenerate(paths)
#     #   print(val)


#     q="select * from videos"
#     res=select(q)
#     data['video']=res
        
#     return render_template('teacher_uploadvideos.html',data=data)


