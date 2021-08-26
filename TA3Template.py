import pygame
import random
#Import time module
import time

pygame.init()

#Create image loading function here
def image_load(location,length,width):
    img=pygame.image.load(location).convert_alpha()
    img_scaled=pygame.transform.smoothscale(img,(length,width))
    return img_scaled

#Create text display function here






size = (350, 400)
screen = pygame.display.set_mode(size)
carx=60
cary=340
#Create variables
car2x=130
car2y=200
threshold=0
roadx=-10
roady=0
threshold=0
#Create a counter variable
counter=0

x_choice=[150,200]
x=random.choice(x_choice)
y=random.randint(50,cary-100)

#Replace file location address on your computer
road=image_load("Assets/road.png",400,800)

#Replace file location address on your computer
car=image_load("Assets/yellowCar.png",70,60)

#Replace file location address on your computer
stone=image_load("Assets/stone.png",70,60)


carryOn = True

#Create timepoint t1 here
t1=time.time()


while carryOn:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False
  
  screen.blit(road,(roadx,roady))
  screen.blit(car,(carx,cary))
  #screen.blit(car2,(car2x,car2y))
  
  

  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_UP:
        cary-=2
        roady-=1
    if event.key==pygame.K_DOWN:
        cary+=2
    if event.key==pygame.K_LEFT:
        carx-=2
    if event.key==pygame.K_RIGHT:
        carx+=2

  if cary<=0:
    #Increment counter by 1
    counter+=1
    roady=0
    cary=340
    x=random.choice(x_choice)
    y=random.randint(50,cary-100)
  car_rect=car.get_rect(topleft=(carx,cary))
  stone_rect=stone.get_rect(topleft=(x,y))
  #Create rectangle for car2
  car2_rect=car2.get_rect(topleft=(car2x,car2y))

  if car_rect.collidepoint(stone_rect.x,stone_rect.y):
    cary=360
  #Check for collision
  if car_rect.collidepoint(car2_rect.x,car2_rect.y):
    cary=360
  
  screen.blit(stone,[x,y])
  #Create second time point here
  t2=time.time()
  #Evaluate gametime here
  game_time=t2-t1
  game_time=round(game_time,2)
  
  #Replace code
  #Display gametime here
  #Select font
  font = pygame.font.Font(None, 24)
  #Select text.Remember to concatenate gametime
  text = font.render("TIME ELAPSED: " + str(game_time)+"seconds", 1, (255,0,255))
  #Display the text
  screen.blit(text, (50,10))

  #Display distance
  distance=counter*6
  font = pygame.font.Font(None, 24)
  text = font.render("DISTANCE: " + str(distance)+"km", 1,(255,255,0))
  screen.blit(text, (50,30))



  #Check if Key is pressed
  if event.type==pygame.KEYDOWN:
  #Check if key pressed is "Enter"
        if event.key==pygame.K_RETURN:
        #Check if game time is within threshold
            if game_time>=threshold and game_time<=(threshold+10):
                    #Decrement "cary" to make car move forward
                    cary-=10 
                    #Increment "threshold" by 10
                    threshold+=10
  
  
  #check if counter is equal to 100
  if counter>=5:
    #Create the finish line rectangle
    finishline=pygame.Rect(50,40,240,20)
    #Draw the rectangle
    pygame.draw.rect(screen,(255,255,255),finishline)
    font = pygame.font.Font(None, 20)
    text = font.render("FINISH", 1,(255,0,0))
    screen.blit(text, (150,40))

  if counter>=5 and cary<=50:
    pygame.time.wait(2000)
    screen.fill((0,100,255))
    font = pygame.font.Font(None, 34)
    text = font.render("Finish time:"+str(round(game_time,2))+"seconds", 1,(255,100,0))
    screen.blit(text, (50,200))
    pygame.display.flip()
    pygame.time.wait(2000)
    break
  
  pygame.display.flip()
  
pygame.quit()
