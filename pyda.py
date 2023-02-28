import wolframalpha
import PySimpleGUI as sg
import pyttsx3

client = wolframalpha.Client("xxx")

sg.theme('Green')
layout =[[sg.Text('Ask a question: '), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('PyDa-Virtual Assistant', layout)

engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res)
    except:
        print("Sorry")

    engine.runAndWait()

    print (values[0])

window.close()