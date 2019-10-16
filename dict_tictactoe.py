Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-reg-oct/google_images.py ==

Item no.: 1 --> Item name = supercar
Evaluating...
Starting Download...
Image URL: https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/body-image/public/mclaren-720s_0.jpg?itok=wZbSZ3FZ
Completed Image ====> 1.mclaren-720s_0.jpg
Image URL: https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/car-reviews/first-drives/legacy/huracan-evo-.jpg?itok=jPfZUNel
Completed Image ====> 2.huracan-evo-.jpg
Image URL: https://cdn.carbuzz.com/gallery-images/840x560/525000/800/525840.jpg
Completed Image ====> 3.525840.jpg
Image URL: https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/body-image/public/ferrari_f8_tributo.jpg?itok=1TG8_Tnx
Completed Image ====> 4.ferrari_f8_tributo.jpg
Image URL: https://www.jamesedition.com/stories/wp-content/uploads/2018/12/Koenigsegg-Regera-prototype-front-three-quarter-03.jpg
Completed Image ====> 5.Koenigsegg-Regera-prototype-front-three-quarter-03.jpg
Image URL: https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/car-reviews/first-drives/legacy/svj_1.jpg?itok=-jWUc7am
Completed Image ====> 6.svj_1.jpg
Image URL: https://robbreportedit.files.wordpress.com/2019/09/sian01.jpg?w=1000
Completed Image ====> 7.sian01.jpg
Image URL: https://d32z17rjnv32pv.cloudfront.net/wp-content/uploads/2018/11/05165117/Lamborghini_SC18_Gaadi.jpg
Completed Image ====> 8.Lamborghini_SC18_Gaadi.jpg
Image URL: http://images.summitmedia-digital.com/esquiremagph/images/2019/06/13/BEST-SUPER-CAR-BRANDS-MAIN.jpg
Completed Image ====> 9.BEST-SUPER-CAR-BRANDS-MAIN.jpg
Image URL: https://img-ik.cars.co.za/images/2019/7/BMWSuperOP/tr:n-news_large/bmw-vision-m-next-concept.jpg
Completed Image ====> 10.bmw-vision-m-next-concept.jpg

Errors: 0



Item no.: 1 --> Item name = burj khalifa
Evaluating...
Starting Download...
Image URL: https://cdn.getyourguide.com/img/location_img-2703-1061214306-148.jpg
Completed Image ====> 1.location_img-2703-1061214306-148.jpg
Image URL: https://images.khaleejtimes.com/storyimage/KT/20190104/ARTICLE/170709664/AR/0/AR-170709664.jpg&MaxW=780&imageVersion=16by9&NCS_modified=&exif=.jpg
Completed Image ====> 2.AR-170709664.jpg
Image URL: https://media.tacdn.com/media/attractions-splice-spp-674x446/07/be/ec/eb.jpg
Completed Image ====> 3.eb.jpg
Image URL: https://tripxtours.imgix.net/uploads/dubai_tours/b39f6c9769e45e1f265b549494511758.jpg?auto=compress&w=2000&h=1500&crop=faces&fit=min
Completed Image ====> 4.b39f6c9769e45e1f265b549494511758.jpg
Image URL: https://imagevars.gulfnews.com/2019/08/16/190816-india-pakistan-flag_16c9b626f73_large.jpg
Completed Image ====> 5.190816-india-pakistan-flag_16c9b626f73_large.jpg
Image URL: https://images2.minutemediacdn.com/image/upload/c_crop,h_1192,w_2123,x_0,y_70/f_auto,q_auto,w_1100/v1559225783/shape/mentalfloss/584459-istock-183342824.jpg
Completed Image ====> 6.584459-istock-183342824.jpg
Image URL: https://d2v9ipibika81v.cloudfront.net/uploads/sites/254/GOPR0128-1140x684.jpg
Completed Image ====> 7.GOPR0128-1140x684.jpg
Image URL: https://mediastream.jumeirah.com/webimage/image1152x648//globalassets/global/hotels-and-resorts/dubai/burj-al-arab/homepage-audit/burj-al-arab-jumeirah-terrace-hero.jpg
Completed Image ====> 8.burj-al-arab-jumeirah-terrace-hero.jpg
Image URL: https://media.tacdn.com/media/attractions-splice-spp-674x446/07/74/81/8c.jpg
Completed Image ====> 9.8c.jpg
Image URL: https://images.musement.com/cover/0002/95/thumb_194286_cover_header.jpeg?w=1200&h=630&q=60&fit=crop
Wrong image format returned. Skipping...
Image URL: https://img.jakpost.net/c/2019/05/08/2019_05_08_71775_1557305219._large.jpg
Completed Image ====> 10.2019_05_08_71775_1557305219._large.jpg

Errors: 1


>>> from urllib.request import urlretrieve
>>> urlretrieve('https://imdb-video.media-imdb.com/vi436517913/1434659607842-pgv4ql-1563245147713.mp4?Expires=1571312620&Signature=XBLdHe41ucM3himo1q~ZIFnORJ5HSxrerp7mmnC~Ykle-iB-2jhwKfUH42L20mYtx4rB54zeOKr0X45F1VO0rMTpw4LKkQFgCluK5r6-4fHgkHnrnCghJAppGCrl9pEschCp8CfjEeil76yE5X8o7-0xVovs9trqs-1do4IT4a26bwqBsTRclAH-xSQmYFQTYv63PuWuBxAm8M9xq2uuDbenvA12tGxO66EaqOB8uPtrBGBxd5qnx2nOXhN1V-QhotoJAuX4b85MHqil7GrzaTLQQ9XNfB1yXbrAVob8MxdYDenRn5zM-mOcR9PnyK1-X~czW0CvfqFYK8RdtZLowQ__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA', 'imdb_video.mp4')
('imdb_video.mp4', <http.client.HTTPMessage object at 0x1077b9908>)
>>> from urllib.request import *
>>> from bs4 import BeautifulSoup as bs
>>> res = urlopen('https://www.imdb.com/title/tt7430722/?ref_=fn_al_tt_1')
>>> html = bs(res)

Warning (from warnings module):
  File "/Users/anmolrajarora/Documents/python-reg-oct/google_images.py", line 1
    # importing google_images_download module
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file /Users/anmolrajarora/Documents/python-reg-oct/google_images.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.

>>> #html = bs(res, 'lxml')
>>> 
>>> images = html.find_all('img')
>>> for i in range(len(images)):
	src = images[i]['src']
	extension = src.rpartition('.')[-1]
	if extension == 'jpg':
		urlretrieve(src, 'img_{}.{}'.format(i + 1, extension))

		
('img_3.jpg', <http.client.HTTPMessage object at 0x1088b1908>)
('img_4.jpg', <http.client.HTTPMessage object at 0x1088b1630>)
('img_7.jpg', <http.client.HTTPMessage object at 0x1088b14e0>)
('img_20.jpg', <http.client.HTTPMessage object at 0x1088b1a90>)
('img_21.jpg', <http.client.HTTPMessage object at 0x1088b1898>)
('img_22.jpg', <http.client.HTTPMessage object at 0x1088b1940>)
('img_23.jpg', <http.client.HTTPMessage object at 0x1088b1668>)
('img_24.jpg', <http.client.HTTPMessage object at 0x1088b1710>)
('img_25.jpg', <http.client.HTTPMessage object at 0x1088b1978>)
('img_26.jpg', <http.client.HTTPMessage object at 0x1088b1860>)
('img_27.jpg', <http.client.HTTPMessage object at 0x1088b1630>)
('img_28.jpg', <http.client.HTTPMessage object at 0x1088b1ba8>)
('img_79.jpg', <http.client.HTTPMessage object at 0x1088b1a90>)
('img_80.jpg', <http.client.HTTPMessage object at 0x1088b1a58>)
('img_81.jpg', <http.client.HTTPMessage object at 0x1088b1cf8>)
('img_84.jpg', <http.client.HTTPMessage object at 0x1088b1860>)
('img_87.jpg', <http.client.HTTPMessage object at 0x1088b17f0>)
('img_90.jpg', <http.client.HTTPMessage object at 0x1088b15f8>)
('img_93.jpg', <http.client.HTTPMessage object at 0x1088b1c88>)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
''')

{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}

>>> 
>>> gamePositions = [1,2,3,4,5,6,7,8,9]
>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3], gamePositions[4], gamePositions[5], gamePositions[6], gamePositions[7], gamePositions[8]))

1 | 2 | 3
------------
4 | 5 | 6
------------
7 | 8 | 9

>>> userInput = input("Enter the position where you want to put X: ")
Enter the position where you want to put X: 5
>>> userInput = int(input("Enter the position where you want to put X: "))
Enter the position where you want to put X: 5
>>> userInput -= 1
>>> userInput
4
>>> gamePositions[userInput] = 'X'
>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3], gamePositions[4], gamePositions[5], gamePositions[6], gamePositions[7], gamePositions[8]))

1 | 2 | 3
------------
4 | X | 6
------------
7 | 8 | 9

>>> 
>>> 
>>> 
>>> # list - > [] , immutable
>>> # list - > [] , mutable
>>> # tuple - > () , immutable
>>> # set,frozen set -> {}  , mutable(set), immutable(frozen)
>>> # dictionary -> {}
>>> # set vs dictionary  -> random elements(set, no indexing, no keys), key-value (dict, immutable)
>>> 
>>> student = {
	1: 'abc'
	}
>>> student
{1: 'abc'}
>>> student = {
	'1': 'abc'
	}
>>> student
{'1': 'abc'}
>>> 
>>> student = {
	'id': 101,
	'name' : 'Ram',
	'contact' : '1234',
	'address' : 'delhi'
	}
>>> 
>>> student['id']
101
>>> student['name']
'Ram'
>>> student = {
	'id': 101,
	'name' : 'Ram',
	'contact' : '1234',
	'address' : ['delhi', 'gurgaon']
	}
>>> student['address']
['delhi', 'gurgaon']
>>> student['address'][0]
'delhi'
>>> student = {
	'id': 101,
	'name' : 'Ram',
	'contact' : {
		'student_no': '1234',
		'father_no': '4567'
		}
	'address' : ['delhi', 'gurgaon']
	}
SyntaxError: invalid syntax
>>> student = {
	'id': 101,
	'name' : 'Ram',
	'contact' : {
		'student_no': '1234',
		'father_no': '4567'
		},
	'address' : ['delhi', 'gurgaon']
	}
>>> student = {
	'id': 101,
	'name' : 'Ram',
	'address' : ['delhi', 'gurgaon'],
	'contact' : {
		'student_no': '1234',
		'father_no': '4567'
		}
	}
>>> student
{'id': 101, 'name': 'Ram', 'address': ['delhi', 'gurgaon'], 'contact': {'student_no': '1234', 'father_no': '4567'}}
>>> student['contact']
{'student_no': '1234', 'father_no': '4567'}
>>> student['contact']['father_no']
'4567'
>>> 
>>> 
>>> 
>>> userid = 'Ram'
>>> email = 'ram@gmail.com
SyntaxError: EOL while scanning string literal
>>> email = 'ram@gmail.com'
>>> password = '1234'
>>> 
>>> 
>>> user = {}
>>> user['userid'] = userid
>>> user['email'] = email
>>> user['password'] = password
>>> user
{'userid': 'Ram', 'email': 'ram@gmail.com', 'password': '1234'}
>>> users = []
>>> users.append(user)
>>> users
[{'userid': 'Ram', 'email': 'ram@gmail.com', 'password': '1234'}]
>>> userid = 'Ram2'
>>> email = 'ram2@gmail.com'
>>> password = '12345'
>>> user = {}
>>> user['userid'] = userid
>>> user['email'] = email
>>> user['password'] = password
>>> users.append(user)
>>> users
[{'userid': 'Ram', 'email': 'ram@gmail.com', 'password': '1234'}, {'userid': 'Ram2', 'email': 'ram2@gmail.com', 'password': '12345'}]
>>> 
>>> 
>>> student
{'id': 101, 'name': 'Ram', 'address': ['delhi', 'gurgaon'], 'contact': {'student_no': '1234', 'father_no': '4567'}}
>>> for key in student:
	print(key)

	
id
name
address
contact
>>> for key in student:
	print(student[key])

	
101
Ram
['delhi', 'gurgaon']
{'student_no': '1234', 'father_no': '4567'}
>>> for value in student.values():
	print(value)

	
101
Ram
['delhi', 'gurgaon']
{'student_no': '1234', 'father_no': '4567'}
>>> 
>>> student.keys()
dict_keys(['id', 'name', 'address', 'contact'])
>>> student.values()
dict_values([101, 'Ram', ['delhi', 'gurgaon'], {'student_no': '1234', 'father_no': '4567'}])
>>> 
>>> for user in users:
	if 'shyam@gmail.com' == user['email']:
		if '12345' == user['password']:
			print('Login successful')
	else:
		print('Email not found')

		
Email not found
Email not found
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
 
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
 
if args.get("video", None) is None:
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
 
else:
	vs = cv2.VideoCapture(args["video"])
 
firstFrame = None
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	text = "Unoccupied"
 
	
	if frame is None:
		break
 
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
		if firstFrame is None:
		firstFrame = gray
		continue
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
 
	

	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
 

	for c in cnts:
		
		if cv2.contourArea(c) < args["min_area"]:
			continue
 
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"

	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 
	
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF
 
	if key == ord("q"):
		break
 
vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()
