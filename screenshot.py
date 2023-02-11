# hooking (사용자가 누른 값을 낚아챈다.)
# pip install keyboard

import keyboard
from PIL import ImageGrab
import time
import tkinter.messagebox as msgbox
onoff = False # F9 작동 스위치 (기본 OFF)

def onoff_reverse():
    global onoff
    onoff = not(onoff)
    if onoff == True:
        msgbox.showinfo("알림","F9 캡처기능 활성화")

    else:
        msgbox.showinfo("알림","F9 캡처기능 비활성화")

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    if onoff == True:
        curr_time = time.strftime("_%Y%m%d_%H%M%S")
        img = ImageGrab.grab()
        img.save("image{}.png".format(curr_time)) # image_20200601_102030.png
    else:
        print("off상태")


keyboard.add_hotkey("F9", screenshot) # F9키로 스크린샷 저장

#keyboard.add_hotkey("a", screenshot) # a키로 스크린샷 저장
#keyboard.add_hotkey("ctrl+shift+s", screenshot) # ctrl+shift+s키로 스크린샷 저장
keyboard.add_hotkey("F8", onoff_reverse) # F9키로 스크린샷 저장


#keyboard.wait("esc") # 사용자가 esc 누를 때까지 프로그램 수행
# ↑ 위 변수 때문에 해당 모듈이 바로 안꺼지고 유지되는 것


# lambda 매개변수 : 표현식
#keyboard.add_hotkey("A", lambda : print(onoff))

