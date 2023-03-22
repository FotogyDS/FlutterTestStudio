import PySimpleGUI as sg
import subprocess
import os
import time
import json

sg.theme('DarkGray4')

def main():
    layoutM = [[sg.T("")],[sg.T("")],[sg.T("")],[sg.Button("Start Test Studio", key="stdio", size=(16,1)), sg.Checkbox('Start Appium Server?', default=False, key='srvToggle')],[sg.Button("Change dependencies", key="depnc", size=(16,1))],[sg.Button("Exit", key="Exit", size=(16,1))]]
    windowM = sg.Window("Main Window", layoutM, size=(700,280), element_justification='c', finalize=True)
    while True:
        event, values = windowM.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "depnc":
            changeDependcies()
        elif event == "stdio":
            if values['srvToggle']==True:
                subprocess.Popen("appiumexe.exe")
            testStudio()
    windowM.close()

def changeDependcies():
    layout2= [
        [sg.Text('Enter Driver Setup Details:')],
        [sg.T("")],
        [sg.Text('PlatformName:'),sg.Text(" "),sg.OptionMenu(['Android','IOS'], size=(40,5))],
        [sg.Text('AutomationName:'),sg.OptionMenu(['XCUITest','UIAutomator2','Flutter'], size=(40,5))],
        [sg.Text('PlatformVersion:  '),sg.OptionMenu(['9.0'], size=(40,5))],
        [sg.Text('Devicename:  '),sg.Text("  "),sg.OptionMenu(['226C100747','Emulator-5554'], size=(40,5))],
        [sg.Text('AppPath: '),sg.Text("        "), sg.InputText(), sg.FileBrowse()],
        [sg.T("")],
        [sg.Button('Apply'), sg.Button('Cancel')]]
    window2 = sg.Window("Second Window", layout2,size=(700,280), finalize=True)
    choice = None
    while True:
        event, values = window2.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        elif event == 'Apply':
            new_dict = {
                "platformName": values[0],
                "automationName": values[1],
                "platformVersion": values[2],
                "deviceName": values[3],
                "app": values[4]
            }

            tmp_json = json.dumps(new_dict, indent=4)
            with open('Parameter.json', 'w') as para:
                # print(para.read())
                para.write(tmp_json)
            break
    window2.close()

def testStudio():
    layout1 = [[sg.Text('Commandline:', size=(40, 1))],
            [sg.Output(size=(550, 10), font=('Helvetica 10'))],
            [sg.Button('Create File'),sg.Button('Send',bind_return_key=True),sg.Button('Back', button_color=('red'))]]

    window1 = sg.Window('Appium Test Studio', layout1, size=(700,280), font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False, finalize=True)

    while True:
        event, value = window1.read()
        if event == sg.WIN_CLOSED or event == 'Back':
            subprocess.call("taskkill /F /IM appiumexe.exe", shell=True)
            subprocess.call("taskkill /F /IM node.exe", shell=True)
            break
        if event == 'Send':
            query = value['-QUERY-'].rstrip()
            time.sleep(5)
            if query == 'Create File *':
                #os.system('python LoginTest.py 1')
                subprocess.Popen('{}').__format(input)
                print('Executing Command:{}'.format(query), flush=True)

    window1.close()
main()