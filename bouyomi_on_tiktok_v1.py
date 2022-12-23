######################################## 
import os
import random
import string
import time

######################################## 
from concurrent.futures import \
    ProcessPoolExecutor  
from concurrent.futures import ThreadPoolExecutor 
from multiprocessing import Pipe, Process
######################################## 
from re import A
from this import d
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent

######################################## MIDI用のやつ   
import pygame.midi
import pygame.mixer
import requests
import simpleaudio
import sound
from gtts import gTTS
from playsound import playsound
######################################## MIDIPort
loopMIDI0 = 6 #loopMIDI Port
loopMIDI1 = 7 #loopMIDI Port 1
loopMIDI2 = 8 #loopMIDI Port 2
#######################################　
likeswitch = 0
likecount = 0
baniracounts = 0
connectcount = 0 #接続前の文字のために待機　スイッチ
connectcount2 = 0 #読まれるランダム　スイッチ
tiktoksheet1 = 2 #なん行目から書き込みするか
index = 2 

######################################## ここのIDを書き換えてね

mastername = "@ultrapunks"


client = TikTokLiveClient(f"{mastername}", **{
})
#@punks5d

######################################## #クラインと接続
@client.on("connect")
async def on_connect(_: ConnectEvent):
    global connectcount
    print("Connected to Room ID:", client.room_id)
    print(mastername)
    connectcount += 1

######################################## #BANにしたいアカウントを追加できるよ。

patternban = ["jpt0p","saaaya.005","amekun27","japwmdmj_75","user9903321254801","daze639","user4432104597393","goryuhasugoi","user7144765731578","user4574974382222","user2384022314972"]


##################################### コメントしたら 音声を鳴らす
@client.on("comment")
async def on_comment(event: CommentEvent):

    global connectcount
    global connectcount2
    global tiktoksheet1
    global index

    if connectcount > 0:
        if event.user.uniqueId in patternban:
            speak_bouyomi("")
        else:
            if connectcount2 == 0:
                speak_bouyomi({event.comment[:20]})  #棒読みちゃんに読み上げさせるコメント数をきめてます。
                coment =(f"{event.comment[:20]}") 
                print(coment)
                return()

    connectcount2 =random.randint(0, 0) 
################################################################################################################## bouyomi

def speak_bouyomi(text='ゆっくりしていってね', voice=0, volume=-1, speed=-1, tone=-1):
    res = requests.get(
        'http://localhost:50080/Talk',
        params={
            'text': text,
            'voice': voice,
            'volume': volume,
            'speed': speed,
            'tone': tone})
    return res.status_code


if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=6) as executor:
        executor.submit(on_comment)
        executor.submit(speak_bouyomi)
    client.run()


