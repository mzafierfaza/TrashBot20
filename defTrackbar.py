import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Merah dan Orange')
cv2.namedWindow('Coklat dan Hijau')
cv2.namedWindow('Biru dan Ungu')

def MerahTrackbar(H_min,S_min,V_min):
    maximum = 255
    cv2.createTrackbar('H_Merah','Merah dan Orange',H_min,maximum,nothing)
    cv2.createTrackbar('S_Merah','Merah dan Orange',S_min,maximum,nothing)
    cv2.createTrackbar('V_Merah','Merah dan Orange',V_min,maximum,nothing)

def OrangeTrackbar(H_min,S_min,V_min):
    maximum = 255
    cv2.createTrackbar('H_Orange','Merah dan Orange',H_min,maximum,nothing)
    cv2.createTrackbar('S_Orange','Merah dan Orange',S_min,maximum,nothing)
    cv2.createTrackbar('V_Orange','Merah dan Orange',V_min,maximum,nothing)

def CoklatTrackbar(H_min,S_min,V_min):
    maximum = 255
    cv2.createTrackbar('H_Coklat','Coklat dan Hijau',H_min,maximum,nothing)
    cv2.createTrackbar('S_Coklat','Coklat dan Hijau',S_min,maximum,nothing)
    cv2.createTrackbar('V_Coklat','Coklat dan Hijau',V_min,maximum,nothing)

def HijauTrackbar(H_min,S_min,V_min):
    maximum = 255
    cv2.createTrackbar('H_Hijau','Coklat dan Hijau',H_min,maximum,nothing)
    cv2.createTrackbar('S_Hijau','Coklat dan Hijau',S_min,maximum,nothing)
    cv2.createTrackbar('V_Hijau','Coklat dan Hijau',V_min,maximum,nothing)

def BiruTrackbar(H_min,S_min,V_min):
    maximum = 255
    cv2.createTrackbar('H_Biru','Biru dan Ungu',H_min,maximum,nothing)
    cv2.createTrackbar('S_Biru','Biru dan Ungu',S_min,maximum,nothing)
    cv2.createTrackbar('V_Biru','Biru dan Ungu',V_min,maximum,nothing)


def UnguTrackbar(H_min,S_min,V_min):
    maximum = 255
    cv2.createTrackbar('H_Ungu','Biru dan Ungu',H_min,maximum,nothing)
    cv2.createTrackbar('S_Ungu','Biru dan Ungu',S_min,maximum,nothing)
    cv2.createTrackbar('V_Ungu','Biru dan Ungu',V_min,maximum,nothing)

#--------------------------------------------------------------------------
    
def RacikMerah(frame):
    H_merah = cv2.getTrackbarPos('H_Merah','Merah dan Orange')
    S_merah = cv2.getTrackbarPos('S_Merah','Merah dan Orange')
    V_merah = cv2.getTrackbarPos('V_Merah','Merah dan Orange')
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
    global merah
    lowerM = np.array([H_merah,S_merah,V_merah])
    upperM = np.array([31,255,255])
    merah = cv2.inRange(hsv,lowerM,upperM)
    merah = cv2.erode(merah, kernel)
    merah = cv2.morphologyEx(merah, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    merah = cv2.morphologyEx(merah, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    return merah

def RacikOrange(frame):
    H_orange = cv2.getTrackbarPos('H_Orange','Merah dan Orange')
    S_orange = cv2.getTrackbarPos('S_Orange','Merah dan Orange')
    V_orange = cv2.getTrackbarPos('V_Orange','Merah dan Orange')
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    global orange
    lowerO = np.array([H_orange,S_orange,V_orange])
    upperO = np.array([180,255,255])
    orange = cv2.inRange(hsv,lowerO,upperO)
    orange = cv2.erode(orange, kernel)
    orange = cv2.morphologyEx(orange, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    orange = cv2.morphologyEx(orange, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    return orange

def RacikCoklat(frame):
    H_coklat = cv2.getTrackbarPos('H_Coklat','Coklat dan Hijau')
    S_coklat = cv2.getTrackbarPos('S_Coklat','Coklat dan Hijau')
    V_coklat = cv2.getTrackbarPos('V_Coklat','Coklat dan Hijau')
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    global coklat
    lowerC = np.array([H_coklat,S_coklat,V_coklat])
    upperC = np.array([180,255,255])
    coklat = cv2.inRange(hsv,lowerC,upperC)
    coklat = cv2.erode(coklat, kernel)
    coklat = cv2.morphologyEx(coklat, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    coklat = cv2.morphologyEx(coklat, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    return coklat

def RacikHijau(frame):
    H_hijau = cv2.getTrackbarPos('H_Hijau','Coklat dan Hijau')
    S_hijau = cv2.getTrackbarPos('S_Hijau','Coklat dan Hijau')
    V_hijau = cv2.getTrackbarPos('V_Hijau','Coklat dan Hijau')
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    global hijau
    lowerH = np.array([H_hijau,S_hijau,V_hijau])
    upperH = np.array([180,255,255])
    hijau = cv2.inRange(hsv,lowerH,upperH)
    hijau = cv2.erode(hijau, kernel)
    hijau = cv2.morphologyEx(hijau, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    hijau = cv2.morphologyEx(hijau, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    return hijau

def RacikBiru(frame):
    H_biru = cv2.getTrackbarPos('H_Biru','Biru dan Ungu')
    S_biru = cv2.getTrackbarPos('S_Biru','Biru dan Ungu')
    V_biru = cv2.getTrackbarPos('V_Biru','Biru dan Ungu')
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    global biru
    lowerB = np.array([H_biru,S_biru,V_biru])
    upperB = np.array([180,255,255])
    biru = cv2.inRange(hsv,lowerB,upperB)
    biru = cv2.erode(biru, kernel)
    biru = cv2.morphologyEx(biru, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    biru = cv2.morphologyEx(biru, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    return biru

def RacikUngu(frame):
    H_ungu = cv2.getTrackbarPos('H_Ungu','Biru dan Ungu')
    S_ungu = cv2.getTrackbarPos('S_Ungu','Biru dan Ungu')
    V_ungu = cv2.getTrackbarPos('V_Ungu','Biru dan Ungu')
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    global ungu
    lowerU = np.array([H_ungu,S_ungu,V_ungu])
    upperU = np.array([180,255,255])
    ungu = cv2.inRange(hsv,lowerU,upperU)
    ungu = cv2.erode(ungu, kernel)
    ungu = cv2.morphologyEx(ungu, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    ungu = cv2.morphologyEx(ungu, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    return ungu

