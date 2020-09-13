import sys
from ball import pilka
from functions import *
from variables import *

win = pygame.display.set_mode(winProps.resolution)

golfball = pilka(
    ballProperties.ballStartingCoordinates,
    ballProperties.ballRadius,
    ballProperties.ballColor)

while True:
    delta += clock.tick() / 1000.0
    line = findCursorLine(golfball)
    redrawWindow(golfball, win, line, winProps)

    while delta > 1/tickrate:
        delta -= 1/tickrate

        if golfball.isMoving:
            golfball.updatePosition()

            if golfball.hitsWindowVerticalAxes(winProps.resolution):
                golfball.verticalEnergyDispersion()

                if golfball.hasNoEnergy():
                    golfball.mustStop()

            if golfball.hitsWindowLateralAxes(winProps.resolution):
                golfball.horizontalEnergyDispersion()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not golfball.isMoving:
                    golfball.isMoving = True
                findSpeedVectorMagnitude(golfball)

