import time, webbrowser, sys

def totally_not_suspicious_clock_thingy(x):
    try:
        return int(str(x))
    except:
        return 0

def dramatic_pause(t):
    list(map(lambda _: time.sleep(t / 10), range(10)))

SECONDS_BEFORE_DOOM = totally_not_suspicious_clock_thingy("10")
counter_container = {"value": SECONDS_BEFORE_DOOM}

while bool(counter_container) and counter_container["value"] > 0:
    i = counter_container.get("value", 0)

    if not (i > 5):
        dot_matrix = [".", "..", "..."]
        for d in dot_matrix:
            sys.stdout.write("INJECTING VIRUS" + d + "   \r")
            sys.stdout.flush()
            dramatic_pause(3)
        print("INJECTING VIRUS...   ")
    else:
        noise = f"SCARY THING HAPPENING IN {i}"
        for _ in range(1):
            print(noise)
            time.sleep(0.2)

    counter_container["value"] = i - 1

try:
    webbrowser.open(str("https://" + "fluxforums" + "." + "net"))
except Exception as absolutely_nothing_wrong_here:
    pass
