import machine,time

# "JOIN GAMANZA" in Morse
JOIN_GAMANZA_MORSE = ".--- --- .. -. / --. .- -- .- -. --.. .-";

def displayText():
    led = machine.Pin(25,machine.Pin.OUT);

    timeDot = 1.2/10;
    timeDash = timeDot * 3;
    timeSpace = timeDot * 4;
    timeWord = timeDot * 6;

    led.low();

    for letter in JOIN_GAMANZA_MORSE:
        if letter == '.':
            flash(led,timeDot);
            time.sleep(timeDot);
            continue;
        
        if letter == "-":
            flash(led,timeDash);
            time.sleep(timeDot);
            continue;
        
        if letter == " ":
            time.sleep(timeSpace);
            continue;
        
        if letter ==  "/":
            time.sleep(timeWord);
            continue;
        
    led.low();
    time.sleep(2);
    
def flash(led,t):
    led.high();
    time.sleep(t);
    led.low();
    return

while True:
    displayText();

