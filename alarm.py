__author__ = 'rsorage'
import mail_snd

from pyfirmata import Arduino, util

port = '/dev/ttyACM0'
board = Arduino(port)

led_red = board.get_pin('d:13:o')
led_green = board.get_pin('d:12:o')
but_disarm = board.get_pin('d:11:i')
sensor_pir = board.get_pin('d:7:i')
act_beeper = board.get_pin('d:3:o')

it = util.Iterator(board)
it.start()

led_green.write(1)
print 'Alarm armed!'

from time import sleep

try:
    while True:
        motion = sensor_pir.read()
        disarm = but_disarm.read()

        if motion is True:
            led_green.write(0)
            led_red.write(1)
            act_beeper.write(1)
            print 'Motion detected!'
            sleep(4)
            #mail_snd.send()
            #sleep(1)

        if disarm is True:
            led_green.write(1)
            led_red.write(0)
            act_beeper.write(0)
            print 'Alarm disarmed!'
            sleep(1)

except KeyboardInterrupt:
    print('Releasing resources ... '),
    board.exit()
    print('Bye!')