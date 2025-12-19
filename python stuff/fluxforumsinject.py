import time
import webbrowser
seconds = 10
for i in range(seconds, 0, -1):
    if i <= 5:
        for dots in range(1, 4):
            print(f"INJECTING VIRUS{'.' * dots}", end="\r", flush=True)
            time.sleep(0.3)
        print("INJECTING VIRUS...   ")
    else:
        print(f"SCARY THING HAPPENING IN {i}")
        time.sleep(0.2)
webbrowser.open("https://fluxforums.net")
