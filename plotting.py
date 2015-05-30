from pyfirmata import Arduino, util

port = '/dev/ttyACM0'
board = Arduino(port)

ldr = board.get_pin('a:5:i')

it = util.Iterator(board)
it.start()

from matplotlib import pyplot

pyplot.ion()
pData = [0] * 25
fig = pyplot.figure()
pyplot.title('Real-time LDR reading')
ax1 = pyplot.axes()
l1, = pyplot.plot(pData)
pyplot.ylim([0, 1])

from time import sleep

while True:
    try:
        sleep(1)
        pData.append(float(ldr.read()))
        pyplot.ylim([0, 1])
        del pData[0]
        l1.set_xdata([i for i in xrange(25)])
        l1.set_ydata(pData)
        pyplot.draw()
    except:
        board.exit()
        break