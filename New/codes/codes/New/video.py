import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

#create fullscreen display 640X480

screen = pygame.display.set_mode((640,480),0)


#find,open start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(640,480))

webcam.start()

while True:

	imagen = webcam.get_image()
	imagen = pygame.transform.scale(imagen,(640,480))
	screen.blit(imagen,(0,0))
	
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			webcam.stop()
			pygame.quit()
       #			sys.exit()

