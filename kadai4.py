import cv2
import time

def __main():
    #0ならカメラ数は1,2以上は1～
    cap=cv2.VideoCapture(0)
    #ここで画面の解像度指定widthとheight
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)

    if not cap.isOpened():
        print('のっとおーぷんどびでおかめら')#ビデオキャプチャ可能か
        exit()
    ret,img=cap.read()

    if not ret:
        print('びでおきゃうちゃーえらー')
        exit()
    
    img=getResize(img)

    timeStart=time.time()
    #ここらから処理
    img = getPeople(img)

    timeEnd=time.time()

    print('{0}={1}'.format('CPU',(timeEnd-timeStart)*1000)+'/ms')
    cv2.imshow('ふぁいなるりざると',img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    cv2.imwrite("image.jpg", img)


def getPeople(img):
    global face_cascade
    #グローバル変数
    grayimg=cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)
    print(face_cascade)
    #NameError: name 'face_cascade' is not defined出てたがなんでか治った（後で調べる）

    facerect=face_cascade.detectMultiScale(grayimg,scaleFactor=1.01,minNeighbors=10)
    print(face_cascade)
    #体が検出されたら
    if len(facerect)>0:
        #赤で囲む
        for x,y,w,h in facerect:
            cv2.rectangle(img=img,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=3)
    return img

def getResize(img):
    basePixSize=640
    height=img.shape[0]
    width=img.shape[1]
    largeSize=max(height,width)
    resizeRate=basePixSize/largeSize
    img=cv2.resize(img,(int(width*resizeRate),int(height*resizeRate)))
    return img
if __name__ == '__main__':
    print(cv2.__version__)
    face_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
    #https://chigusa-web.com/blog/opencvsharp-haarcascade/ 千草webのopencvhaarcascade_frontalface_default.xmlの解説
    __main()
