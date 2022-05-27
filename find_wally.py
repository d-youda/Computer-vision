import cv2

#wally와 wally를 찾을 영상 가져오기
src = cv2.imread('find_wally.jpg')
wally = cv2.imread('wally.png')

#cv2.imshow('wally',wally)
#cv2.imshow('src',src)
#cv2.waitKey()
#cv2.destroyAllWindows()

#CCOEFF_NORMED가지고 객체 검출
res = cv2.matchTemplate(src,wally,cv2.TM_CCOEFF_NORMED)
#res_norm = cv2.normalize(res,None,0,255,cv2.NORM_MINMAX,cv2.CV_8U)

minv , maxv, minloc, maxloc =cv2.minMaxLoc(res)
print('maxv',maxv)
print('maxloc',maxloc)

wh , ww = wally.shape[:2]
#dst = cv2.cvtColor(src,cv2.COLOR_GRAY2BGR)
cv2.rectangle(src,maxloc,(maxloc[0]+ww,maxloc[1]+wh),(255,0,0),2)

cv2.imshow('res',res)
cv2.imshow('dst',src)
cv2.waitKey()
cv2.destroyAllWindows()
