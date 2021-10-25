import numpy as np
import cv2
from time import time
from time import sleep
import win32gui
import win32ui
import win32con
import win32api
import pyautogui
import keyboard
import tkinter
from skimage.metrics import structural_similarity as compare_ssim

class WindowCapture():
    
    
    w = 1920 # set this
    h = 1080 # set this
    hwnd=None
    windowname=""
    def __init__(self,window_name):
        self.w=1920
        self.h=1080
        self.hwnd = win32gui.FindWindow(None, window_name)
        self.windowname=window_name
    
    def windowcap(self):

        self.hwnd = win32gui.FindWindow(None, self.windowname)
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)
        #dataBitMap.SaveBitmapFile(cDC, "out.bmp")


        signedIntsArray=dataBitMap.GetBitmapBits(True)
        img=np.frombuffer(signedIntsArray,dtype='uint8')
        img.shape=(self.h,self.w,4)
        img=img[...,:3]
        img=np.ascontiguousarray(img)

        
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        
        return img


l_status = tkinter.Label(text='Casts: Inactive', font=('Times','15'), fg='red', bg='black')
l_status.master.overrideredirect(True)
l_status.master.geometry("+1750+450")
l_status.master.lift()
l_status.master.wm_attributes("-topmost", True)
l_status.master.wm_attributes("-disabled", True)
l_status.pack()

currRota = tkinter.Label(text='Inactive', font=('Times','15'), fg='red', bg='black')
currRota.master.overrideredirect(True)
currRota.master.geometry("+1750+450")
currRota.master.lift()
currRota.master.wm_attributes("-topmost", True)
currRota.master.wm_attributes("-disabled", True)
currRota.pack()

cdMode = tkinter.Label(text="CD's :Inactive", font=('Times','15'), fg='red', bg='black')
cdMode.master.overrideredirect(True)
cdMode.master.geometry("+1750+450")
cdMode.master.lift()
cdMode.master.wm_attributes("-topmost", True)
cdMode.master.wm_attributes("-disabled", True)
cdMode.pack()
#weird test


#weirdtestend

#win=pyautogui.getWindow("Ascension") 
    
wincap=WindowCapture("Ascension")

hwnd=win32gui.FindWindow(None,wincap.windowname)

win=win32ui.CreateWindowFromHandle(hwnd)

cv2.destroyAllWindows()
#explo
explo_on= cv2.imread('exploshoton.jpg', cv2.IMREAD_COLOR)
grayExpOn = cv2.cvtColor(explo_on, cv2.COLOR_BGR2GRAY)

explo_off= cv2.imread('exploshotoff.jpg', cv2.IMREAD_COLOR)
grayExpOff = cv2.cvtColor(explo_off, cv2.COLOR_BGR2GRAY)

#arcane
arcane_on= cv2.imread('arcaneshoton.jpg', cv2.IMREAD_COLOR)
grayarcaneOn = cv2.cvtColor(arcane_on, cv2.COLOR_BGR2GRAY)

arcane_off= cv2.imread('arcaneshotoff.jpg', cv2.IMREAD_COLOR)
grayarcaneOff = cv2.cvtColor(arcane_off, cv2.COLOR_BGR2GRAY)

#multi
multi_on= cv2.imread('multishoton.jpg', cv2.IMREAD_COLOR)
graymultiOn = cv2.cvtColor(multi_on, cv2.COLOR_BGR2GRAY)

multi_off= cv2.imread('multishotoff.jpg', cv2.IMREAD_COLOR)
graymultiOff = cv2.cvtColor(multi_off, cv2.COLOR_BGR2GRAY)

#aimed
aimed_on= cv2.imread('aimedshoton.jpg', cv2.IMREAD_COLOR)
grayaimedOn = cv2.cvtColor(aimed_on, cv2.COLOR_BGR2GRAY)

aimed_off= cv2.imread('aimedshotoff.jpg', cv2.IMREAD_COLOR)
grayaimedOff = cv2.cvtColor(aimed_off, cv2.COLOR_BGR2GRAY)


#black
black_on= cv2.imread('blackshoton.jpg', cv2.IMREAD_COLOR)
grayblackOn = cv2.cvtColor(black_on, cv2.COLOR_BGR2GRAY)

black_off= cv2.imread('blackshotoff.jpg', cv2.IMREAD_COLOR)
grayblackOff = cv2.cvtColor(black_off, cv2.COLOR_BGR2GRAY)


#charge
charge_on= cv2.imread('chargeshoton.jpg', cv2.IMREAD_COLOR)
graychargeOn = cv2.cvtColor(charge_on, cv2.COLOR_BGR2GRAY)

charge_off= cv2.imread('chargeshotoff.jpg', cv2.IMREAD_COLOR)
graychargeOff = cv2.cvtColor(charge_off, cv2.COLOR_BGR2GRAY)


#trap
trap_on= cv2.imread('trapshoton.jpg', cv2.IMREAD_COLOR)
graytrapOn = cv2.cvtColor(trap_on, cv2.COLOR_BGR2GRAY)

trap_off= cv2.imread('trapshotoff.jpg', cv2.IMREAD_COLOR)
graytrapOff = cv2.cvtColor(trap_off, cv2.COLOR_BGR2GRAY)


#lload
lload_on= cv2.imread('lloadshoton.jpg', cv2.IMREAD_COLOR)
graylloadOn = cv2.cvtColor(lload_on, cv2.COLOR_BGR2GRAY)

lload_off= cv2.imread('lloadshotoff.jpg', cv2.IMREAD_COLOR)
graylloadOff = cv2.cvtColor(lload_off, cv2.COLOR_BGR2GRAY)


#snip
snip_on= cv2.imread('snipshoton.jpg', cv2.IMREAD_COLOR)
graysnipOn = cv2.cvtColor(snip_on, cv2.COLOR_BGR2GRAY)

snip_off= cv2.imread('snipshotoff.jpg', cv2.IMREAD_COLOR)
graysnipOff = cv2.cvtColor(snip_off, cv2.COLOR_BGR2GRAY)


#snip9
snip9_off= cv2.imread('snipshotoff9.jpg', cv2.IMREAD_COLOR)
graysnip9Off = cv2.cvtColor(snip9_off, cv2.COLOR_BGR2GRAY)
#snip8
snip8_off= cv2.imread('snipshotoff8.jpg', cv2.IMREAD_COLOR)
graysnip8Off = cv2.cvtColor(snip8_off, cv2.COLOR_BGR2GRAY)
#snip7
snip7_off= cv2.imread('snipshotoff7.jpg', cv2.IMREAD_COLOR)
graysnip7Off = cv2.cvtColor(snip7_off, cv2.COLOR_BGR2GRAY)
#snip6
snip6_off= cv2.imread('snipshotoff6.jpg', cv2.IMREAD_COLOR)
graysnip6Off = cv2.cvtColor(snip6_off, cv2.COLOR_BGR2GRAY)
#arcanepower
arcanepower= cv2.imread('arcanepower.jpg', cv2.IMREAD_COLOR)
grayarcanepower = cv2.cvtColor(arcanepower, cv2.COLOR_BGR2GRAY)
#mug
mug= cv2.imread('mug.jpg', cv2.IMREAD_COLOR)
graymug = cv2.cvtColor(mug, cv2.COLOR_BGR2GRAY)
#mana
mana= cv2.imread('mana.jpg', cv2.IMREAD_COLOR)
graymana = cv2.cvtColor(mana, cv2.COLOR_BGR2GRAY)
#gcd
gcd= cv2.imread('gcd.jpg', cv2.IMREAD_COLOR)
graygcd = cv2.cvtColor(gcd, cv2.COLOR_BGR2GRAY)
#DBEXPLO
DBexplo_on= cv2.imread('explodebuff.jpg', cv2.IMREAD_COLOR)
grayDBExpOn = cv2.cvtColor(DBexplo_on, cv2.COLOR_BGR2GRAY)
#DBsun
DBsun_on= cv2.imread('sundebuff.jpg', cv2.IMREAD_COLOR)
grayDBsun = cv2.cvtColor(DBsun_on, cv2.COLOR_BGR2GRAY)
#MELEECHECK
melee_on= cv2.imread('meleecheck.jpg', cv2.IMREAD_COLOR)
graymelee= cv2.cvtColor(melee_on, cv2.COLOR_BGR2GRAY)


loop_time=time()
last_pressed=time()
explo_last_pressed=time()-3
arcaneban=False
lloadremain=0
continueable=False
explobreak=2
aoe_mode=False
latbase=((62/1000)/2)-0.75
latency=((62/1000)/2)-0.75
latency=-1.5
print(latency)
last_cd=time()-20
cd_mode=False
labelkeep={"l_status":"Casts: Inactive","currRota":"Inactive","cdMode":"CD's :Inactive"}
print(labelkeep)
lock=0
waiter=time()-5


while True:
    currSkill='Using: '
    currRota['text']=labelkeep['currRota']
    if keyboard.is_pressed('ü'):
        print("C O N T I N U E ")
        l_status['text']='Casts: Active'
        l_status['fg']='green'
        continueable=True
        aoe_mode=False

        
    if keyboard.is_pressed(','):
        print("S T O P")
        l_status['text']='Casts: Inactive'
        l_status['fg']='red'
        continueable=False

        
    if keyboard.is_pressed('shift+1') and lock==0:
        print("HIDE")
        l_status.master.geometry("+9550+9350")
        lock=1

        
    if keyboard.is_pressed('shift+q') and lock==1:
        print("UNHIDE")
        l_status.master.geometry("+1550+350")
        lock=0

        
    if keyboard.is_pressed('q'):
        print("CD MODE ")
        cdMode['fg']="green"
        cd_mode=True
        cdMode['text']="CD's: Active"
        
    if keyboard.is_pressed('0'):
        print("CD MODE OFF  ")
        cd_mode=False
        cdMode['text']="CD's: Inactive"
        cdMode['fg']="red"

    
    #scr=scr[:,:,::-1].copy()
    #cv2.imshow('frame',scr)
    #print('FPS {}'.format(1/(time()-loop_time)))

    if time()-waiter>=0.15:
        scr=wincap.windowcap()
        scr=np.array(scr)
        
        #print(time()-waiter)
        loop_time=time()
        if continueable:
            gcdCurr=scr[620:635,360:410]
            graygcdCurr = cv2.cvtColor(gcdCurr, cv2.COLOR_BGR2GRAY)
            cv2.imshow("crr",graygcdCurr)
            cv2.imshow("gcd",graygcd)
            if(compare_ssim(graygcd, graygcdCurr, full=True)[0]>=0.95):
                print("WE IN CHIEF")
                lloadCurr=scr[499:551,719:772]
                graylloadCurr = cv2.cvtColor(lloadCurr, cv2.COLOR_BGR2GRAY)
                if((lloadremain<=0 and compare_ssim(graylloadOn, graylloadCurr, full=True)[0]>=compare_ssim(graylloadOff, graylloadCurr, full=True)[0])):
                    print("LOCKED AND LOADED C H I E F")
                    lloadremain=3
                    arcaneban=True
                    latency=explobreak-(1.5-latency)
                    if aoe_mode:
                        explobreak=2
                
                ###black
                blackCurr=scr[714:768,719:772]
                grayblackCurr = cv2.cvtColor(blackCurr, cv2.COLOR_BGR2GRAY) 
                if(cd_mode and compare_ssim(grayblackOn, grayblackCurr, full=True)[0]>=0.79):
                    print("TRUE",compare_ssim(grayblackOn, grayblackCurr, full=True)[0],"FALSE",compare_ssim(grayblackOff, grayblackCurr, full=True)[0])
                    if(True):
                        
                        blackarcanepower=scr[610:663,554:607]
                        grayarcanepowerCurr = cv2.cvtColor(blackarcanepower, cv2.COLOR_BGR2GRAY)
                        if(time()-last_cd>=20 and compare_ssim(grayarcanepower, grayarcanepowerCurr, full=True)[0]>=0.9):
                            print("Arcane P O W E R ")
                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x47, 0)
                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x47, 0)
                            last_cd=time()
                        
                        blackmug=scr[610:663,498:551]
                        graymugCurr = cv2.cvtColor(blackmug, cv2.COLOR_BGR2GRAY)
                        
                        print("B L A C K  S H O T ")
                        currSkill+='Black Arrow'
                        #pyautogui.press('z')
                        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x5A, 0)
                        win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x5A, 0)
                        last_pressed=time() 
                
                        if(time()-last_cd>=20 and compare_ssim(graymug, graymugCurr, full=True)[0]>=0.9):
                            print("M U G ")
                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x43, 0)
                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x43, 0)
                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x43, 0)
                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x43, 0)
                else:
                    ###explo
                    ExploCurr=scr[555:608,718:771]
                    grayExpCurr = cv2.cvtColor(ExploCurr, cv2.COLOR_BGR2GRAY)
                    
                    DBExploCurr=scr[588:605,374:393]
                    grayDBExpCurr = cv2.cvtColor(DBExploCurr, cv2.COLOR_BGR2GRAY)
                    
                    if(compare_ssim(grayExpOn, grayExpCurr, full=True)[0]>=compare_ssim(grayExpOff, grayExpCurr, full=True)[0]):
                        if(compare_ssim(grayDBExpOn, grayDBExpCurr, full=True)[0]<=0.90 or time()-explo_last_pressed>=explobreak ):
                            print("E X P L O ")
                            currSkill+='Explo Shot'
                            #pyautogui.press('r')
                            #pyautogui.press('r')
                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x52, 0)
                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x52, 0)
                            lloadremain=lloadremain-1
                            if lloadremain==0:
                                arcaneban=False
                                explobreak=2
                                latency=latbase
                            #if((compare_ssim(grayExpOn, grayExpCurr, full=True)[0]<=compare_ssim(grayExpOff, grayExpCurr, full=True)[0]) and lloadremain<=0):
                            last_pressed=time()
                            explo_last_pressed=time()
                            if latency==latbase+0.12:
                                latency=latbase
                    else:
                        manaCurr=scr[483:505,593:654]
                        graymanaCurr = cv2.cvtColor(manaCurr, cv2.COLOR_BGR2GRAY)
                        if(compare_ssim(graymana, graymanaCurr, full=True)[0]>=0.9):
                            if(True):
                                #pyautogui.press('T')
                                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x54, 0)
                                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x54, 0)
                                print("get mana dumbass")
                                currSkill+='Life Tap'
                                last_pressed=time()
                                latency=latbase

                        else:##CHARGE+EXPLOTRAP+ST>6
                            chargeCurr=scr[609:661,661:713]
                            graychargeCurr = cv2.cvtColor(chargeCurr, cv2.COLOR_BGR2GRAY)
                            
                            trapCurr=scr[661:714,661:714]
                            graytrapCurr = cv2.cvtColor(trapCurr, cv2.COLOR_BGR2GRAY)

                            
                            check1=compare_ssim(graychargeOn, graychargeCurr, full=True)[0]>=0.9
                            check2=compare_ssim(graytrapOn, graytrapCurr, full=True)[0]>=0.9
                            ##CHARGE+TRAP
                            snipCurr=scr[712:765,607:659]
                            graysnipCurr = cv2.cvtColor(snipCurr, cv2.COLOR_BGR2GRAY)
                            ###print("TRAP ACC ",compare_ssim(graytrapOn, graytrapCurr, full=True)[0])
                            if(check1 and check2 and (compare_ssim(graysnip9Off, graysnipCurr, full=True)[0]>=0.95 or #CHANGE IF BUILD HAS CHARGE
                                compare_ssim(graysnip8Off, graysnipCurr, full=True)[0]>=0.95 or
                                compare_ssim(graysnip7Off, graysnipCurr, full=True)[0]>=0.95 or
                                not(cd_mode)
                                )):
                                    print("charge trap combo")
                                    currSkill+='Trap Combo'
                                    #pyautogui.press('x')
                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x58, 0)
                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x58, 0)
                                    melee_status=True
                                    entry=time()
                                    times_looped=0
                                    cast_allowed=True
                                    while melee_status:
                                        scr=wincap.windowcap()
                                        scr=np.array(scr)
                                        meleeCurr=scr[448:460,600:649]
                                        graymeleeCurr = cv2.cvtColor(meleeCurr, cv2.COLOR_BGR2GRAY)
                                        if(compare_ssim(graymelee, graymeleeCurr, full=True)[0]>=0.95):
                                            melee_status=False
                                            print("we in melee bish",times_looped)
                                        if time()-entry>=0.95:
                                            melee_status=False
                                            print("we not in melee but waited too damn long bish",times_looped)
                                                    
                                        chargeCurr=scr[609:661,661:713]
                                        graychargeCurr = cv2.cvtColor(chargeCurr, cv2.COLOR_BGR2GRAY)
                                        times_looped+=1
                                        check1=compare_ssim(graychargeOn, graychargeCurr, full=True)[0]>=0.95
                                        if check1 and time()-entry>=0.55:
                                            print("bruh melee went way too fast",times_looped)
                                            melee_status=False
                                            cast_allowed=False 
                                        if (not melee_status) and cast_allowed: 
                                            #pyautogui.press('f')
                                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x46, 0)
                                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x46, 0)
                                            #pyautogui.press('5')
                                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x35, 0)
                                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x35, 0)      
                                            last_pressed=time()
                                            latency=latbase
                                        
                            else:
                                ###DBSUN
                                DBsunCurr=scr[624:648,786:813]
                                grayDBsunCurr = cv2.cvtColor(DBsunCurr, cv2.COLOR_BGR2GRAY) 
                                if(False and compare_ssim(grayDBsun, grayDBsunCurr, full=True)[0]>=0.95):
                                    print("WENT TO DB ")
                                    if(True):
                                        #pyautogui.press('e')
                                        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x34, 0)
                                        win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x34, 0)
                                        print("Sunfire")
                                        currSkill+='Sunfire'
                                        last_pressed=time()
                                        latency=latbase+0.12
                                else:###arcane
                                    arcaneCurr=scr[555:608,773:827]
                                    grayarcaneCurr = cv2.cvtColor(arcaneCurr, cv2.COLOR_BGR2GRAY) 
                                    if(compare_ssim(grayarcaneOn, grayarcaneCurr, full=True)[0]>=compare_ssim(grayarcaneOff, grayarcaneCurr, full=True)[0]):
                                        if(True):
                                            #pyautogui.press('1')
                                            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x31, 0)
                                            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x31, 0)
                                            print("arcane")
                                            currSkill+='Arcane Shot'
                                            last_pressed=time()
                                            latency=latbase
                                    else:
                                        ###multi
                                        multiCurr=scr[661:713,718:771]
                                        graymultiCurr = cv2.cvtColor(multiCurr, cv2.COLOR_BGR2GRAY) 
                                        if(compare_ssim(graymultiOn, graymultiCurr, full=True)[0]>=0.9):
                                            if(True):
                                                #pyautogui.press('3')
                                                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x33, 0)
                                                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x33, 0)
                                                print("multi")
                                                currSkill+='Multi Shot'
                                                last_pressed=time()
                                                latency=latbase
                                        else:
                                            ###aimed
                                            aimedCurr=scr[609:661,718:771]
                                            grayaimedCurr = cv2.cvtColor(aimedCurr, cv2.COLOR_BGR2GRAY) 
                                            if(compare_ssim(grayaimedOn, grayaimedCurr, full=True)[0]>=compare_ssim(grayaimedOff, grayaimedCurr, full=True)[0]):
                                                if(True):
                                                    #pyautogui.press('e')
                                                    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x32, 0)
                                                    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x32, 0)
                                                    print("steady")
                                                    currSkill+='Steady Shot'
                                                    last_pressed=time()
                                                    latency=latbase+0.12
                                
        waiter=time()
    if currSkill!='Using: ':
        labelkeep['currRota']=currSkill
        currRota['text']=labelkeep['currRota']
    l_status.update_idletasks()
    l_status.update()
    currRota.update_idletasks()
    currRota.update()
    if cv2.waitKey(1)==ord('q'):
        break
"""

scr=wincap.windowcap()
scr=np.array(scr)
cv2.imshow('frame',scr)
a=scr[555:608,718:771]
#cv2.imwrite('exploshotoff.jpg',a)

#cap.release()
cv2.destroyAllWindows()
explo_on= cv2.imread('exploshoton.jpg', cv2.IMREAD_COLOR)
graExpOn = cv2.cvtColor(explo_on, cv2.COLOR_BGR2GRAY)

explo_off= cv2.imread('exploshotoff.jpg', cv2.IMREAD_COLOR)
grayExpOff = cv2.cvtColor(explo_off, cv2.COLOR_BGR2GRAY)

    
(score, diff) = compare_ssim(graExpOn, graExpOn, full=True)
print("score",score)"""
