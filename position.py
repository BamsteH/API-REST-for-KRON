import time
from gpiozero import LED, Button
from signal import pause
import requests

button1 = Button(1)
button2 = Button(2)
button3 = Button(3)
button4 = Button(4)
button5 = Button(5)
button6 = Button(6)

ledRed = LED(7)
ledGreen = LED(8)


url = 'http://192.168.1.81'
controler = '/controler'
setter = '/set'
startRec = "/startRecording"
stopRec = "/stopRecording"
startPlay = "/startPlayback"

playPos = "playbackPosition"
fps = 60
multiplyFPS = 2

post = request.post('http://127.0.0.1:8080/api/auth/signin', json = {"login":"admin1@test.com",
                                                                     "password":"aaaa"})
print("Hello World")

button1.when_pressed = {
    ledRed.on
    post = requests.post('http://192.168.1.81/control/startLivedisplay', json = {})
    post = requests.post('http://192.168.1.81/control/startRecording', json = {})
    }

button2.when_pressed = {
    post = requests.post('http://192.168.1.81/control/stopRecording')
    post = requests.post('http://192.168.1.81/control/startPlayback', json = {})
    }

button3.when_pressed = {
    post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":60})
    }

button3.when_released = {
    post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":0})
    }

button4.when_pressed = {
    post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":-60})
    }

button4.when_released = {
    post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":0})
    }

button5.when_pressed = {
    post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":60})
    }

button6.when_pressed = {
    post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":-60})
    }


pause()
#post = requests.post('http://192.168.1.81/controler/set', json={"playbackPosition":300})
#post = requests.post('http://192.168.1.81/controler/set', json = {"loopcount":50})
#post = requests.post(url, json={"playbackPosition":100})
#post = requests.post("http://192.168.1.81/control/startLivedisplay")
#time.sleep(5)
#print("record")
#кнопка номер 1 (запись с любого положения)
#post = requests.post("http://192.168.1.81/control/startLivedisplay", json = {})
#post = requests.post('http://192.168.1.81/control/startRecording', json = {})
#time.sleep(5)
#print("play")
#кнока номер 2 (переход в режим playback)
#post = requests.post('http://192.168.1.81/control/stopRecording')
#post = requests.post('http://192.168.1.81/control/startPlayback', json = {})
#нопка номер 3 (переход в воиспроизведение со скоростью 60 кадров)
#time.sleep(3)
#print("play 60fps")
#post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":60})
#кнопка 4 (кадр вправо, кадр влево)
#time.sleep(2)
#post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":-60})
#time.sleep(2)
#post = requests.post('http://192.168.1.81/control/startPlayback', json = {"framerate":0})



#ползунок 1 позиция playback
#ползунок 2 позиция playback framerate

#тумблер х2 playback framerate 

#кнопка 1 запись с индикацией (красный свет)
#кнопка 2 режим playback + (stop rec) (зеленый свет)
#кнопка 3 покадрово назад
#кнопка 4 покадрово вперед
#кнопка 5 playback назад    (желтый свет)
#кнопка 6 playback вперед    (желтый свет)
