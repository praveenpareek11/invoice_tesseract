#!/usr/bin/env python
# coding: utf-8

#Import necessary libraries
import cv2
import sys
import pytesseract
import re


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: python ocr_simple.py image.jpg')
        sys.exit(1)
    imPath = f'/home/praveen/work/AGS_pdfs/AGS_sample_Invoices/img_2.jpg'

    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    config = ('-l eng --oem 1 --psm 3')

    im = cv2.imread(imPath, cv2.IMREAD_GRAYSCALE)

    text = pytesseract.image_to_string(im, config=config)


l = text.split("\n")

pattern1 = re.compile(r'Invoice No.\ *\:*\©*\ *\w*/\w*-\w*')
pattern2 = re.compile(r'Date : \w*-\w*-\w*')
pattern3 = re.compile(r'P.O. No. & Date : \w*')

for data in l:
    result1 = pattern1.findall(data)
    result2 = pattern2.findall(data)
    result3 = pattern3.findall(data)

    if (result1 != []):
        print(result1[0])
    if (result2 != []):
        print(result2[0])
    if (result3 != []):
        print(result3[0])

for i in range(0,len(l)):
    if l[i].endswith('LTD.'):
        print(l[i])
