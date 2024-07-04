import cv2
import pickle

cap = cv2.VideoCapture(r'carPark.mp4')

try:
    with open('CarParkPos','rb') as f:
        posList = pickle.load(f)
except:
    posList = []

width, height = 107, 48


def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

    with open('CarParkPos','wb') as f:
        pickle.dump(posList, f)

def runframes():
    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    #img = cv2.imread('D:\Christ\SEMESTER 4\DBMS Project\ParkEase\carParkImg3resize.png')  
        success, img = cap.read() 
        for pos in posList:
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height),(255,0,255),2)
    #cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)
    #cv2.namedWindow('Image')  # create named window before callback
        cv2.imshow("Image",img)
        cv2.setMouseCallback("Image", mouseClick)
        keyCode = cv2.waitKey(1)
        if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) <1:
            break
