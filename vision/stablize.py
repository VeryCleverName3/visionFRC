from vidgear.gears.stabilizer import Stabilizer
import cv2

stream = cv2.VideoCapture(0) #Open any video stream such as live webcam video stream on first index(i.e. 0) device

stab = Stabilizer() #initiate stabilizer object with default parameters

# infinite loop
while True:
	
	# read frames
	(grabbed, frame) = stream.read()

	# check if frame empty
	if not grabbed:
		#if True break the infinite loop
		break
		
	#send current frame to stabilizer for processing
	stabilized_frame = stab.stabilize(frame)
		
	#hack for stabilizer which is still initializing
	if stabilized_frame is None:
		#wait till initialization is not completed
		continue 

	#do something with stabilized frame here
	   
	# Show output window
	cv2.imshow("Stabilized Frame", stabilized_frame)

	key = cv2.waitKey(1) & 0xFF
	# check for 'q' key-press
	if key == ord("q"):
		#if 'q' key-pressed break out
		break

cv2.destroyAllWindows()
# close output window
#clear stabilizer resources
stab.clean()
# safely close video stream
stream.release()