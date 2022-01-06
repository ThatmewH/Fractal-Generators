import numpy as np
import scipy.misc as smp
import time
import math
import winsound
width = 500
height = 500
data = np.empty( (height,width,3), dtype=np.uint8 )

imageStartTime = time.time()
totalTimeStart = time.time()
def numMap(value, oldRangeMax, oldRangeMin, newRangeMax, newRangeMin):
    oldRange = oldRangeMax - oldRangeMin
    newRange = newRangeMax - newRangeMin
    return (((value - oldRangeMin) * newRange) / oldRange) + newRangeMin

def drawScreen(width, height, scale, maxItterations):
    global data, imageStartTime
    imageStartTime = time.time()
    for y in range(height):
        for x in range(width):
            inSet = True
            xScaled = numMap(x-scroll[0], 0, width, -scale, scale) + scroll[0]
            yScaled = numMap(y-scroll[1], 0, height, -scale, scale) + scroll[1]
            originalxS = xScaled
            originalyS = yScaled

            brightness = 0
            n = 0
            while n < maxItterations:
                aa = xScaled*xScaled - yScaled*yScaled
                bb = 2*xScaled*yScaled

                xScaled = aa + originalxS
                yScaled = bb + originalyS

                if (xScaled*xScaled+yScaled*yScaled) > 4:
                    inSet = False
                    break
                brightness += 1
                n += iterationIncrement
            if inSet:
                data[y][x] = [0,0,0]
            else:
                brightness = numMap(brightness,maxItterations,0,255,0)
                # brightness = numMap(1,maxItterations,brightness*(1/iterationIncrement),255,0)
                data[y][x] = [brightness, 0, 0]
        # if y%int(height*0.05) == 0:
        #     print("LOADING: " + str(y/height * 100) + "%")
num = 0
maxNum = 100

iterations = 100
iterationIncrement = 1

scroll = [-1.156268466747, -0.278924214146] # [-1.156268466747,-0.278924214146] # [- 0.7746806106269039,- 0.1374168856037867]
scale = 1.5

# Initalise Variables
for x in range(num):
    scale *= 0.3
    # iterations += iterationIncrement

while num < maxNum:
    drawScreen(width, height, scale, iterations)
    img = smp.toimage( data )       # Create a PIL image
    img.save("fractalZoom/fractal_" + str(num) + ".png")
    # scale *= 0.3
    print("Images Done: " + str(num) + ", " + str(time.time()-imageStartTime))
    num+=1
    # iterations += iterationIncrement
print("\nTotal Time: " + str(time.time()-totalTimeStart))
# winsound.Beep(1000, 100)
# img.show()
