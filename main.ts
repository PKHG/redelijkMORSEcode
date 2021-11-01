input.onPinPressed(TouchPin.P0, function () {
    basic.clearScreen()
    clearallGlobals()
    basic.showIcon(IconNames.Square)
    basic.pause(1000)
    basic.clearScreen()
})
function clearallGlobals () {
    StringA = "."
    StringB = "-"
    StringAenB = ""
    tellerA = 0
    tellerB = 0
    tellerAenB = 0
    alleletterSamen = ""
}
function allestonen () {
    alleletterSamen = "" + alleletterSamen + StringAenB
    basic.showString(alleletterSamen)
}
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    if (StringAenB.length > 5) {
        basic.showIcon(IconNames.Sad)
        basic.pause(1000)
        basic.showString("overnieuw!")
        clearallGlobals()
    } else {
        tellerAenB = tellerAenB + 1
        tellerA = tellerA + 1
        StringAenB = "" + StringAenB + "."
        basic.showString(".")
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.showString(alleletterSamen)
})
input.onButtonPressed(Button.AB, function () {
    let waarMorse: number;
try {

        waarMorse = _py.py_array_index(morse, StringAenB)
        waarAlphabet = alphabet[waarMorse]
        basic.clearScreen()
        basic.showString(StringAenB)
        basic.showIcon(IconNames.Heart)
        basic.showNumber(tellerAenB)
        basic.showString("" + waarAlphabet)
        basic.pause(500)
        basic.clearScreen()
        basic.pause(500)
        StringAenB = ""
        tellerAenB = 0
        tellerA = 0
        tellerB = 0
        alleletterSamen += waarAlphabet
        basic.showString(alleletterSamen)
        alleletterSamenCopy =  alleletterSamen
    }
    catch (_) {
        StringAenB = ""
        tellerAenB = 0
        tellerA = 0
        tellerB = 0
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    if (StringAenB.length > 5) {
        basic.showIcon(IconNames.Sad)
        basic.pause(1000)
        basic.showString("overnieuw!")
        clearallGlobals()
    } else {
        tellerAenB = tellerAenB + 1
        tellerB = tellerB + 1
        // StringAenB = "" + StringAenB + "-"4"
        StringAenB = "" + StringAenB + "-"
        basic.showString("-")
    }
})
let StringB = ""
let StringA = ""
let alleletterSamenCopy = ""
let alleletterSamen = ""
let StringAenB = ""
let tellerB = 0
let tellerA = 0
let alphabet: string[] = []
let tellerAenB = 0
let waarAlphabet = ""
let elapsed = 0
let start = 0
let herhaal = 1
StringAenB = ""
tellerB = 1
tellerA = 1
let morse = [
".-",
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
"-----"
]
alphabet = [
"A",
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
"0"
]
