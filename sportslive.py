import webbrowser


def watch_live_sports_stream(text=""):
    if text == "boxing":
        webbrowser.open("http://www.stream2watch.cc/livenow/boxing/")  # opens up the webbrowser for the specified link
    elif text == "wrestling":
        webbrowser.open("http://www.stream2watch.cc/livenow/wrestling/")  # opens up the link for the wresting
    elif text == "athletics":
        webbrowser.open("http://www.stream2watch.cc/livenow/athletics/")
    elif text == "basketball":
        webbrowser.open("")
    elif text == "beach soccer":
        webbrowser.open("http://www.stream2watch.cc/livenow/beach-soccer/")
    elif text == "baseball":
        webbrowser.open("http://www.stream2watch.cc/livenow/baseball/")
    elif text == "cricket":
        webbrowser.open("http://www.stream2watch.cc/livenow/crick/")
    elif text == "UFC":
        webbrowser.open("http://www.stream2watch.cc/livenow/ufc/")
    elif text == "hockey":
        webbrowser.open("http://www.stream2watch.cc/livenow/hockey/")
    elif text == "snooker":
        webbrowser.open("http://www.stream2watch.cc/livenow/snooker/")
    elif text == "football":
        webbrowser.open("http://www.stream2watch.cc/livenow/football/")
