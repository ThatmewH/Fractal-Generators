import numpy as np
import scipy.misc as smp
import time
import math
width = 12000
height = 12000
data = np.empty( (height,width,3), dtype=np.uint8 )

imageStartTime = time.time()
totalTimeStart = time.time()
def numMap(value, oldRangeMax, oldRangeMin, newRangeMax, newRangeMin):
    oldRange = oldRangeMax - oldRangeMin
    newRange = newRangeMax - newRangeMin
    return (((value - oldRangeMin) * newRange) / oldRange) + newRangeMin

def drawScreen(width, height, scale, maxItterations, cx, cy, realScale):
    global data, imageStartTime
    imageStartTime = time.time()
    for y in range(height):
        for x in range(width):
            inSet = True
            zx = numMap(x - (width/2 - width/2/realScale) - scroll[0], 0, width/realScale, -scale, scale)
            zy = numMap(y - (height/2 - height/2/realScale) - scroll[1], 0, height/realScale, -scale, scale)

            brightness = 0
            n = 0
            if not(y < width*0.2 or y > width*0.8):
                while n < maxItterations and (zx**2 + zy**2) < scale*scale:
                    xtemp = (zx * zx) - (zy * zy) + cx
                    zy = (2 * zx * zy) + cy
                    zx = xtemp

                    brightness += 1
                    n += iterationIncrement
                if n > maxItterations:
                    data[y][x] = [0,0,0]
                else:
                    brightness = numMap(brightness, 0, maxItterations, 1, 500)

                    data[y][x] = [brightness, brightness//2, 0]
            else:
                data[y][x]=[0,0,0]
        if y%int(height*0.05) == 0:
            print("LOADING: " + str(y/height * 100) + "%")
num = 0
maxNum = 1


iterations = 500
iterationIncrement = 1

scroll = [0,0] # [-1.156268466747,-0.278924214146] # [- 0.7746806106269039,- 0.1374168856037867]
scale = 2
realScale = 0.75
cx = -0.7
cy = 0.27015
angle = 0

# Initalise Variables
for x in range(num):
    scale *= 0.3
    # iterations += iterationIncrement

while num < maxNum:
    drawScreen(width, height, scale, iterations, cx, cy, realScale)
    img = smp.toimage( data )       # Create a PIL image
    img.save("fractalZoom/fractal_" + str(num) + ".png")
    cx = 0.7855*math.e**math.radians(angle)
    cy = 0.7855*math.e**math.radians(angle)
    angle += 1
    print("Images Done: " + str(num) + ", " + str(time.time()-imageStartTime))
    num+=1
print("\nTotal Time: " + str(time.time()-totalTimeStart))
