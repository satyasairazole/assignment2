#---------#instalations#---------------#
cuda gpu version is working only on python 3.10

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install easyocr



For separating images folder-wise, use a script that separates avatars and selfies into two different folders.
Then, in test.py, use the images from those folders.


-----------------------------------------------------------------
Next, extract the name and phone number from each image.
Use final.py to extract the names from those images.