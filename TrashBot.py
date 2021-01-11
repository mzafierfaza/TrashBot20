import cv2
import numpy as np
import serial
import time
import defTrackbar as dt

cap = cv2.VideoCapture(1)


dt.CoklatTrackbar(19,232,71)
dt.HijauTrackbar(43,148,119)
dt.BiruTrackbar(0,0,0)
dt.UnguTrackbar(144,155,22)
minRadius = 150
warna = {
    'merah':0,
    'orange':0,
    'coklat':0,
    'hijau':0,
    'biru':0,
    'ungu':0
    }

while True:
    _,frame = cap.read()
    dt.RacikCoklat(frame)
    dt.RacikHijau(frame)
    dt.RacikBiru(frame)
    dt.RacikUngu(frame)
    blynk.run()    
    mask = cv2.bitwise_or(dt.coklat,dt.hijau,dt.biru,dt.ungu)
   data = arduino.readline().decode("UTF-8")
   if data.startswith('A') :
       warna.update({"merah":1,"orange":0,"coklat":0,"hijau":0,"biru":0,"ungu":0})
   elif data.startswith('B'):
       warna.update({"merah":0,"orange":1,"coklat":0,"hijau":0,"biru":0,"ungu":0})
   elif data.startswith('C'):
       warna.update({"merah":0,"orange":0,"coklat":1,"hijau":0,"biru":0,"ungu":0})
   elif data.startswith('D'):
       warna.update({"merah":0,"orange":0,"coklat":0,"hijau":1,"biru":0,"ungu":0})
   elif data.startswith('E'):
       warna.update({"merah":0,"orange":0,"coklat":0,"hijau":0,"biru":1,"ungu":0})
   elif data.startswith('F'):
       warna.update({"merah":0,"orange":0,"coklat":0,"hijau":0,"biru":0,"ungu":1})
   elif data.startswith('S'):
       warna.update({"merah":0,"orange":0,"coklat":0,"hijau":0,"biru":0,"ungu":0})    
   print(warna)    
  

    ## ------ Coklat --------
    contours = cv2.findContours(dt.coklat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(contours) > 0:
        area = max(contours, key = cv2.contourArea)
        approx = cv2.approxPolyDP(area, 0.02*cv2.arcLength(area, True), True)
        ((x, y), radius) = cv2.minEnclosingCircle(area)
        xx = int(x)
        yy = int(y)
        pusat_str = (int(x) - 35, int(y) + 15)
        koordinat_str = ("(" + str(int(x)) + "," + str(int(y)) + ")")

        if area is not None:
            cv2.putText(frame, koordinat_str, pusat_str,cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            cv2.drawContours(frame, [approx], 0, (0, 167, 255), 3)
            cv2.circle(frame, (int(x),int(y)), int(radius), (255,255,255), 2)
            if len(approx) == 3:
                cv2.putText(frame, "Segitiga Kuning", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),2)
                if radius > minRadius:
                    cv2.putText(frame, "Segitiga Kuning", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255),2)
##                    arduino.write(str.encode('S'))    #berhenti di Merah kalo ketemu

    ## ------ Hijau --------
    contours = cv2.findContours(dt.hijau, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(contours) > 0:
        area = max(contours, key = cv2.contourArea)
        approx = cv2.approxPolyDP(area, 0.02*cv2.arcLength(area, True), True)
        ((x, y), radius) = cv2.minEnclosingCircle(area)
        xx = int(x)
        yy = int(y)
        pusat_str = (int(x) - 35, int(y) + 15)
        koordinat_str = ("(" + str(int(x)) + "," + str(int(y)) + ")")

        if area is not None:
            cv2.putText(frame, koordinat_str, pusat_str,cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            cv2.drawContours(frame, [approx], 0, (0, 167, 255), 3)
            cv2.circle(frame, (int(x),int(y)), int(radius), (255,255,255), 2)

            if len(approx) == 3:
                cv2.putText(frame, "Segitiga Hijau", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),2)
                if radius > minRadius:
                    cv2.putText(frame, "Segitiga Hijau", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),2)
##                    arduino.write(str.encode('S'))    #berhenti di Merah kalo ketemu

    ## ------ Biru --------
    contours = cv2.findContours(dt.biru, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(contours) > 0:
        area = max(contours, key = cv2.contourArea)
        approx = cv2.approxPolyDP(area, 0.02*cv2.arcLength(area, True), True)
        ((x, y), radius) = cv2.minEnclosingCircle(area)
        xx = int(x)
        yy = int(y)
        pusat_str = (int(x) - 35, int(y) + 15)
        koordinat_str = ("(" + str(int(x)) + "," + str(int(y)) + ")")

        if area is not None:
            cv2.putText(frame, koordinat_str, pusat_str,cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            cv2.drawContours(frame, [approx], 0, (0, 167, 255), 3)
            cv2.circle(frame, (int(x),int(y)), int(radius), (255,255,255), 2)

            if len(approx) == 3:
                cv2.putText(frame, "Segitiga Biru", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),2)
                if radius > minRadius:
                    cv2.putText(frame, "Segitiga Biru", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0),2)
##                    arduino.write(str.encode('S'))    #berhenti di Merah kalo ketemu

    ## ------ Ungu --------
    contours = cv2.findContours(dt.ungu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(contours) > 0:
        area = max(contours, key = cv2.contourArea)
        approx = cv2.approxPolyDP(area, 0.02*cv2.arcLength(area, True), True)
        ((x, y), radius) = cv2.minEnclosingCircle(area)
        xx = int(x)
        yy = int(y)
        pusat_str = (int(x) - 35, int(y) + 15)
        koordinat_str = ("(" + str(int(x)) + "," + str(int(y)) + ")")

        if area is not None:
            cv2.putText(frame, koordinat_str, pusat_str,cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            cv2.drawContours(frame, [approx], 0, (0, 167, 255), 3)
            cv2.circle(frame, (int(x),int(y)), int(radius), (255,255,255), 2)
            if len(approx) == 3:
                cv2.putText(frame, "Segitiga Ungu", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),2)
                if radius > minRadius:
                    cv2.putText(frame, "Segitiga Ungu", (xx, yy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 188),2)
##                    arduino.write(str.encode('S'))    #berhenti di Merah kalo ketemu
##
##    else:
##        print('Tidak ada Warna')
        
    cv2.imshow("frame", frame)
##    cv2.imshow("mask", mask)
##    cv2.imshow("MERAH", dt.merah)
    cv2.imshow("HIJAU", dt.hijau)
##    cv2.imshow("ORANGE", dt.orange)
    cv2.imshow("COKLAT", dt.coklat)
    cv2.imshow("BIRU", dt.biru)
    cv2.imshow("UNGU", dt.ungu)
##
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
