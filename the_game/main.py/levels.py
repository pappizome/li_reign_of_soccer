# made by james with help of chat


import pygame as pg
import os

class LevelNode:
    def __init__(self, level_id, x, y, name, unlocked=False):
        self.level_id = level_id
        self.x = x
        self.y = y
        self.name = name
        self.unlocked = unlocked
        self.rect = pg.Rect(x - 15, y - 15, 30, 30)  # clickable area

    def draw(self, surface):
        #defines color for unlocked and locked
        color = (100, 200, 100) if self.unlocked else (100, 100, 100)
        pg.draw.circle(surface, color, (self.x, self.y), 15)
        # Draw level number or icon
        #font and allows us to draw text
        font = pg.font.SysFont("arial", 20)
        #centers text
        text = font.render(str(self.level_id), True, (255, 255, 255))
        surface.blit(text, (self.x - 10, self.y - 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Define level map and if it is unlocked or not
#placement of the levels
LEVEL_MAP = [
    LevelNode(1, 100, 500, "floor1", unlocked=True),
    LevelNode(2, 250, 500, "floor2", unlocked=False),
    LevelNode(3, 200, 350, "floor3", unlocked=False),
    LevelNode(4, 150, 250, "floor4", unlocked=False),
    LevelNode(5, 300, 250, "floor5", unlocked=False),
]

def draw_connections(surface, levels):
    """Draw lines between connected levels"""
    #lines between level pairs
    connections = [(1, 2), (2, 3), (3, 4), (4, 5)]  # level pairs for grey connections
    for l1, l2 in connections:
        node1 = levels[l1 - 1]
        node2 = levels[l2 - 1]
        #draws connection between levels
        pg.draw.line(surface, (150, 150, 150), (node1.x, node1.y), (node2.x, node2.y), 2)