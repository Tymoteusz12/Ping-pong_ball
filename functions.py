import pygame
from pygame.math import Vector2

black = (0, 0, 0)
speedMagnitudeRegulation = 20

def redrawWindow(golfball, win, line, winProps):
    win.fill(winProps.backgroundColor)
    golfball.Draw(win)
    pygame.draw.line(win, black, line[0], line[1])
    pygame.display.update()

def findCursorLine(golfball):
    cursorPos = pygame.mouse.get_pos()
    return [(golfball.ballPos.x, golfball.ballPos.y), cursorPos]

def findSpeedVectorMagnitude(golfball):
    cursorPos = pygame.mouse.get_pos()
    speedVector = Vector2(cursorPos[0] - golfball.ballPos.x, cursorPos[1] - golfball.ballPos.y)
    golfball.updateSpeedVector(speedVector / speedMagnitudeRegulation)