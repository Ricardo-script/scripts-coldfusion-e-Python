robo fechar alert:
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
            if 'Essa página diz' in child.get_properties()['texts']:
                alert = child
                return (chrome, alert)

while True:
    chrome, alert = polling2.poll(get_chrome_alert, step=0.5, poll_forever=True)
    
    fechar = None

    for children in alert.descendants():
        if 'OK' in children.get_properties()['texts']:
            fechar = children
    


    fechar.click_input()
    time.sleep(1)
   
