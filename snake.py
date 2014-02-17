
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import threading
import random
import sys
#python snake.py
# Some api in the chain translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
window = 0
grid=[]
snake=[]
snakeColor=[0.9,0.8,0.2]
c=0
l=0
i=0
j=0

h = 1
v = -1
h1 = 1
v1 = -1
class carre(object):
	def __init__(self,x,y,couleur):
		self.red=couleur[0]
		self.green=couleur[1]
		self.blue=couleur[2]
		self.vertices = [[x,y,0],[x,y+1, 0],[x+1, y+1, 0],[x+1,y, 0]]
	def drawSquare(self):
		glBegin(GL_QUADS)
		glColor3f(self.red, self.green, self.blue)
		for vertex in self.vertices:
			glVertex3f(vertex[0],vertex[1],vertex[2])
		glEnd()

mysquare = carre(0,0, [0.3,0.5,0.1])
mysquare2 = carre(1,0, [0.,1.,0.])


def move():

	threading.Timer(1.2, move).start()
	global i
	global j
	global h
	global v
	global h1
	global v1

	
	
	if len(snake)>3 :
		snake.pop(0)
	if h==1 and  v == v1 :
		i+=1
		

	if h==0 and v == v1 :
		i-=1
	if v==1 and h==h1 :
		j+=1
	if v==0 and h==h1 :
		j-=1

	v1=v
	h1=h
	snake.append(carre(i,j,snakeColor))

	
#	print("H :",h)
#	print("V :",v)
#	print(i)

def InitGL(Width, Height):				
	glClearColor(0.0, 0.0, 0.0, 0.0)	
	glClearDepth(1.0)					
	glDepthFunc(GL_LESS)				
	glEnable(GL_DEPTH_TEST)				
     	glShadeModel(GL_SMOOTH)				
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()				
										
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

	glMatrixMode(GL_MODELVIEW)



def ReSizeGLScene(Width, Height):
	if Height == 0:						
		Height = 1

	glViewport(0, 0, Width, Height)	
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)


# The main drawing function. 
def DrawGLScene():
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glTranslatef(-4., 1.069, -5.) 
        
	
	for item in snake :
		item.drawSquare()
	for item in grid :
		item.drawSquare()
		
	glutSwapBuffers()
	

  


def keyPressed(key, x, y):
	global window
	global h	
	global v
	
	if key == ESCAPE or key == 'q':
		sys.exit()
	
	if  key == 'm':
		
		h = 1

	if  key == 'k':

		h = 0

	if  key == 'l':

		
		v = 0	
	if  key == 'o':

	
		v = 1
		#Faire un compteur pour les n premiers blocs qui font j-1 tandis que les len(snake)-n font i+/-1

#		snake.insert(0,carre(i,j,[1.,1.,0.]))
#		i=i-1
#		if len(snake)>3:
			
#			snake.pop()
		
def main():
	global window
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	
	glutInitWindowSize(1600,900)   #HAUTEUR = 839
	 
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("Snake")
 
	InitGL(1600,900)
   
	glutDisplayFunc(DrawGLScene)
	glutIdleFunc(DrawGLScene)
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(keyPressed)
	glutMainLoop()


move()

for l in [0,1,2,3] :
	for c in [0,1,2,3,4,5,6,7] :
		grid.append(carre(c,0-l,[0.1,0.15,0.53]))  #random.random()
	

main()	
