
######################################## GUI

######################################## 棒読み確率
import os
import random
import string
import time

######################################## 並列処理
from concurrent.futures import \
    ProcessPoolExecutor  # /マルチスレッド　プロセスが併用　3.2から始まった
from concurrent.futures import ThreadPoolExecutor  # /マルチスレッド　プロセスが併用　3.2から始まった
from multiprocessing import Pipe, Process
######################################## TIKTOK API
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
#######################################　ローカル・グルーバル関数定義 global likeswitch ライク判定のスイッチ
likeswitch = 0
likecount = 0
baniracounts = 0
connectcount = 0 #接続前の文字のために待機　スイッチ
connectcount2 = 0 #読まれるランダム　スイッチ
tiktoksheet1 = 2 #なん行目から書き込みするか
index = 2 

######################################## #現在時刻をコメント

######################################## 

mastername = "@ultrapunks"

#punks5d

#@ultrapunks
#ultrapunks


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

######################################## #BANしたID

patternban = ["jpt0p","saaaya.005","amekun27","japwmdmj_75","user9903321254801","daze639","user4432104597393","goryuhasugoi","user7144765731578","user4574974382222","user2384022314972"]


#鈴木アカウント↓
#goryuhasugoi
#user4432104597393  
#user7144765731578

#user2384022314972


##################################### 特定のひとがコメントしたら 音声を鳴らす
@client.on("comment")
async def on_comment(event: CommentEvent):
    #print(f"{event.user.nickname} -> {event.comment}")
    global connectcount
    global connectcount2
    global tiktoksheet1
    global index
    #storepath = "C://Users/takei/OneDrive/デスクトップ/tiktok/TikTok-Api-master/" # 【//】って二個必要
    if connectcount > 0:
        if event.user.uniqueId in patternban:
            speak_bouyomi("")
        else:
            if connectcount2 == 0:
                speak_bouyomi({event.comment[:20]}) #棒読みちゃんで読ませてる
                coment =(f"{event.comment[:20]}") 
                print(coment)
                return()

    connectcount2 =random.randint(0, 0) #読まれるランダムを検出（0，4）なら01234の数字のどれかを出力

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


