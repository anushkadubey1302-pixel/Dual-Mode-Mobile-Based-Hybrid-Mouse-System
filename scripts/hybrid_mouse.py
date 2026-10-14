from flask import Flask, request, render_template
import time
import os
import pyautogui
pyautogui.FAILSAFE = False
app = Flask(__name__)
last_x = None
last_y = None
# Get screen size
screen_width, screen_height = pyautogui.size()


# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move_mouse():
    global last_x, last_y

    data = request.json
    print("MOVE REQUEST:", data)
    x = data.get("x", 0)
    y = data.get("y", 0)

    if last_x is None:
        last_x = x
        last_y = y
        return {"status": "initialized"}

    dx = x - last_x
    dy = y - last_y

    last_x = x
    last_y = y

    sensitivity = data.get("sensitivity", 1.0)

    pyautogui.moveRel(
        int(dx * sensitivity * 4),
        int(dy * sensitivity * 4),
        duration=0
    )

    return {"status": "moved"}
@app.route('/scroll', methods=['POST'])
def scroll_mouse():
    data = request.json
    deltaY = data.get("deltaY", 0)
    
    # More responsive scrolling - lower divisor for faster scrolling
    scroll_amount = int(deltaY / 3)  # Reduced from 5 to 3 for more sensitivity
    
    if scroll_amount != 0:
        pyautogui.scroll(scroll_amount)
    
    return {"status": "scrolled"}
# Click mouse
@app.route('/click', methods=['POST'])
def click_mouse():
    pyautogui.click()
    return {"status": "clicked"}

@app.route('/rightclick', methods=['POST'])
def right_click_mouse():
    pyautogui.rightClick()
    return {"status": "right_clicked"}

@app.route('/doubleclick', methods=['POST'])
def double_click_mouse():
    pyautogui.doubleClick()
    return {"status": "double_clicked"}

@app.route('/middleclick', methods=['POST'])
def middle_click_mouse():
    pyautogui.middleClick()
    return {"status": "middle_clicked"}

@app.route('/drag_start', methods=['POST'])
def drag_start():
    pyautogui.mouseDown()
    return {"status": "drag_started"}

@app.route('/drag_end', methods=['POST'])
def drag_end():
    pyautogui.mouseUp()
    return {"status": "drag_ended"}

@app.route('/type_text', methods=['POST'])
def type_text():
    data = request.json
    text = data.get("text", "")

    pyautogui.write(text)

    return {"status": "typed"}

@app.route('/enter', methods=['POST'])
def enter_key():
    pyautogui.press('enter')
    return {"status": "enter"}

@app.route('/backspace', methods=['POST'])
def backspace_key():
    pyautogui.press('backspace')
    return {"status": "backspace"}

@app.route('/copy', methods=['POST'])
def copy_text():
    pyautogui.hotkey('ctrl', 'c')
    return {"status": "copied"}

@app.route('/paste', methods=['POST'])
def paste_text():
    pyautogui.hotkey('ctrl', 'v')
    return {"status": "pasted"}

@app.route('/selectall', methods=['POST'])
def select_all():
    pyautogui.hotkey('ctrl', 'a')
    return {"status":"ok"}

@app.route('/cut', methods=['POST'])
def cut_text():
    pyautogui.hotkey('ctrl', 'x')
    return {"status":"ok"}

@app.route('/undo', methods=['POST'])
def undo_action():
    pyautogui.hotkey('ctrl', 'z')
    return {"status":"ok"}

@app.route('/redo', methods=['POST'])
def redo_action():
    pyautogui.hotkey('ctrl', 'y')
    return {"status":"ok"}

@app.route('/tab', methods=['POST'])
def tab_key():
    pyautogui.press('tab')
    return {"status":"ok"}

@app.route('/volumeup', methods=['POST'])
def volume_up():
    pyautogui.press('volumeup')
    return {"status": "ok"}

@app.route('/volumedown', methods=['POST'])
def volume_down():
    pyautogui.press('volumedown')
    return {"status":"ok"}

@app.route('/mute', methods=['POST'])
def mute_audio():
    pyautogui.press('volumemute')
    return {"status":"ok"}

@app.route('/playpause', methods=['POST'])
def play_pause():
    pyautogui.press('playpause')
    return {"status":"ok"}

@app.route('/previoustrack', methods=['POST'])
def previous_track():
    pyautogui.press('prevtrack')
    return {"status":"ok"}

@app.route('/nexttrack', methods=['POST'])
def next_track():
    pyautogui.press('nexttrack')
    return {"status":"ok"}

@app.route('/presentation/start', methods=['POST'])
def presentation_start():
    pyautogui.press('f5')
    return {"status":"ok"}

@app.route('/presentation/end', methods=['POST'])
def presentation_end():
    pyautogui.press('esc')
    return {"status":"ok"}

@app.route('/presentation/next', methods=['POST'])
def presentation_next():
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    return {"status":"ok"}

@app.route('/presentation/previous', methods=['POST'])
def presentation_previous():
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')
    return {"status":"ok"}

@app.route('/presentation/black', methods=['POST'])
def presentation_black():
    pyautogui.press('b')
    return {"status":"ok"}

@app.route('/system/notepad', methods=['POST'])
def open_notepad():
    os.system("notepad")
    return {"status":"ok"}

@app.route('/system/calculator', methods=['POST'])
def open_calculator():
    os.system("calc")
    return {"status":"ok"}

@app.route('/system/chrome', methods=['POST'])
def open_chrome():
    os.system("start chrome")
    return {"status":"ok"}

@app.route('/system/lock', methods=['POST'])
def lock_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return {"status":"ok"}

@app.route('/system/screenshot', methods=['POST'])
def screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")
    return {"status":"ok"}

@app.route('/system/alttab', methods=['POST'])
def alt_tab():
    pyautogui.hotkey('alt', 'tab')
    return {"status":"ok"}


if __name__ == '__main__':
    print("🟢 WiFi Server Running...")
    app.run(host='0.0.0.0', port=5000)