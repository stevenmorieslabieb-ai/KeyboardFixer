import pystray
from PIL import Image
import pyperclip
import keyboard
import time
import re
arabic_to_english = {
    "ذ":"`",
    "ض":"q",
    "ص":"w",
    "ث":"e",
    "ق":"r",
    "ف":"t",
    "غ":"y",
    "ع":"u",
    "ه":"i",
    "خ":"o",
    "ح":"p",
    "ج":"[",
    "د":"]",
    "ش":"a",
    "س":"s",
    "ي":"d",
    "ب":"f",
    "ل":"g",
    "ا":"h",
    "ت":"j",
    "ن":"k",
    "م":"l",
    "ك":";",
    "ط":"'",
    "ئ":"z",
    "ء":"x",
    "ؤ":"c",
    "ر":"v",
    "لا":"b",
    "ى":"n",
    "ة":"m",
    "و":",",
    "ز":".",
    "ظ":"/",
    }

english_to_arabic = {
    value:key
    for key ,value in arabic_to_english.items()
}
def has_arabic(text):
    for char in text:
        if '\u0600' <= char <= '\u06FF':
            return True

    return False

def convert_mixed_text(text):
    parts = re.split(r"(\s+)", text)

    result = []
    for part in parts:
        if part.isspace():
            result.append(part)

        elif has_arabic(part):
            result.append(convert_to_english(part))

        else:
            result.append(convert_to_arabic(part))
    



    return "".join(result)
def convert_to_english(text):
    result = ""
    i = 0
    while i < len(text):
        two_chars = text[i:i+2]
        if two_chars in arabic_to_english:
            result += arabic_to_english[two_chars]
            i += 2
        elif text[i] in arabic_to_english:
            result += arabic_to_english[text[i]]
            i += 1
        else: 
            result += text[i]
            i += 1

    return result
def convert_to_arabic(text):
    result = ""

    for char in text:
        if char.lower() in english_to_arabic:
            result += english_to_arabic[char.lower()]
        else:
            result += char
    return result
def fix_text():
    print("CTRL+B DETECTED")

    old_text = pyperclip.paste()
    
    pyperclip.copy("")

    keyboard.press_and_release("ctrl+c")

    for _ in range(20):
        time.sleep(0.05)

        new_text = pyperclip.paste()

        if new_text != "":
            break

    else:
        pyperclip.copy(old_text)
        return

    result = convert_mixed_text(new_text)

    pyperclip.copy(result)

    keyboard.press_and_release("ctrl+v")

keyboard.add_hotkey("ctrl+b",fix_text)

print("program is running .....")

def exit_app(icon, item):
    keyboard.unhook_all_hotkeys()
    icon.stop()

image = Image.new("RGB", (30, 30), "black")

icon = pystray.Icon(
    "KeyboardFixer",
    image,
    "KeyboardFixer",
    menu=pystray.Menu(
        pystray.MenuItem("Exit", exit_app)
    )
)
icon.run()



