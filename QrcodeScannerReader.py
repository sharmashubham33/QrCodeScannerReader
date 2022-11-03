# QR CODE GENERATOR AND SCANNER
from pyzbar.pyzbar import decode
import pyqrcode
import cv2    # use to open camera
from PIL import ImageTk
import PIL.Image
import io



n=input("Enter 1 to create Qr Code \n\nEnter 2 to Scan Qr Code  ")
n=int(n)

if(n==1):
    n1 = input("Enter the string which you want to convert into QR Code   ")
    qr = pyqrcode.create(n1)
    qr.png("myqrcode.png" ,scale=8)
elif(n==2):
    flag=0
    capture = cv2.VideoCapture(0)
    while True:
        _, frame = capture.read()

        decoded_data = decode(frame)
        try:
            data = decoded_data[0]
            if(flag==0):
                print(data.data.decode('ascii'))
                flag=1
        except:
            pass
        cv2.imshow("QR Code Scanner" , frame)
        
        key = cv2.waitKey(1)

        if(key == ord('q')):
            break
