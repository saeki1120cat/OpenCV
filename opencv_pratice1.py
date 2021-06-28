import numpy as np
import cv2
import dlib

start_frame1 = 0
end_frame1 = 250 
end_frame2 = 400 
end_frame3 = 600
end_frame4 = 700
end_frame5 = 900
 
reader = cv2.VideoCapture('./video/Alec_Baldwin.mp4')

bs = cv2.createBackgroundSubtractorKNN(detectShadows=True) #knn
detector = dlib.get_frontal_face_detector()          # Dlib 的人臉偵測器
fgbg = cv2.createBackgroundSubtractorMOG2(history=200, detectShadows = True) #(MOG2)高斯混合模型分離演算法,MOG的改進演算法 Geometric Multigid

writer = cv2.VideoWriter('./video/opencv_homework.mp4', 
              cv2.VideoWriter_fourcc('I', '4', '2', '0'),
              30, # fps
              (int(reader.get(cv2.CAP_PROP_FRAME_WIDTH)),int(reader.get(cv2.CAP_PROP_FRAME_HEIGHT)))) # resolution
 
print(reader.isOpened())


count = 0
while True:
    ret, frame = reader.read()
    count += 1
    if count>= start_frame1 and count<= end_frame1:
        cv2.waitKey(1)
        fg_mask1 = bs.apply(frame)
        cv2.putText(fg_mask1,'K-Nearest(KNN)',(10,80),cv2.FONT_HERSHEY_COMPLEX,2,(230,225,240),3)
        writer.write(fg_mask1)
        
    if count> end_frame1 and count<= end_frame2:
        cv2.waitKey(1)
        cv2.putText(frame,'original',(10,80),cv2.FONT_HERSHEY_COMPLEX,2,(230,225,240),3)
        writer.write(frame)
        
    if count> end_frame2 and count<= end_frame3:
        cv2.waitKey(1)
        if ret :
            face_rects, scores, idx = detector.run(frame, 0, -.5)  # 偵測人臉

            for i, d in enumerate(face_rects):               # 取出所有偵測的結果
                x1 = d.left(); y1 = d.top(); x2 = d.right(); y2 = d.bottom()
                text = f'{scores[i]:.2f}, ({idx[i]:0.0f})'

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA) # 以方框標示偵測的人臉
                cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,          # 標示分數
                            0.7, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame,'DLib',(10,80),cv2.FONT_HERSHEY_COMPLEX,2,(230,225,240),3)
            writer.write(frame)   
            
    if count> end_frame3 and count<= end_frame4:
        cv2.waitKey(1)
        fg_mask2 = fgbg.apply(frame)
        cv2.putText(fg_mask2,'MOG2',(10,80),cv2.FONT_HERSHEY_COMPLEX,2,(230,225,240),3)
        writer.write(fg_mask2)
        
    if count> end_frame4 and count<= end_frame5:
        cv2.waitKey(1)
        frame1 = cv2.flip(frame, 1)   # left side right
        if ret :
            face_rects, scores, idx = detector.run(frame1, 0, -.5)  # 偵測人臉

            for i, d in enumerate(face_rects):               # 取出所有偵測的結果
                x1 = d.left(); y1 = d.top(); x2 = d.right(); y2 = d.bottom()
                text = f'{scores[i]:.2f}, ({idx[i]:0.0f})'

                cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA) # 以方框標示偵測的人臉
                cv2.putText(frame1, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,          # 標示分數
                            0.7, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame1,'Use DLib and left side right',(10,580),cv2.FONT_HERSHEY_COMPLEX,2,(230,225,240),3)
            writer.write(frame1)  
            
    if count>end_frame5:
        print('completely!')
        break
 
 
writer.release()
reader.release()
cv2.destroyAllWindows()
