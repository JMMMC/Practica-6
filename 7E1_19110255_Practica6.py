import cv2
import numpy as np

# HSV – RGB – YUV

def Impresion(namme,imagen,x,y):
    cv2.namedWindow(namme)
    cv2.moveWindow(namme, x,y)
    cv2.imshow(namme, imagen)
    
def Rango(imagen,lower,upper):
    lower = np.array(lower)
    upper = np.array(upper)
    mask = cv2.inRange(imagen, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    return (mask,res)
    
cap = cv2.VideoCapture('RAfrodita.mp4')


while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_hsv,res_hsv = Rango(hsv,[0,150,50],[255,255,180])
        Impresion('mask hsv',mask_hsv,550,10)
        Impresion('res hsv',res_hsv,1050,10)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mask_rgb,res_rgb = Rango(rgb,[219, 20, 114],[255, 240, 245])
        Impresion('frame rgb',frame,50,270)
        Impresion('mask rgb',mask_rgb,550,270)
        Impresion('res rgb',res_rgb,1050,270)

        yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        mask_yuv,res_yuv = Rango(yuv,[0,150,50],[255,255,180])
        Impresion('mask yuv',mask_yuv,550,550)
        Impresion('res yuv',res_yuv,1050,550)
        
        if cv2.waitKey(30) == ord('s'):
            break
    else: break

cv2.destroyAllWindows()
cap.release()
