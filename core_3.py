from time import sleep


def dounload_photos(url, amount, printer):
    printer(f'получен url: {url} и количество: {amount}')
    sleep(1)
    printer("Функция dounload_photos отработала")

def upload_photos(printer):
    sleep(1)
    printer("Функция upload_photos отработала")

def run_core(url, amount, printer):
    dounload_photos(url, amount, printer)
    upload_photos(printer)


