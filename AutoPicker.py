import pyautogui as gui
import datetime
import time
import os
'''
pwd=gui.password("请输入软件密码")
if pwd!="easy":
    exit()
'''
os.system("title AutoPicker 版本3.4 作者小雨")
print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "]" , "成功进入主程序 请跟随指引使用程序")
print("************************************************************")
print("* 欢迎使用AutoPicker 本工具专门辅助Orin-Cheat")
print("* Orin-Cheat Telegram交流群https://t.me/OrinCheatop")
print("* 请自行切换到原神游戏窗口")
print("\n* 草神瞳请注意以下几点")
print("1: 角色切换成草主,开启无限Q\n2: 开启无敌\n3: 开启充能2\n4: 开启飞天不落\n5: 开启自动拾取勾选神瞳并将速度设置成1")
print("************************************************************")
print("同意后自动开始") 
gui.alert(text='本软件仅供学习交流 禁止用作违法用途', title='提醒',button = '同意')


def findWindow():
    windows = gui.getWindowsWithTitle("原神")
    if len(windows)==0:
        gui.alert(text="未找到原神窗口")
        raise Exception("原神窗口未找到")
    return windows[0]
genshin=findWindow()
genshin.activate()


def s(key,t):
    gui.hotkey(key)
    time.sleep(t)
    
grass=0
result = gui.confirm('哪个神瞳', buttons=['风', '岩', '雷','草'])
print(result)
if result == '风':
    sum = 66
elif result == '岩':
    sum = 131
elif result == '雷':
    sum = 181
elif result == '草':
    sum = 235
    grass = 1

for i in range(1,sum+1): 
    print("[" , datetime.datetime.now().strftime("%H:%M:%S") , "]" ,"正在收集第" , i , "个神瞳, 还剩下",sum+1-i,"个")
    s('right',0.3)
    s('space',6)    
    if grass==1:#死域
        if i==5 or i==8 or i==70 or i==41 or i==59 or i==73 or i==85 or i==88 or i==92 or i==104:
            s('space',5)
            s('q',4)
    else:
        s('space',2)
    

