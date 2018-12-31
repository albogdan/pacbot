import os, sys
import pygame
import level001
import basicSprite
from pygame.locals import *
from helpers import *
from snakeSprite import Snake,Ghost
#from image import *	

# TODO
# > add power pills
# > add cherries etc / powerups
# > choose control of ghost / pacman


clock = pygame.time.Clock()
BLOCK_SIZE = 24

class PyManMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        pygame.init()
	
        """Set the window Size"""
        self.width = width
        self.height = height
	
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
	
	# Setup the variables
	self.collisiontol=5;
	self.collisions=0;

    def MainLoop(self):
        """This is the Main Loop of the Game"""
	self.fdir=(1,1)
	while 1:
		"""Load All of our Sprites"""
		self.LoadSprites();
		
		"""Create the background"""
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0,0,0))
		"""Draw the blocks onto the background, since they only need to be 
		drawn once"""
		self.block_sprites.draw(self.background)
		self.gwall_sprites.draw(self.background)
		
		while 1:
			if self.snake.rect[0]-self.ghost3.rect[0]!=0 and self.snake.rect[1]-self.ghost3.rect[1]!=0:
				self.fdir= ((self.snake.rect[0]-self.ghost3.rect[0])/(abs(self.snake.rect[0]-self.ghost3.rect[0])),(self.snake.rect[1]-self.ghost3.rect[1])/(abs(self.snake.rect[1]-self.ghost3.rect[1])))#,self.ghost.rect,self.ghost2.rect,self.ghost3.rect,self.ghost4.rect\

			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == KEYDOWN: #or event.type == KEYUP
					if ((event.key == K_RIGHT) or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN)):
						self.snake.MoveKeyDown(event.key)

			"""Update the sprites"""        
			self.snake_sprites.update(self.block_sprites)
			self.ghost_sprites.update(self.block_sprites,self.fdir)     
			self.ghost2_sprites.update(self.block_sprites,self.fdir) 
			self.ghost3_sprites.update(self.block_sprites,self.fdir) 
			self.ghost4_sprites.update(self.block_sprites,self.fdir) 
			
			if pygame.sprite.collide_rect(self.ghost,self.snake) or pygame.sprite.collide_rect(self.ghost2,self.snake) or pygame.sprite.collide_rect(self.ghost3,self.snake) or pygame.sprite.collide_rect(self.ghost4,self.snake):
				self.collisions+=1
				if self.collisions==self.collisiontol:
					print "gameover"
					break
			else:
				self.collisions=0

			"""Check for a snake collision/pellet collision"""
			lstCols = pygame.sprite.spritecollide(self.snake, self.pellet_sprites, True)
			"""Update the amount of pellets eaten"""
			self.snake.pellets = self.snake.pellets + len(lstCols)
			self.score=self.snake.pellets
				
			"""Do the Drawing"""               
			self.screen.blit(self.background, (0, 0))
			if pygame.font:
				font = pygame.font.Font(None, 36)
				text = font.render("Score %s" % self.score, 1, (255, 255, 255))
				textpos = [0,550]
				self.screen.blit(text, textpos)
			
			self.pellet_sprites.draw(self.screen)
			self.snake_sprites.draw(self.screen)
			self.ghost_sprites.draw(self.screen)
			self.ghost2_sprites.draw(self.screen)
			self.ghost3_sprites.draw(self.screen)
			self.ghost4_sprites.draw(self.screen)
			pygame.display.flip()
			clock.tick(60)
			#print clock.get_fps()
        
    def LoadSprites(self):
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        x_offset = (BLOCK_SIZE/2)
        y_offset = (BLOCK_SIZE/2)
        """Load the level"""        
        level1 = level001.level()
        layout = level1.getLayout()
	print len(layout[0]),len(layout)
        img_list = level1.getSprites()

        self.pellet_sprites = pygame.sprite.Group()
        self.block_sprites = pygame.sprite.Group()
        self.gwall_sprites = pygame.sprite.Group()

        for y in xrange(len(layout)):
            for x in xrange(len(layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                if layout[y][x]==level1.BLOCK:
                    self.block_sprites.add(basicSprite.Sprite(centerPoint, img_list[level1.BLOCK]))
                elif layout[y][x]==level1.GWALL:
                    self.gwall_sprites.add(basicSprite.Sprite(centerPoint, img_list[level1.GWALL]))
                elif layout[y][x]==level1.SNAKE:
                    self.snake = Snake(centerPoint,img_list[level1.SNAKE])
                elif layout[y][x]==level1.PELLET:
                    self.pellet_sprites.add(basicSprite.Sprite(centerPoint, img_list[level1.PELLET]))
                elif layout[y][x]==level1.GHOST:
                    self.ghost = Ghost(centerPoint,img_list[level1.GHOST])
                elif layout[y][x]==level1.GHOST2:
                    self.ghost2 = Ghost(centerPoint,img_list[level1.GHOST2]) 
                elif layout[y][x]==level1.GHOST3:
                    self.ghost3 = Ghost(centerPoint,img_list[level1.GHOST3])  
                elif layout[y][x]==level1.GHOST4:
                    self.ghost4 = Ghost(centerPoint,img_list[level1.GHOST4])  
        """Create the Snake group"""            
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))                                  
	self.ghost_sprites = pygame.sprite.RenderPlain((self.ghost))      
	self.ghost2_sprites = pygame.sprite.RenderPlain((self.ghost2))    
	self.ghost3_sprites = pygame.sprite.RenderPlain((self.ghost3))
	self.ghost4_sprites = pygame.sprite.RenderPlain((self.ghost4))
