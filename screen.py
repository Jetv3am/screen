import subprocess
import numpy as np
import cv2
import multiprocessing
import time as time

def take_screenshot(output, index):
    # Run the screencapture command and save the output to a file
    subprocess.call(["screencapture", "-x", "screenshot{}.png".format(index)])
    
    # Read the image file using OpenCV
    img = cv2.imread("screenshot{}.png".format(index))
    
    # Convert the image to RGB format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Store the image in the output array
    output[index] = img

# Set up the multiprocessing pool
num_processes = 4
pool = multiprocessing.Pool(num_processes)

# Set up the output array
output = multiprocessing.Array('i', [0] * num_processes)

# Take screenshots in parallel
for i in range(num_processes):
    pool.apply_async(take_screenshot, args=(output, i))

# Set up an infinite loop to merge the screenshots
while True:
    # Check if all the processes have finished
    if all(result.ready() for result in pool._cache):
        break
    
    # Wait for a short period of time before checking again
    time.sleep(0.1)

# Merge the screenshots into a single image
merged_image = np.vstack([np.hstack(output[i::num_processes]) for i in range(num_processes)])

# Display the merged image
cv2.imshow("Screenshot", merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




