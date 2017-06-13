from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
import traceback




def appointment_search(email, pw):
    print(email,pw)
    driver = webdriver.Chrome('C:\chromedriver.exe')
    driver.get('https://fr.tlscontact.com/gb/LON/login.php')            #open webpage
    driver.find_element_by_id('email').send_keys('karltannerlegend@yahoo.gr')           #paste  email
    driver.find_element_by_id('pwd').send_keys('sadja6234jehd')         #paste  password
    driver.find_element_by_xpath('//*[@id=\"login_form\"]/div[3]/input').click()            #clicks the 'log in' button
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    el = driver.find_elements_by_xpath('//*[@id=\"ajax_form_status\"]/table/tbody/tr[7]/td[3]/b')           #inserts all appointment options
    appointment_made = False
    keyboard = Controller()

    #javascript executor here in java

    while (not  appointment_made):
        print('while reached')
        try:
            all_appointments = driver.find_elements_by_xpath('//*[@id=\"ajax_form_status\"]/table/tbody/tr[6]/td[3]/table/tbody/tr/td/div/nobr/ul/li/a')
            for i in range(0, len(all_appointments)):
                print(all_appointments[i].text)
                if(all_appointments[i].get_attribute('class') == 'dispo'):
                    print(' available appointment time : ' + all_appointments[i].text)
                    all_appointments[i].click()
                    appointment_made = True

                    time.sleep(3)

                    driver.find_element_by_xpath('//*[@id="ajax_confirm_action"]/center/input[2]').click()        #clicks the 'cancel' button
                    #driver.find_element_by_id('ajaxConfirmCall_submit]').click()       #clicks the 'submit' button
                    break;

        except:
            #in case of exception webpage refreshes
            print("Exception occured...")
            keyboard.press(Key.f5)
            time.sleep(4)
            traceback.print_exc()
        #if an appointment time was not available webpage refreshes and bot starts searching again
        keyboard.press(Key.f5)
        time.sleep(4)
