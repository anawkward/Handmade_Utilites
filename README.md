# MyUtil.py
: some useful user exprience, simplified funtions to import. maybe you can study basics of python understanding these scripts :D

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
: use exe file, or modify py script

b2s.exe : I monitors your clipboard every second. if you have path like "C:\\...", I change format to "C:/..."

mouseLock.py : I prevent mouse to across border. if you have a monitor not using, or turned off for some purpose, it might be useful

double_checker.exe : it's made for double-check between documents. you can select strings to compare by pressing "ctrl + C"
