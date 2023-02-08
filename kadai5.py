#webサーバーを使用したビデオストリーミング djangoでもいけそうだが、bottleの参考例があるためこっちを使用
import cv2
import bottle
import time

web=bottle.Bottle()

def __main():
    #0ならカメラ数は1,2以上は1～
    cap=cv2.VideoCapture(0)
    #ここで画面の解像度指定widthとheight
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)
    
    if not cap.isOpened():
        print('のっとおーぷんどびでおかめら')#ビデオキャプチャ可能か
        exit()


    while True:
        ret,img=cap.read()
        if not ret:
            print('びでおきゃうちゃーえらー')
            break

        grayimg=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
        face_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
        #模範のhaarcascade_frontalface_alt.xmlは正面の顔、こっちは体

        facerect=face_cascade.detectMultiScale(grayimg,scaleFactor=1.01,minNeighbors=2,minSize=(50,50))
        
        print(face_cascade)
        print('32')
        #体が検出されたら
        if len(facerect)>0:
            #赤で囲む
            for rect in facerect:
                cv2.rectangle(img,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),(0,0,255),thickness=3)
        
        #処理を実行
        result,jpgImg=cv2.imencode('.jpg',img=img,params=[int(cv2.IMWRITE_JPEG_QUALITY),80])
        yield   b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\n'+bytearray(jpgImg)+b'\r\n\n'
        time.sleep(1/60)

    cap.release()
    cv2.destroyAllWindows()

    return 0
@web.route('/')
def main():
    return bottle.static_file('index.html',root='./')

@web.route('/video_recv')
def video_recv():
    bottle.response.content_type='multipart/x-mixed-replace;boundary=frame'
    #ここ誤字ると動かない
    return __main()

if __name__=='__main__':
    print(cv2.__version__)

    web.run(host='localhost',port=8080)
    #記事見ながら自身の自宅Wi-Fiでやった場合localhost、学校ラズパイは別192.168.2.555でもいけるぽい
    #web.run(host='192.168.5.222',port=8080,reloader=True,debug=True)



