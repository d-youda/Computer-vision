import cv2
src = cv2.imread('mypicture.jpg')
batmask = cv2.imread('batmask.png',cv2.IMREAD_UNCHANGED)

#얼굴 검출 및 눈 검출을 위한 학습 데이터 가져오기
face_class = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_class = cv2.CascadeClassifier('haarcascade_eye.xml')

#유효한 학습 데이터인지 확인하기
if face_class.empty():
    print("XML file error")

#멀티스케일 통해 얼굴 검출
faces = face_class.detectMultiScale(src)
#눈 검출 위해 얼굴 위치 지정
for(x,y,w,h) in faces:
    faceROI = src[y:y + h // 2, x:x + w]

#멀티 스케일 통해 눈 검출
eyes = eye_class.detectMultiScale(faceROI)
for (x2,y2,w2,h2) in eyes:
   print("eyes:",x2,y2,w2,h2)

#mask 위치 찾기
mask_size = int(src.shape[1]/5)
x_pos = int(src.shape[1]/38)
y_pos = int(src.shape[1]/7)

#alpha채널 추가 후 두 사진 사이즈 맞추기
src = cv2.cvtColor(src,cv2.COLOR_BGR2BGRA)
batmask = cv2.resize(batmask,(w,h))
w, h, c = batmask.shape

#batmask 사진에 씌우기
for i in range(0,w):
    for j in range(0,h):
        if batmask[i,j][3] !=0:
            src[y-y_pos+i,x-x_pos+j] = batmask[i,j]

cv2.imshow('src',src)
cv2.waitKey()
cv2.destroyAllWindows()
