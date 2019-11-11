from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
PIN = 7

dot_time = 0.20




timer = {'.': dot_time, '-': dash_time, ' ': symbol_space}
morse_code_dic = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
               'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-','L': '.-..',
               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-','R': '.-.', 'S': '...', 'T': '-',
               'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..','1': '.----', '2': '..---',
               '3': '...--','4': '....-', '5': '.....', '6': '-....',
               '7': '--...', '8': '---..', '9': '----.', '0': '-----',
               ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
               '-': '-....-', '(': '-.--.', ')': '-.--.-'}





def transmit_dot():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(dot_time)




def transmit_dash():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(dot_time * 3)


def wait_between_signals():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(dot_time)


def wait_between_letters():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(dot_time * 3)


def wait_between_words():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(dot_time * 7)




