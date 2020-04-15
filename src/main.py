from algorithms import *
import pygame
import random
import time
import sys

# initializing display
screen = pygame.display.set_mode((500, 400))

# global variables
white = ((255, 255, 255))
black = ((0, 0, 0))
red = ((255, 0, 0))
green = ((0, 255, 0))
blue = ((0, 0, 255))

# spriteGroups
bubble_group = pygame.sprite.Group()

class BarItem(pygame.sprite.Sprite):
	def __init__(self, height, color, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def update(self):
		self.rect.x = self.x
		self.rect.y = self.y

class drawBubbleSort():
	def __init__(self):
		self.items = [random.randint(0, 1000) for i in range(10)]
		self.color = green
		self.surfaces = []
		self.x = []
		self.y = []
		self.rect = None

	def sort(self):
		length = len(self.items)
		for i in range(0, length-1):
			swapped = f=False

			for j in range(0, length-1):
				if self.items[j] > self.items[j+1]:
					self.items[j], self.items[j+1] = self.items[j+1], self.items[j]
					for i in self.items:
						bubble_group.add(BarItem(i, self.color, len(bubble_group)*10, 100))
					swapped = True
			if not swapped:
				break

	def draw(self, image, x, y):
		screen.blit(image, (x, y))

bubble = drawBubbleSort()

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit(0)

	# update details
	screen.fill(black)

	bubble.sort()

	bubble_group.draw(screen)
	bubble_group.update()

	# updating display
	pygame.display.update()