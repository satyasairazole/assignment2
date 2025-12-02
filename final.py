import easyocr
import os
import csv
import re

reader = easyocr.Reader(['en'], gpu=True)

FOLDER = r"D:\aass\uploads\avatar"
OUTPUT = "results_m.csv"


def extract_name_phone(text_list):
    combined = " ".join(text_list)


    match = re.search(r"[+\-]?\s*\(?\d{1,4}\)?[\s-]*\d[\d\s-]{8,14}", combined)

    if match:
        raw_phone = match.group(0)

        phone = re.sub(r"[^\d+\-]", "", raw_phone)

        if phone.startswith("-"):
            phone = "+" + phone[1:]

        if not phone.startswith("+"):
            phone = "+" + phone
        phone = phone.replace("-", "")

    else:
        phone = ""
        raw_phone = ""

  
    name = combined.replace(raw_phone, "").replace(phone, "").strip()
    name = name.rstrip("-").strip()

    return name, phone



with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Image", "Name", "Phone", "Status"])

    for img in os.listdir(FOLDER):
        if not img.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        path = os.path.join(FOLDER, img)

        try:
            result = reader.readtext(path)
            result_sorted = sorted(result, key=lambda x: x[0][0][1])
            text_list = [i[1] for i in result_sorted]

            name, phone = extract_name_phone(text_list)

            writer.writerow([img, name, phone, "OK"])
            print(f"{img} → Name: {name}, Phone: {phone}")

        except Exception as e:
            writer.writerow([img, "", "", "CORRUPT"])
            print(f"{img} → SKIPPED (Corrupted Image)")
