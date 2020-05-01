import pyautogui
import time
import logging
import sys
import os

logger = logging.getLogger('my')
logger.setLevel(logging.INFO) # info 수준 이상을 로깅, 그 이하는 로깅X
logger.addHandler(logging.StreamHandler()) # 뭔지 아직 모름
pyname = os.path.basename(__file__).split('.')[0]
file_handler = logging.FileHandler(pyname+'.txt') # 로깅을 파일로 저장
logger.addHandler(file_handler)

def logged_exc(type, value, tb):
    logger.exception("Uncaught exception: {0}".format(str(value)))

sys.excepthook = logged_exc # 파이썬 빌트인 exception handler 를 수정, logger를 통한 exception 으로 대체.

while True:
    location = pyautogui.position()
    x, y = location
    if x > 1920:
        pyautogui.moveTo(1920,y)
    time.sleep(0.1)