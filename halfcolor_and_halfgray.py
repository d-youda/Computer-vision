import cv2
import numpy as np #배열을 사용하기 위해 numpy를 받아옵니다.

imgBGR = cv2.imread('./lena.bmp')
h,w,c = imgBGR.shape

imgGRAY = imgBGR[0:512,0:256,0] #반쪽짜리 회색
imgGRAY_3 = cv2.cvtColor(imgGRAY, cv2.COLOR_GRAY2BGR) #흑백사진 채널 3게로 변경

imgColor = imgBGR[0:512,256:512,:] #색깔있는 반쪽

imgFinal = np.hstack((imgGRAY_3,imgColor)) # 두 개를 합쳐요!

cv2.imshow('imgBGR',imgFinal)
cv2.waitKey()
cv2.destroyAllWindows()
