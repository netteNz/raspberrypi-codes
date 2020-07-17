from gpiozero import Button, LED, Buzzer
from time import sleep

buzzer = Buzzer(15)
led_red = LED(25)
led_yellow = LED(8)
led_green = LED(7)
button = Button(21)

while True:
    button.wait_for_press()
    led_green.on()
    sleep(1)
    led_yellow.on()
    sleep(1)
    led_red.on()
    sleep(1)
    led_green.off()
    led_yellow.off()
    led_red.off()