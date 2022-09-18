import os
from tkinter import filedialog
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



loginbase = filedialog.askopenfilename(initialdir="Y:\programing projects\newinstbot",
                                       title="Enter login value",
                                       filetypes=(("text files", "*.txt"),
                                                  ("all files", "*.*")))

passbase = filedialog.askopenfilename(initialdir="Y:\programing projects\newinstbot",
                                      title="Enter pass value",
                                      filetypes=(("text files", "*.txt"),
                                                 ("all files", "*.*")))


wevdrive = filedialog.askopenfilename(initialdir="Y:\programing projects\newinstbot",
                                      title="Enter webdriver",
                                      filetypes=(("text files", "*.exe"),
                                                 ("all files", "*.*")))

os.environ['PATH'] += wevdrive


def buttoncheck() :
    try :
        buter = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        buter.click()
    except :
        print("")
   


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/accounts/emailsignup/")

with open(loginbase) as f :
    lines = f.readlines()

with open(passbase) as q :
    kentwort = q.readlines()





def cheacker() :
    mailcode = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input")
    if mailcode == driver.find_element(By.XPATH,
                                       "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input") :
        print("enter code from mail " + l)
    elif  j == lines[0] :
        print("test complited")


reversecheck = loginbase[: :-1]






def rederect() :
    driver.execute_script("window.open('');")
    sleep(2)
    driver.switch_to.window(driver.window_handles[j])
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    sleep(2)



wait = WebDriverWait(driver, 10)

for k, r in enumerate(kentwort):
    for j, l in enumerate(lines):
        sleep(5)
        buttoncheck()
        sleep(4)
        emaillog = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input")
        emaillog.send_keys(lines[j])
        passlogi = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input")
        passlogi.send_keys(kentwort[k])
        sleep(3)
        randname = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/div/div/button")
        randname.click()
        sleep(3)
        but1 = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button")
        sleep(3)
        but1.click()
        sleep(3)
        DAY = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[4]/div/div/span/span[2]/select")
        DAY.click()
        sleep(3)
        dayselect = driver.find_element(By.XPATH,
                                        "/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[4]/div/div/span/span[2]/select/option[11]")
        dayselect.click()
        year = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[4]/div/div/span/span[3]/select")
        year.click()
        sleep(3)
        yearselect = driver.find_element(By.XPATH,
                                         "/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[4]/div/div/span/span[3]/select/option[31]")
        yearselect.click()
        but2 = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[6]/button")
        but2.click()
        sleep(7)
        sleep(7)
        cheacker()
        sleep(10)
        sleep(5)
        rederect()
        if lines[j] == lines[-1] :
            print(""""""""


                  )
            print("Accounts Created")
            break
    break

