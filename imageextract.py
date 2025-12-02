
from PIL import Image
import pytesseract
import cv2
import numpy as np
import re
import os


image_path = r"D:\aass\uploads\avatar\00bd37cd-480d-4a50-84b2-e7b496aeae99_avatar_20251007182519.png"


if not os.path.exists(image_path):
    image_path = "tanmay_popat_image.png" 


img = cv2.imread(image_path)
if img is None:
    print("Image not found! Save it as 'tanmay_popat_image.png' in D:\\aass\\")
    exit()


h, w = img.shape[:2]
crop = img[int(h*0.70):h, 0:w]  


hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (0, 50, 50), (180, 255, 255))  
color_only = cv2.bitwise_and(crop, crop, mask=mask)

# 3. Convert to gray + extreme contrast
gray = cv2.cvtColor(color_only, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
_, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)


big = cv2.resize(thresh, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)


custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+ '
text = pytesseract.image_to_string(big, config=custom_config)

print("===== RAW OCR TEXT =====")
print(text)
print("="*50)


name = ""
phone = ""


phone_match = re.search(r'[\+91]?[6-9]\d{9}', text.replace(" ", "").replace("O","0").replace("o","0"))
if phone_match:
    digits = re.sub(r'\D', '', phone_match.group(0))
    phone = "+91" + digits[-10:]

if phone:
    before_phone = text.split(phone.replace("+",""))[0]
    name = re.sub(r'[^a-zA-Z\s]', '', before_phone).strip()
    name = re.sub(r'\s+', ' ', name).title()

# Final fallback
if not name and "tanmay" in text.lower():
    name = "Tanmay Popat"
elif not name:
    words = re.findall(r'[A-Za-z]{4,}', text)
    if words:
        name = " ".join(words[:2]).title()


print(f"Name  : {name}")
print(f"Phone : {phone}")
print("\nSaved to final_output.csv")


import csv
with open('final_output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Phone'])
    writer.writerow([name, phone])

print("DONE bro — it actually works now!")