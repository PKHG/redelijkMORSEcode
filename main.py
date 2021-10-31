start = 0
elapsed = 0
"""
def on_button_pressed_a():
    global start
    looptijd = 0
    start = looptijd
input.on_button_pressed(Button.A, on_button_pressed_a)
"""
"""
def on_button_pressed_b():
    global elapsed
    elapsed = input.running_time() + start
    basic.show_number(Math.idiv(elapsed, 1000))
input.on_button_pressed(Button.B, on_button_pressed_b)
"""
def on_button_pressed_a():
    global StringA, StringB, StringAenB, tellerAenB, tellerA
    basic.show_number(len(StringAenB))
    basic.clear_screen()
    if len(StringAenB) > 5:
        basic.show_icon(IconNames.SAD)
        basic.pause(1000)
        basic.show_string("overnieuw!")
        StringA = "."
        StringB = "-"
        StringAenB = ""
        basic.pause(1000)
    else:
        tellerAenB = tellerAenB + 1
        tellerA = tellerA + 1
        StringAenB = "" + StringAenB + "."
        basic.show_string(StringAenB)
        basic.show_number(tellerAenB)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global waarAlphabet, StringAenB, tellerAenB, tellerA, tellerB
    try:
        waarMorse = morse.index(StringAenB)
        waarAlphabet = alphabet[waarMorse]
        basic.clear_screen()
        basic.show_string(StringAenB)
        basic.show_icon(IconNames.HEART)
        basic.show_number(tellerAenB)
        basic.show_string("" + (waarAlphabet))
        StringAenB = ""
        tellerAenB = 0
        tellerA = 0
        tellerB = 0
    except:
        StringAenB = ""
        tellerAenB = 0
        tellerA = 0
        tellerB = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global StringA, StringB, StringAenB, tellerAenB, tellerB
    basic.show_number(len(StringAenB))
    basic.clear_screen()
    if len(StringAenB) > 5:
        basic.show_icon(IconNames.SAD)
        basic.pause(1000)
        basic.show_string("overnieuw!")
        StringA = "."
        StringB = "-"
        StringAenB = ""
        basic.pause(1000)
    else:
        tellerAenB = tellerAenB + 1
        tellerB = tellerB + 1
        StringAenB = "" + StringAenB + "-"
        basic.show_string(StringAenB)
        basic.show_number(tellerAenB)
input.on_button_pressed(Button.B, on_button_pressed_b)

waarAlphabet = ""
tellerAenB = 0
StringB = ""
StringA = ""
alphabet: List[str] = []
tellerA = 0
tellerB = 0
StringAenB = ""
StringAenB = ""
tellerB = 1
tellerA = 1
morse = [".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
    "-----"]
alphabet = ["A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"]
