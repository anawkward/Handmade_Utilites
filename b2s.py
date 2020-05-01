import pyperclip
import time

while True:
    content = pyperclip.paste() #type:str
    print(content)
    if content[1:3] == ":\\":
        content = content.replace("\\", "/")
        pyperclip.copy(content)
    time.sleep(1)