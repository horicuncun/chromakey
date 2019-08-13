import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)

embed = cv2.imread("./img/weather.jpg", 1)
cap.set(cv2.CAP_PROP_FPS, 30)  
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
lower_color = np.array([20,20,50])
upper_color = np.array([110,255,255])

dt_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


writer1 = cv2.VideoWriter('./movie_original/' + dt_now +'capture.mov', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
writer2 = cv2.VideoWriter('./movie_chromakey/' + dt_now +'capture.mov', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

while True:
    ret, frame = cap.read()
    writer1.write(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    embed_cut = cv2.bitwise_and(embed, embed, mask= mask)
    mask_not = cv2.bitwise_not(mask)
    frame_cut = cv2.bitwise_and(frame, frame, mask= mask_not)
    overlay = cv2.bitwise_or(embed_cut, frame_cut)
    writer2.write(overlay)

    cv2.imshow('frame', overlay)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer1.release()
writer2.release()
cv2.destroyAllWindows()
