import pygame as pg
from pygame.locals import *
import time
size = 50
bg_white = (112,128,144)
bg_black = (47,79,79)


def checker(per):
    i=len(per)-1
    for j in range(i):
        if( i-j == abs(per[i]-per[j])):
            return False
    return True

def solver(per, n, ans=False):
    if(len(per)==n):
        return per
     
    for i in range(n):
        if i not in per:
            per.append(i)
            
            if(checker(per)):
                ans=solver(per,n)
                if(ans):
                    return ans

            per.pop()
    return ans

def drawSoln(screen, soln, posArray):
	img = pg.transform.scale(pg.image.load('Assignment 1\queen.png'), (size,size))
	col = 0
	print(soln)
	for i in soln:
		time.sleep(0.7)
		x,y = posArray[col][i]
		screen.blit(img, (x,y))
		col+=1
		pg.display.update()

def main():
	screen = pg.display.set_mode((800,200))
	icon = pg.image.load('Assignment 1\logo.png')
	pg.display.set_icon(icon)
	pg.display.update()
	n=8
	done = False
	screen.fill(bg_black)
	screen = pg.display.set_mode((size*n, size*n))
	pg.display.set_caption('Assignment 1')
	posArray = []
	
	for x in range(n):
		tempPos = []
		for y in range(n):
			tempPos.append((size*(x), size*(y)))
			if((x+y)&1^1):
				pg.draw.rect(screen, bg_white, (x*size, y*size, size, size))
		posArray.append(tempPos)
	
	soln = solver([], n)
	
	if soln:
		drawSoln(screen, soln, posArray)
	else:
		screen = pg.display.set_mode((800,200))
		font = pg.font.Font(None, 32)
		surf = font.render("Solution does not Exist!", True, (0,0,0), bg_black)
		rect = surf.get_rect()
		rect.center = (400, 100)
		screen.blit(surf,rect)
	
	pg.display.update()
	
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True



if __name__=="__main__":
	pg.init()
	main()
	pg.quit()