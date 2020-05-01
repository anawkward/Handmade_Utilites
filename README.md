# MyUtil.py
: some useful user exprience, siplified funtions to import

MyUtil.subplot() : make subplot at once
(example)
```python
import MyUtil
import cv2

img1 = cv2.imread('C:/img1.png')
img2 = cv2.imread('C:/img2.png')

MyUtil.subplot(img1, img2, col = 1)
```









# lifehacking tools(exe, scripts for exe)
: modify py file, and make exe file using pyinstaller with options like -y -F -w ...

b2s.exe : I monitors your clipboard every second. if you have path like "C:\\...", I change format to "C:/..."

mouseLock.py : I prevent mouse to across border. if you have a monitor not using, or turned off for some purpose, it might be useful

