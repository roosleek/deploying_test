import requests
from time import sleep

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