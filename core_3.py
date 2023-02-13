from time import sleep


def dounload_photos(url, amount, printer: callable = None):
    printer(f'получен url: {url} и количество: {amount}')
    sleep(2)
    printer("Функция dounload_photos отработала")

def upload_photos(printer: callable = None):
    sleep(2)
    printer("Функция upload_photos отработала")

def run_core(*args, printer: callable = None):
    dounload_photos(*args, printer)
    upload_photos(printer)

