import numpy as np
import cv2
#마우스 클릭값을 저장하기 위한 4X2 행렬
point = np.zeros((4,2),np.float32)
#행렬 값 저장 위치 표시 위한 counter
counter = 0
#입력 영상
src = cv2.imread('warp.jpg')
cv2.namedWindow('src')
w,h = 720,540
#mouseevent 함수 정의
def mouse_event(event,x,y,flags,param):
 global counter,srcQuad,dstQuad
 if event == cv2.EVENT_LBUTTONDOWN:
 # src에서 꼭짓점 값 클릭->좌상 우상 우하 좌하 순서여야 함
 point[counter][0] = x
 point[counter][1] = y
 cv2.circle(src, (x,y), 3, (255, 255, 255), -3)
 cv2.imshow('src',src)
 elif event == cv2.EVENT_LBUTTONUP:
 #좌표값 확인해보기위한 출력
 print("Value :{},{}".format(point[counter][0],point[counter][1]))
 #counter값을 올려 다음 클릭값을 다음 배열에 저장함
 counter = counter + 1
 #값 네 개를 모두 선택했을 때,
 if counter == 4:
 srcQuad = np.array([[point[0][0], point[0][1]], [point[1][0], point[1][1]], 
[point[2][0], point[2][1]],
 [point[3][0], point[3][1]]], dtype=np.float32)
 dstQuad = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], 
dtype=np.float32)
 perspect = cv2.getPerspectiveTransform(srcQuad, dstQuad)
 dst = cv2.warpPerspective(src, perspect, (w, h))
 cv2.imshow('dst', dst)
cv2.imshow('src',src)
cv2.setMouseCallback('src',mouse_event,src)
cv2.waitKey()
cv2.destroyAllWindows()
