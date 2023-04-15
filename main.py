# import subprocess
# import cv2 as cv
# from time import time
# import multiprocessing as mp 




"""
MacOS Commandline Screenshot Method 3-4 FPS and 0.2 seconds per frame 
"""
# while True:
#     loop_time = time()
#     # Execute the screencapture command and capture the output
#     output = subprocess.check_output(["screencapture","-x","screenshot.png"]) 
#     #Reads the output and coverts binary to nparray that can be readable by cv 
#     img = cv.imread("screenshot.png")  
    
#     #Prints out FPS and displays the screen image  
#     # print('This frame takes {} seconds.'.format(time()-loop_time))
#     print('FPS{}'.format(1/(time()-loop_time)))
#     cv.imshow("test",img)  
#     loop_time = time()

#     #Ends the loop 
#     if cv.waitKey(25) & 0xFF == ord('q'):
#         cv.destroyAllWindows()
#         break 



"""
MSS 18 frames per second 0.06 seconds per frame 
"""
# from mss import mss
# import cv2
# from PIL import Image
# import numpy as np
# from time import time

# mon = {'top': 100, 'left':200, 'width':1600, 'height':1024}

# sct = mss()

# while 1:
#     begin_time = time()
#     sct_img = sct.grab(mon)
#     img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
#     img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#     print('FPS{}'.format(1/(time()-begin_time)))
#     cv2.imshow('test', np.array(img_bgr))
#     print('This frame takes {} seconds.'.format(time()-begin_time))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break

"""
MSS version.2  22 FPS 
""" 
# import mss
# from PIL import Image, ImageGrab
# import pyautogui

# import cv2 as cv
# import numpy as np
# import time

# w, h = pyautogui.size()
# print("PIL Screen Capture Speed Test")
# print("Screen Resolution: " + str(w) + 'x' + str(h))

# img = None
# t0 = time.time()
# n_frames = 1
# monitor = {"top": 0, "left": 0, "width": w, "height": h}
# with mss.mss() as sct:
#     while True:
#         img = sct.grab(monitor=monitor)
#         img = np.array(img)                         # Convert to NumPy array
#         # img = cv.cvtColor(img, cv.COLOR_RGB2BGR)  # Convert RGB to BGR color
        
#         small = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
#         cv.imshow("Computer Vision", small)

#         # Break loop and end test
#         key = cv.waitKey(1)
#         if key == ord('q'):
#             break
        
#         elapsed_time = time.time() - t0
#         avg_fps = (n_frames / elapsed_time)
#         print("Average FPS: " + str(avg_fps))
#         n_frames += 1
