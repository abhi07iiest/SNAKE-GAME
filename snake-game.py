import pygame,sys,random


pygame.init()
clock = pygame.time.Clock()




green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

bg_color = pygame.Color('blue')



screen_width = 960
screen_height = 580
speed_x = 0
speed_y = 0



x = random.randint(10,900)
y = random.randint(10,560)



screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('i will think')

snake_x = screen_width/2
snake_y = screen_height/2

snake_list = []
snake_length = 1
player1_score = 0
#High_score = 0
score_list = []
snake_head = []
game_font = pygame.font.Font("freesansbold.ttf",30)

with open("highscore.txt","r") as hs:
    High_score = hs.read()

eat_sound =  pygame.mixer.Sound('pong.ogg')
out_sound =  pygame.mixer.Sound('score.ogg')


while 1:

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_DOWN:
                 speed_y = 7
                 speed_x = 0

              if event.key == pygame.K_UP:
                  speed_y = -7
                  speed_x = 0

              if event.key == pygame.K_LEFT:

                 speed_x = -7
                 speed_y = 0
              if event.key == pygame.K_RIGHT:

                  speed_x = 7
                  speed_y = 0




     snake_x += speed_x
     snake_y +=  speed_y


     if -7<=snake_x-x <=7 and -7<= snake_y -y <=7:
             pygame.mixer.Sound.play(eat_sound)
             snake_length +=1
             player1_score +=10
             x= random.randint(10,900)
             y = random.randint(10,560)
             snake_length += 7



     screen.fill(bg_color)

     if len(snake_list) > snake_length:
         del(snake_list[0])

     player1_text = game_font.render("SCORE:",False,red)
     screen.blit(player1_text,(10,10))
     player1_text = game_font.render(f"{player1_score}",False,red)
     screen.blit(player1_text,(130,10))

     if int(High_score) < player1_score:
         High_score = player1_score
         with open("highscore.txt","w") as hs:
              hs.write(str(High_score))

     player1_text = game_font.render("HIGH SCORE:",False,red)
     screen.blit(player1_text,(200,10))
     player1_text = game_font.render(f"{High_score}",False,red)
     screen.blit(player1_text,(400,10))



     pygame.draw.rect(screen,red,[x,y,20,20])
     snake_head = []
     snake_head.append(snake_x)
     snake_head.append(snake_y)
     snake_list.append(snake_head)
     for gf,bf in snake_list:
       pygame.draw.rect(screen,black,[gf,bf,20,20])

     if snake_head in snake_list[1:len(snake_list)-1]:
            pygame.mixer.Sound.play(out_sound)
            pygame.quit()













     pygame.display.flip()
     clock.tick(40)
