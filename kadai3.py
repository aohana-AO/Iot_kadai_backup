import cv2
def gazouseisei():
    if __name__ == '__main__':

    #０ならカメラ数は１、２以上は1～
        cap = cv2.VideoCapture(0)
    #ここで画面の解像度指定widthとheight
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        if not cap.isOpened():                  # ビデオキャプチャー可能か判断
            print("Not Opened Video Camera")
            exit()

        ret, img = cap.read()
            

        #画面表示が以下２行。wait keyが必要らしい？

        cv2.imshow("Final result",img)
        cv2.waitKey(0) 
        cv2.imwrite('kyousitu2.JPG', img)

        cap.release()
        cv2.destroyAllWindows()

def rinnkaku():
    img_origin = cv2.imread('kyousitu2.JPG', 1)
    img = cv2.bitwise_not(img_origin)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray, 150, 255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    img_contour = cv2.drawContours(img_origin, contours, -1, (0, 255, 0), 5)
    cv2.imshow("img_edge",img_contour)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


gazouseisei()
rinnkaku()
