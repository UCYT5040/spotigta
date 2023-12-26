import os, sys, psutil, pynput, time

# CHANGE BELOW TO YOUR GTA V MUSIC FOLDER (if it isn't the default)
gta_media = os.path.join(os.getenv('USERPROFILE'), 'Documents', 'Rockstar Games', 'GTA V', 'User Music')


def check_gta():
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'GTA5.exe':
                print("Pinging GTA V...")
                for file in proc.open_files():
                    if "little-bass-funk" in file.path:
                        print("Pinged (yes)")
                        return True
                print("Pinged")
        except psutil.AccessDenied:
            pass
    return False


last_state = None

print("Program started")
print("You must have the four little-bass-funk files in your GTA V music folder.")
while True:
    state = check_gta()
    if state != last_state:
        if state:
            print('GTA V has accessed the silence.mp3 file. (Spotify will start soon.)')
        else:
            print('GTA V is not playing music. (Spotify will stop soon.)')
        pynput.keyboard.Controller().press(pynput.keyboard.Key.media_play_pause)
        last_state = state
    time.sleep(1)
