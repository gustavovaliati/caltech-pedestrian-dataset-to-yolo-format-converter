# adapted from https://github.com/mitmul/caltech-pedestrian-dataset-converter/blob/master/scripts/convert_seqs.py

import os
import glob
import cv2 as cv


def save_img(dname, fn, i, frame):
	cv.imwrite('{}/{}_{}_{}.jpg'.format(
		out_dir, os.path.basename(dname),
		os.path.basename(fn).split('.')[0], i), frame)

out_dir = 'images'
if not os.path.exists(out_dir):
	os.makedirs(out_dir)

def convert(dir):
	for dname in sorted(glob.glob(dir)):
		print(dname)
		for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
			cap = cv.VideoCapture(fn)
			i = 0
			while True:
				ret, frame = cap.read()
				if not ret:
					break
				save_img(dname, fn, i, frame)
				i += 1
			print(fn)


def convert_to_caltech10x(dir, skipper=30):
	'''
	Training set: Caltech 10x.
	Uses only every 3rd frame.
	1. Brazil, G., Yin, X., & Liu, X. (2017). Illuminating Pedestrians via Simultaneous Detection & Segmentation. Retrieved from http://arxiv.org/abs/1706.08564
	2. Zhang, S., Benenson, R., & Schiele, B. (n.d.). Filtered Channel Features for Pedestrian Detection. Retrieved from https://arxiv.org/pdf/1501.05759.pdf
	'''
	for dname in sorted(glob.glob(dir)):
		print(dname)
		for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
			cap = cv.VideoCapture(fn)
			i = 1
			while True:
				ret, frame = cap.read()
				if not ret:
					break
				if (i % skipper) == 0:
					save_img(dname, fn, i-1, frame)
				i += 1
			print(fn)

# convert_to_caltech10x('/media/gustavo/GRV/datasets/CaltechPedestrians/original/videos/train/*', skipper=3)
convert_to_caltech10x('/media/gustavo/GRV/datasets/CaltechPedestrians/original/videos/test/*', skipper=30)
