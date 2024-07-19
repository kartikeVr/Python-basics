import cv2

#select camera 
cap = cv2.VideoCapture(0)

#Run stream in a loop
while True:
    ret,cam = cap.read()
    
    cv2.imshow("camera",cam)
    #Create a key to exit
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#After the loop exists break all the windows
cv2.destroyAllWindows()
