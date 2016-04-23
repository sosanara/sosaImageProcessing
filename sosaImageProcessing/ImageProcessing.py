import cv2
import numpy as np
from PIL import Image
import sys, time

REFERENCE_IMAGE = 'reference/ref.png'

class ImageProcessing:
	INPUT_IMAGE = ""
	SAVE_IMAGE = ""

	def __init__(self, input_image, save_image):
		self.INPUT_IMAGE = input_image
		self.SAVE_IMAGE = save_image
		self.main()

	def main(self):
		img = cv2.imread(self.INPUT_IMAGE)

		img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
		img_binary = self.setPreprocessing(img_YCrCb)

		cv2.imwrite(self.SAVE_IMAGE, img_binary)

		diff_percentage = self.get_image_pixel_similarity(self.SAVE_IMAGE, REFERENCE_IMAGE)

		print 'diff_percentage : ' + str(diff_percentage)

		self.image_matching(diff_percentage)

	def image_matching(self, diff_percentage):

		num = ''
		reference_filename = 'reference/'
		diff_per = ['0.png']
		temp = ''

		if(diff_percentage < 14):
			num = '0/'
			reference_filename += num
			result_file = diff_per[0]
			result_file = reference_filename + result_file
			print result_file
			return result_file

		elif(14 <= diff_percentage < 25):
			num = '1/'
			reference_filename += num

			for i in range(1, 8):
				type = str(i) + '.png'
				diff_per.append(self.get_image_pixel_similarity(self.SAVE_IMAGE, reference_filename + type))

			result_name = 0
			if(diff_per.index(min(diff_per))>=3) :
				result_name = 3
			else :
				result_name = diff_per.index(min(diff_per))
			result_file = str(result_name) + '.png'
			result_file = reference_filename + result_file
			print result_file
			return result_file

		elif(25 <= diff_percentage < 36):
			num = '2/'
			reference_filename += num

			for i in range(1, 8):
				type = str(i) + '.png'
				diff_per.append(self.get_image_pixel_similarity(self.SAVE_IMAGE, reference_filename + type))

			result_name = 0
			if(diff_per.index(min(diff_per))>=3) :
				result_name = 3
			else :
				result_name = diff_per.index(min(diff_per))
			result_file = str(result_name) + '.png'
			result_file = reference_filename + result_file
			print result_file
			return result_file

		elif(36 <= diff_percentage < 47):
			num = '3/'
			reference_filename += num

			for i in range(1, 8):
				type = str(i) + '.png'
				diff_per.append(self.get_image_pixel_similarity(self.SAVE_IMAGE, reference_filename + type))

			result_name = 0
			if(diff_per.index(min(diff_per))>=3) :
				result_name = 3
			else :
				result_name = diff_per.index(min(diff_per))
			result_file = str(result_name) + '.png'
			result_file = reference_filename + result_file
			print result_file
			return result_file

		elif(47 <= diff_percentage < 58):
			num = '4/'
			reference_filename += num

			for i in range(1, 8):
				type = str(i) + '.png'
				diff_per.append(self.get_image_pixel_similarity(self.SAVE_IMAGE, reference_filename + type))

			result_name = 0
			if(diff_per.index(min(diff_per))>=3) :
				result_name = 3
			else :
				result_name = diff_per.index(min(diff_per))
			result_file = str(result_name) + '.png'
			result_file = reference_filename + result_file
			print result_file
			return result_file

		elif(58 <= diff_percentage < 69):
			num = '5/'
			reference_filename += num

			for i in range(1, 8):
				type = str(i) + '.png'
				diff_per.append(self.get_image_pixel_similarity(self.SAVE_IMAGE, reference_filename + type))

			result_name = 0
			if(diff_per.index(min(diff_per))>=3) :
				result_name = 3
			else :
				result_name = diff_per.index(min(diff_per))
			result_file = str(result_name) + '.png'
			result_file = reference_filename + result_file
			print result_file
			return result_file

		elif(69 <= diff_percentage < 80):
			num = '6/'
			reference_filename += num

			for i in range(1, 8):
				type = str(i) + '.png'
				diff_per.append(self.get_image_pixel_similarity(self.SAVE_IMAGE, reference_filename + type))

			result_name = 0
			if(diff_per.index(min(diff_per))>=3) :
				result_name = 3
			else :
				result_name = diff_per.index(min(diff_per))
			result_file = str(result_name) + '.png'
			result_file = reference_filename + result_file
			print result_file
			return result_file

		elif(80 <= diff_percentage):
			num = '7/'
			reference_filename += num

			result_file = '4.png'
			result_file = reference_filename + result_file
			print result_file
			return result_file

	def setPreprocessing(self, img_YCrCb):

		# Flesh Skin's Color ( Modify the Range )
		lower_skin = np.array([70,137,70])
		upper_skin = np.array([255,180,140])
		mask = cv2.inRange(img_YCrCb, lower_skin, upper_skin)

		# bitwise
		# mask = cv2.inRange(img_hsv, lower_skin, upper_skin)
		# img_skin = cv2.bitwise_and(img, img, mask=mask)

		return mask

	def get_image_pixel_similarity(self, img1, img2):

		# start the timer
		start = time.time()

		image1 = Image.open(img1).convert('L') if isinstance(img1, str) else img1
		image2 = Image.open(img2).convert('L') if isinstance(img2, str) else img2

		image2 = image2.resize(image1.size, Image.BILINEAR)

		image1_pixels = list(image1.getdata())
		image2_pixels = list(image2.getdata())

		# initialize vars
		i = 0
		tot_img_diff = 0
		diff_pixels = 0

		for pix1 in image1_pixels:
			pix2 = image2_pixels[i]

			tot_pix_diff = abs(pix1 - pix2)

			if tot_pix_diff != 0:
				diff_pixels += 1

			i += 1

			tot_img_diff += tot_pix_diff

		tot_pix = image1.size[0] * image1.size[1]
		img_diff = (float(diff_pixels) * 10000) / (float(tot_pix)*30.81563786)

		return img_diff

# if __name__ == '__main__':
#
# 	INPUT_IMAGE = "input/input.png"
#
# 	SAVE_IMAGE = "save/save.png"
# 	ImageProcessing(INPUT_IMAGE, SAVE_IMAGE)