# 제작 : killsonic@naver.com
# 해상도 1920*1080 FHD / 2560*1440 QHD 창모드 최대화 (그림크기가 달라져 인식안됨)

from email.headerregistry import ContentTransferEncodingHeader
import pyautogui as pgi
import time
import keyboard
import pydirectinput as pyd
import random
print('피파온라인4 감독모드')
print('by 불닭 blog.naver.com/killsonic')
print('해상도 1920*1080 FHD / 2560*1440 QHD')
print('창모드 최대화 권장')
print('"F3" 시작 / "F4" 10초 누르면 종료')

width, height = pgi.size()      #화면해상도 확인
print('해상도 :' , width, height)

def skey():
    pyd.keyDown("s")
    time.sleep(0.05)
    pyd.keyUp("s")


def imgclick(files):    #이미지 찾아서 클릭 함수
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.8)
    if imgfile == None:
        pass
    else:
        print(imgfile)
        x, y = imgfile
        x = x - random.randint(1, 20) + random.randint(1, 20)
        y = y - random.randint(1, 20) + random.randint(1, 20)
        pgi.click(x, y)

def skeypress(files):   #이미지 찾아서 S 누름
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.8)
    if imgfile == None:
        pass
    else:
        print(imgfile)
        x, y = imgfile
        x = x - random.randint(1, 20) + random.randint(1, 20)
        y = y - random.randint(1, 20) + random.randint(1, 20)
        pgi.click(x, y)
        pyd.keyDown("s")
        time.sleep(0.05)
        pyd.keyUp("s")

def esckeypress(files): #이미지 찾아서 ESC 누름
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.8)
    if imgfile == None:
        pass
    else:
        print(imgfile)
        x, y = imgfile
        x = x - random.randint(1, 20) + random.randint(1, 20)
        y = y - random.randint(1, 20) + random.randint(1, 20)
        pgi.click(x, y)
        pyd.keyDown("esc")
        time.sleep(0.05)
        pyd.keyUp("esc")

while True:
    if keyboard.is_pressed('F3'): #작업시작
        print('작업시작')

        while True:
            if keyboard.is_pressed('F4'): #F4 중지
                print('중지됨')
                break
            else:
                if width == 2560: #해상도가 QHD 일 때 실행
                    skeypress('ss.png') #s 누르기
                    imgclick('s2.png')  #확인
                    imgclick('s3.png')  #공식경기
                    imgclick('s4.png')  #진행
                    imgclick('s5.png')  #선택완료
                    imgclick('s6.png')  #다음
                    imgclick('s7.png')  #확인
                    esckeypress('sesc.png') #esc 누르기
                    skeypress('sskip.png')  #s 누르기
                                    
                else:           #해상도가 FHD 일 때 실행
                    skeypress('fhds.png')   #s 누르기
                    imgclick('fhd2.png')    #확인
                    imgclick('fhd3.png')    #공식경기
                    imgclick('fhd4.png')    #진행
                    imgclick('fhd5.png')    #선택완료
                    imgclick('fhd6.png')    #다음
                    imgclick('fhd7.png')    #다음
                    esckeypress('fhdesc.png')   #esc 누르기
                    skeypress('fhdskip.png')    #s 누르기