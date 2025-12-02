import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import easyocr
reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext(r"D:\aass\uploads\avatar\00bd37cd-480d-4a50-84b2-e7b496aeae99_avatar_20251007182519.png")

for _, text, _ in result:
    print(text)
