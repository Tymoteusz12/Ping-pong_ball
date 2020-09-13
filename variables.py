import pygame
from typing import NamedTuple

pygame.init()
clock = pygame.time.Clock()
delta = 0
tickrate = 120

class ballConst(NamedTuple):
    ballRadius: int = 6
    ballStartingCoordinates: tuple = (400, 394)
    ballColor: tuple = (255, 255, 255)

class WindowProps(NamedTuple):
    resolution: tuple = (800, 400)
    backgroundColor: tuple = (0, 150, 150)

ballProperties = ballConst()
winProps = WindowProps()


