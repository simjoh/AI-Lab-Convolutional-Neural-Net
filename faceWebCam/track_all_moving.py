import cv2
import numpy as np
import imutils
def main():
   cap=cv2.VideoCapture(0)
   
   if cap.isOpened():
      ret, frame = cap.read()

   else:
      ret = False

   ret, frame1 = cap.read()
   ret, frame2 = cap.read()

   while ret:
      ret, frame = cap.read()

      d = cv2.absdiff(frame1, frame2)

      grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

      blur = cv2.GaussianBlur(grey, (5, 5), 0)
      ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
      dilated = cv2.dilate(th, np.ones((8, 8), np.uint8), iterations=3)
      cnts = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      cnts = imutils.grab_contours(cnts)
      #print(th)
      #cv2.drawContours(frame1, cnts, -1, (0, 255, 0), 2)
      cv2.imshow("TH", th)
      cv2.imshow("Grey", grey)
      cv2.imshow("Blur", blur)
      cv2.imshow("Inter", frame1)
      for c in cnts:
         # compute the center of the contour
         M = cv2.moments(c)
         cX = int(M["m10"] / M["m00"])
         cY = int(M["m01"] / M["m00"])
       
         # draw the contour and center of the shape on the image
         cv2.drawContours(frame1, [c], -1, (0, 255, 0), 2)
         cv2.circle(frame1, (cX, cY), 7, (255, 255, 255), -1)
         cv2.putText(frame1, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
       
         # show the image
         cv2.imshow("Image", frame1)
      #cv2.waitKey(0)
      if cv2.waitKey(40) == 27:
         break
      frame1 = frame2
      ret, frame2 = cap.read()
   cv2.destroyAllWindows()
   cap.release()
main()