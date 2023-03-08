#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# In[2]:


#定義
def click_button():
    global click, user, password, him_id
    click = False
    if click == False:
        click = True
        user = acc_user.get()
        password = acc_pass.get()
        him_id = tid.get()
        # print(user, password, him_id)
        button_inp.set('已輸入....')
        label_text.set('正在騷擾' + him_id)
    else:
        click = False
        button_inp.set('輸入')
        label_text.set('FB-Massenger騷擾器')
    win.destroy()  # 終止 mainloop 的執行並關閉視窗


# In[11]:


#介面設定

#視窗
win = tk.Tk()
win.title('FB-Massenger騷擾器')
win.geometry('800x300')
win.resizable(False, False) # 如果不想讓使用者能調整視窗大小的話就均設為False

#互動標題
label_text = tk.StringVar()
label_text.set('FB-Massenger騷擾器')
top_text = tk.Label(win, textvariable=label_text, fg='black', font=('Arial', 25), width=20, height=1)
# 說明： bg為背景，font為字型，width為長，height為高，這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高
top_text.pack()

# 創建一個帳號 Frame
acc_frame = tk.LabelFrame(win, text='    帳號        密碼', font=('Arial', 20))
#帳號
acc_user = tk.Entry(acc_frame,bg='white', font=('Arial', 15), width=10)
acc_user.pack(side=tk.LEFT, padx=5, pady=5)
#密碼
acc_pass = tk.Entry(acc_frame,bg='white', font=('Arial', 15), width=10)
acc_pass.pack(side=tk.LEFT, padx=5, pady=5)
# 將 LabelFrame 放到你想要的位置
acc_frame.pack(padx=10, pady=10)

# 創建一個 LabelFrame
id_frame = tk.LabelFrame(win, text="input your target's id", font=('Arial', 15))
#id輸入欄
tid = tk.Entry(id_frame,bg='white', font=('Arial', 15), width=10)
tid.pack(side=tk.LEFT, padx=5, pady=5)
#id輸入按鈕
button_inp = tk.StringVar() # 初始化tk的字串變數
button_inp.set('輸入')
btn = tk.Button(id_frame, bg='white',
                textvariable=button_inp,
                font=('Arial', 10),
                width=10,
                command=click_button)
btn.pack(side=tk.LEFT, padx=5, pady=5)
# 將 LabelFrame 放到你想要的位置
id_frame.pack(padx=10, pady=10)

win.mainloop() # 讓window不斷的重新整理，如果沒有mainloop,就是一個靜態的window


# In[9]:


#登入階段
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)

browser = webdriver.Chrome('chromedriver_win32/chromedriver',chrome_options = options)
browser.get('https://zh-tw.facebook.com/')

time.sleep(2)
user_name = browser.find_element(by='name', value='email')
user_password = browser.find_element(by='name', value='pass')
user_name.send_keys(user)
user_password.send_keys(password)
user_password.send_keys(Keys.CONTROL,'\ue007')

time.sleep(2)
browser.get('https://www.facebook.com/messages/t/'+him_id)

time.sleep(1)

i = 0
while i<5:
    time.sleep(1)
    msg = browser.find_element(By.CSS_SELECTOR, '*[aria-label="訊息"]')
    msg.send_keys('雞雞')
    click = browser.find_element(By.CSS_SELECTOR, '*[aria-label="按 Enter 即可傳送"]')
    click.click()
    i+=1

