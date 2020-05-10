#coding:utf-8

import serial
import time
import pygame
import sys
import os

# シリアルポートのデバイスファイル名に差し替える
port = '/dev/sekkin'

pygame.mixer.init(44100, -16, 1, 256)

print(__file__)

sekkin = pygame.mixer.Sound(os.path.dirname(__file__) + '/sounds/sekkin.wav')
s = serial.Serial(port, dsrdtr=True)

s.dtr = True
last_state = False

while True:
    try:
        state = s.dsr
    except OSError:
        print('disconnected')
        exit()

    if last_state == False and state == True:
        sys.stdout.flush()
        print('ZAISEN')
        sys.stdout.flush()
        sekkin.play()
        last_state = True

    if state == False:
        last_state = False

    time.sleep(0.01)
