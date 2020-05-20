import pyperclip
import time
import pynput
from pynput.keyboard import Key
from typing import Union

seq_len = input("한번에 비교할 list of strings 의 length 를 지정해주십시오: ")
print(f"사이즈 {seq_len}의 리스트를 서로 비교합니다.")
print(f"공백, 줄바꿈차이는 SAME으로 간주합니다. switch 를 기준으로 문서를 옮기면 됩니다.")

seq_len = int(seq_len)
history = []

def compare(s1:str, s2:str):
    if len(s1) > len(s2):
        x = s1
        y = s2
    else:
        x = s2
        y = s1
    if x == y:
        return True
    else:
        return False
def compareList(l1:list, l2:list):
    ret = []
    for i in range(len(l1)):
        comp = compare(l1[i], l2[i])
        if comp:
            ret.append(True)
        else:
            ret.append(False)
    return ret
def remover(target:str, delete:Union[list, tuple, str]):
    for item in delete:
        target = target.replace(item, '')
    return target
def history_to_lists(history:list, seq_len:int):
    l1 = history[-2*seq_len:-seq_len]
    l2 = history[-seq_len:]
    return l1, l2

def key_release(k):
    global history
    try:
        if k.char == '\x03':
            content = pyperclip.paste() #type:str
            content = remover(content, ['\n', ' ', '\r', '\"', '\''])
            print(content, end = '|')
            history.append(content)
            if len(history)%(seq_len*2) == 0:
                l1, l2 = history_to_lists(history, seq_len)
                comp = compareList(l1, l2)
                for b in comp:
                    if b:
                        print('\b\nSAME')
                        history = []
                    else:
                        print('\b\nDIFF')
                        history = []
            elif len(history)%seq_len == 0:
                print('\b\n<SWITCH>')
    except:
        pass

k_listener = pynput.keyboard.Listener(on_release=key_release)
k_listener.start()
k_listener.join()