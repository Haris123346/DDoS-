import httpx
import threading
from colorama import Fore, Style

g = Fore.GREEN
r = Style.RESET_ALL
b = Style.BRIGHT
sent = f"[{Fore.BLUE}{b}>{r}]"
counter = 0


def sendRequest():
    global counter
    client = httpx.Client()
    while True:
        try:
            client.get("enter url")
            counter += 1
            print(f"{sent}{g}{b} Request: {counter} sent...{r}")
        except:
            continue


if __name__ == "__main__":
    threadCount = int(input(f"{sent}{g}{b} Enter your thread count: {r}"))
    threads = [
        threading.Thread(target=sendRequest) for _ in range(threadCount)
    ]
    for thread in threads:
        thread.start()
