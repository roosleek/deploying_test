import requests
from time import sleep
import signal
import sys

def signal_handler(signum, frame):
    print("Получен сигнал остановки. Выполняем завершающие действия...")
    # Выполните необходимые завершающие действия здесь
    cleanup()
    sys.exit(0)  # Завершите скрипт корректно

def cleanup():
    url = f"https://kabiev.ru/send/Script stopped."
    requests.get(url)

signal.signal(signal.SIGTERM, signal_handler)  # Сигнал завершения процесса
signal.signal(signal.SIGINT, signal_handler)   # Сигнал прерывания (Ctrl+C)

def run():
    print("Script started.")
    for i in range(10):
        print(f"iter {i}")
        url = f"https://kabiev.ru/send/{i}"
        requests.get(url)
        sleep(5)
    print("Script stopped.")
        
if __name__=="__main__":
    run()
