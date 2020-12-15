Fechar compartilhar tela:

import pywinauto
import polling2
import time

windows = pywinauto.Desktop(backend="uia").windows(class_name_re='.*Chrome.*', title_re='.*Chrome.*')

def get_chrome_alert():
    global windows
    
    if windows == []:
        windows = pywinauto.Desktop(backend="uia").windows(class_name_re='.*Chrome.*', title_re='.*Chrome.*')
        
    for window in windows:
        alert = None
        chrome = window

        for child in window.children():
            if 'Compartilhar sua tela' in child.get_properties()['texts']:
                alert = child
                return (chrome, alert)

while True:
    chrome, alert = polling2.poll(get_chrome_alert, step=0.5, poll_forever=True)

    tela_inteira = None
    compartilhar = None
    
    

    for children in alert.descendants():
        if 'Compartilhar' in children.get_properties()['texts']:
            compartilhar = children
        if 'A tela inteira' in children.get_properties()['texts']:
            tela_inteira = children
        if 'Cancelar' in children.get_properties()['texts']:
            cancel = children

    #chrome.maximize()
    tela_inteira.click_input()
    #compartilhar.click_input()
    time.sleep(1)
    cancel.click_input()



