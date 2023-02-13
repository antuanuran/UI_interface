import VK
import YD
import configparser
import json
from time import sleep


def dounload_photos(url, amount, printer):
    screen_VK = url
    count_photo = amount

    printer(f'получен НИК VK: {screen_VK} и количество загружаемых фото: {count_photo}')
    sleep(3)

    printer("Функция dounload_photos отработала")


def upload_photos(printer):
    sleep(2)
    printer("Функция upload_photos отработала")



def run_core(url, amount, printer):
    dounload_photos(url, amount, printer)
    upload_photos(printer)


