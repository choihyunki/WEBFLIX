import pyautogui as pg
import sys
import pyperclip as pc
import keyboard










wt = pg.prompt(text='웹툰 제목을 입력하세요.', title='WEBFLIX', default='') #wt = 웹툰 제목
while(wt==''):                              #제목을 입력하지 않을경우 
    rt = pg.alert(text='다시 입력해주세요.', title='WEBFLIX', button='OK') #rt = 다시입력
    wt = pg.prompt(text='웹툰 제목을 입력하세요.', title='WEBFLIX', default='')
    if(wt==''):                             #한번더 입력하지 않을 경우 경고문 출력
        we = pg.alert(text='오류입니다. 다시 시작해주세요.', title='WEBFLIX', button='OK') #경고문
        sys.exit()
    else:
        break #입력 했을경우 넘어가기


wr = pg.prompt(text='웹툰 회차를 입력하세요.\n     숫자만 입력하세요.', title='WEBFLIX', default='') #wr = 웹툰 회차  
while(wr==''):                              #회차를 입력하지 않을 경우
    rt = pg.alert(text='다시 입력해주세요.', title='WEBFLIX', button='OK') #rt = 다시입력
    wr = pg.prompt(text='웹툰 회차를 입력하세요.\n     숫자만 입력하세요.', title='WEBFLIX', default='')
    if(wr==''):                             #한번더 입력하지 않을 경우 경고문 출력 후 종료
        we = pg.alert(text='오류입니다. 다시 시작해주세요.', title='WEBFLIX', button='OK') # 경고문
        sys.exit()
    else:
        break #입력 했을경우 넘어가기

scroll = pg.prompt(text='                      읽는 속도를 입력하세요.\n                            숫자만 입력하세요.\n  1=매우느림 2=느림 3=보통 4=빠름 5=매우빠름', title='WEBFLIX', default='')
if scroll > '5':
    pg.alert(text='잘못 입력하셨습니다.\n      다시 시작해주세요.', title="WEBFLIX", button='OK')
    sys.exit()


ms = pg.size()
ws = pg.alert(text = ms, title='WEBFLIX', button='OK') #모니터 사이즈 출력




# chrome 웹브라우저 실행
pg.press('win') #윈도우키 누르기
pg.sleep(0.5) #0.5초 대기
pg.write('chrome', interval=0.1) #0.1초마다chrome을타이핑합니다
pg.press('enter')
pg.sleep(3)
# 네이버 웹툰 홈페이지 검색
pg.moveTo(300,50)
pg.click(button = 'left')
pc.copy('comic.naver.com/index') #웹툰홈페이지 복사
pg.hotkey('ctrl','v') #웹툰홈페이지 붙여넣기
pg.press('enter')
pg.sleep(2)
search = pg.locateOnScreen('./검색.JPG') # 웹툰 검색창 이미지의 위치찾기
point = pg.center(search) #웹툰검색창의 정중앙 좌표
pg.moveTo(point) 
pg.click(button='left') #마우스 좌클릭

pc.copy(wt) #웹툰제목 클립보드에 저장
pg.hotkey('ctrl','v')#클립보드에 저장된 제목 붙여넣기
pg.sleep(0.5)
pg.press('enter')

pg.sleep(1)
pg.click(420,450)#검색한 웹툰 첫번째 웹툰 선택
pg.sleep(1)








if(wr=='1'): #1회차 시작일 경우
    first = pg.locateOnScreen('./1화부터.PNG') # 웹툰 1화부터 이미지의 위치찾기
    point1 = pg.center(first) #웹툰1화부터의 정중앙 좌표
    pg.moveTo(point1) 
    pg.click(button='left')
    pg.sleep(0.5)
    webfirst = pg.locateOnScreen('./1화.PNG') # 웹툰 1화 이미지의 위치찾기
    pointwebfirst = pg.center(webfirst) #웹툰1화의 정중앙 좌표
    pg.moveTo(pointwebfirst)
    pg.click(button='left')
    pg.sleep(2)
elif(wr>='2'): #2회차 이상 시작일 경우
    first = pg.locateOnScreen('./1화부터.PNG') # 웹툰1화부터 이미지의 위치찾기
    point1 = pg.center(first) #웹툰1화부터의 정중앙 좌표
    pg.moveTo(point1) 
    pg.click(button='left')
    pg.sleep(0.5)
    webfirst = pg.locateOnScreen('./1화.PNG') # 웹툰 1화 이미지의 위치찾기
    pointwebfirst = pg.center(webfirst) #웹툰1화의 정중앙 좌표
    pg.moveTo(pointwebfirst)
    pg.click(button='left')
    pg.sleep(2)
    i = 1
    while i < int(wr) : # 원하는 웹툰 회차까지 이동
        nextround = pg.locateOnScreen("./다음화.JPG")
        nextroundcenter = pg.center(nextround)
        pg.moveTo(nextroundcenter)
        pg.click(button='left')
        pg.sleep(1)
        i += 1



#프로그램 종료 함수
def exitprogram():
    if keyboard.is_pressed("F9"): #F9 누르고 있으면 프로그램 정지
        wstop = pg.alert(text='프로그램이 정지되었습니다.', title='WEBFLIX', button='OK')
        rsave = pg.alert(text='저장되었습니다.', title='WEBFLIX', button='OK')
        pg.press('WIN') #윈도우키 입력
        pg.sleep(0.2) #0.2초 대기
        pg.write('notepad',interval=0.1)    #notepad 0.1초마다 입력
        pg.press('ENTER')                   #enter 입력
        pg.sleep(1)                         #1초간 대기
        pc.copy(wt)              #입력받은 저장할 웹툰 제목 복사
        pg.hotkey('ctrl','v')               #붙여넣기
        pg.sleep(0.5)                       #0.5초 대기
        pc.copy(wr)              #입력받은 저장할 웹툰 회차 복사
        pg.hotkey('ctrl','v')               #붙여넣기
        pg.sleep(0.5)                       #0.5초 대기
        pg.hotkey('ctrl','shift','s')       #다른이름으로 저장하기
        pg.sleep(1)                         #1초간 대기
        pc.copy(wt)              #입력받은 저장할 웹툰 제목 복사
        pg.hotkey('ctrl','v')               #notepad 제목으로 붙여넣기
        pg.press('ENTER')                   #enter키 입력
        sys.exit() # 정지                   #프로그램 종료






#이미지 찾는 함수
def findscroll(next, maxscroll=1000): # 다음화 사진, 최대 스크롤 횟수
    scrollcount = 0  # 스크롤 횟수

    while scrollcount < maxscroll:
        try:
            # 이미지를 찾기 시도
            imagepoint = pg.locateOnScreen(next) #"다음화.JPG" 이미지 좌표
            
            if imagepoint is not None:
                # 이미지를 찾았을 경우 클릭하고 스크롤 후 반복문 종료
                pg.click(imagepoint) 
                pg.sleep(2)
                while True:
                    if scroll == '1' : #스크롤 속도 1일경우
                        exitprogram()
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.sleep(1)
                        break
                    if scroll == '2' : #스크롤 속도 2일경우
                        exitprogram()
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.sleep(1)
                        break
                    if scroll == '3' : #스크롤 속도 3일경우
                        exitprogram()
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.sleep(1)
                        break
                    if scroll == '4' : #스크롤 속도 4일경우
                        exitprogram()
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.sleep(1)
                        break
                    if scroll == '5' : #스크롤 속도 5일경우
                        exitprogram()
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.scroll(-200)
                        pg.sleep(1)
                        break
                break
            else:
                # 이미지를 찾지 못했을 경우 스크롤 다운
                while True:
                    if scroll == '1' : #스크롤 속도 1일경우
                        exitprogram()
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.sleep(1)
                        break
                    if scroll == '2' : #스크롤 속도 2일경우
                        exitprogram()
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.sleep(1)
                        break
                    if scroll == '3' : #스크롤 속도 3일경우
                        exitprogram()
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.sleep(1)
                        break
                    if scroll == '4' : #스크롤 속도 4일경우
                        exitprogram()
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.sleep(1)
                        break
                    if scroll == '5' : #스크롤 속도 5일경우
                        exitprogram()
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.scroll(-100)
                        pg.sleep(1)
                        break
                scrollcount += 1
                pg.sleep(1)  # 스크롤 동작 후 잠시 대기
        except Exception as e:
            print(f"오류 발생: {e}")
            break


next = "./다음화.JPG"







while True:
    pg.sleep(1.5)
    exitprogram()
    while scroll :
        if scroll == '1' : #스크롤 속도 1일경우
            pg.scroll(-200)
            pg.sleep(1)
            break
        if scroll == '2' : # 스크롤 속도 2일경우
            pg.scroll(-200)
            pg.scroll(-200)
            pg.sleep(1)
            break
        if scroll == '3' : # 스크롤 속도 3일경우
            pg.scroll(-200)
            pg.scroll(-200)
            pg.scroll(-200)
            pg.sleep(1)
            break
        if scroll == '4' : # 스크롤 속도 4일경우
            pg.scroll(-200)
            pg.scroll(-200)
            pg.scroll(-200)
            pg.scroll(-200)
            pg.sleep(1)
            break
        if scroll == '5' : # 스크롤 속도 5일경우
            pg.scroll(-200)
            pg.scroll(-200)
            pg.scroll(-200)
            pg.scroll(-200)
            pg.scroll(-200)
            pg.sleep(1)
            break
    findscroll(next)













