import cv2
from PIL import Image, ImageTk
from tensorflow.keras.models import model_from_json
from string import ascii_uppercase
import operator

def uploadimage(paths):
    vs = cv2.VideoCapture(paths)
    ok, frame = vs.read()

    if ok:
        cv2image = cv2.flip(frame, 1)

        x1 = int(0.1 * frame.shape[1])
        y1 = 10
        x2 = frame.shape[1] - 10
        y2 = int(0.7 * frame.shape[1])

        cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0) ,1)
        cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)

        current_image = Image.fromarray(cv2image)
        # imgtk = ImageTk.PhotoImage(image = self.current_image)


        # cv2image = cv2image[y1 : y2, x1 : x2]

        gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)
        image = cv2.imwrite('test.jpg',gray) 

        blur = cv2.GaussianBlur(gray, (5, 5), 2)

        th3 = cv2.adaptiveThreshold(blur, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        out=predict(res)
        print(out)
        return out

            
def predict(test_image):

    json_file = open("Models\\model_new.json", "r")
    model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(model_json)
    loaded_model.load_weights("Models\\model_new.h5")

    
    test_image = cv2.resize(test_image, (128, 128))

    
    result = loaded_model.predict(test_image.reshape(1, 128, 128, 1))


    # result_dru = self.loaded_model_dru.predict(test_image.reshape(1 , 128 , 128 , 1))

    # result_tkdi = self.loaded_model_tkdi.predict(test_image.reshape(1 , 128 , 128 , 1))

    # result_smn = self.loaded_model_smn.predict(test_image.reshape(1 , 128 , 128 , 1))

    prediction = {}

    prediction['blank'] = result[0][0]

    inde = 1

    for i in ascii_uppercase:

        prediction[i] = result[0][inde]

        inde += 1

    #LAYER 1

    prediction = sorted(prediction.items(), key = operator.itemgetter(1), reverse = True)

    current_symbol = prediction[0][0]
    return current_symbol



uploadimage("C:/Users/renuk/OneDrive/Desktop/a.jpeg")