import glob
import cv2
from PIL import Image

for i in range(1,63):
	if i<10:
		location = '/home/pratik/Documents/restaurant-menu-ocr/English/Fnt/Sample00' + str(i)
	else:
		location = '/home/pratik/Documents/restaurant-menu-ocr/English/Fnt/Sample0' + str(i)
	

	files = glob.glob(location+'/*')

	for(idx,image) in enumerate(files):
		img = cv2.imread(image)
		img = cv2.resize(img,(28,28))

		im = Image.fromarray(img)

		im.save('test_data/sample' + str(i) + '/' + str(idx) + '.png')