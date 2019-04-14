import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

#create fullscreen display 640X480

screen = pygame.display.set_mode((1366,768),0)


#find,open start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(1366,768))

webcam.start()

while True:

	imagen = webcam.get_image()
	imagen = pygame.transform.scale(imagen,(1366,768))
	screen.blit(imagen,(0,0))
	
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			webcam.stop()
			pygame.quit()
       			#sys.exit()

