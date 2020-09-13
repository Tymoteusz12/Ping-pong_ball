import pygame
from pygame.math import Vector2

black = (0, 0, 0)

class pilka:
    def __init__(self, coord, radius, color):
        self.ballPos = Vector2(coord)
        self.radius = radius
        self.color = color
        self.velocity = Vector2(0, 0)
        self.gravAcceleration = 0.1
        self.isMoving = False

    def Draw(self, win):
        pygame.draw.circle(win, black, (int(self.ballPos.x), int(self.ballPos.y)), self.radius)
        pygame.draw.circle(win, self.color, (int(self.ballPos.x), int(self.ballPos.y)), self.radius-1)

    def updatePosition(self):
        self.ballPos.x += self.velocity.x
        self.ballPos.y += self.velocity.y
        self.velocity.y += self.gravAcceleration

    def hitsWindowVerticalAxes(self, winResolution):
        return self.ballPos.y > winResolution[1] - self.radius or self.ballPos.y < self.radius

    def hitsWindowLateralAxes(self, winResolution):
        return self.ballPos.x < self.radius or self.ballPos.x > winResolution[0] - self.radius

    def verticalEnergyDispersion(self):
        self.velocity.x /= 1.2
        self.velocity.y /= -1.3
        self.updatePosition()

    def horizontalEnergyDispersion(self):
        self.velocity.x /= -1.2
        self.updatePosition()

    def updateSpeedVector(self, speedVector):
        self.velocity.x = speedVector.x
        self.velocity.y = speedVector.y

    def hasNoEnergy(self):
        return abs(self.velocity.x) < 0.1 and abs(self.velocity.y) < 0.1

    def mustStop(self):
        self.ballPos.y = 394
        self.isMoving = False


