import cv2


# initialize the normal camera
vid=cv2.VideoCapture(0)
# initialize the Qrcode detector
detector=cv2.QRCodeDetector()
while True:
    ret,frame=vid.read()

    # first detect the code and decode it
    data,bbox,_=detector.detectAndDecode(frame)

    if bbox is not None:
        if data:
            print(data)

    cv2.imshow("qrdetector",frame)
    if cv2.waitKey(1)==ord("e"):
        break

vid.release()
cv2.destroyAllWindows()


