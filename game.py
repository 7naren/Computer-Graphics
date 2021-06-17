"""
Snake Game Made with PyGame
"""

import pygame, sys, time, random

#increasing framescount will increase difficulty
framescount = 10

# Window size
frame_size_x = 900
frame_size_y = 500

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('Game successfully initialised')


# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
# Font Style
Font=pygame.font.SysFont('SF Pro', 30)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50], [100-(3*10), 50], [100-(4*10), 50]]

food_pos1 = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_pos2 = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_pos3 = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_pos4 = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = False

direction = 'RIGHT'
change_to = direction

score = 0
num1 = 4
num2 = 5
opr = 2
count = 0
position_list = [(10, 100), (int(frame_size_x /4), 100), (int(frame_size_x / 2), 100), (int(3 * frame_size_x /4), 100), (10, int(frame_size_y / 2)), 
        (int(frame_size_x /4), int(frame_size_y / 2)), (int(frame_size_x /2), int(frame_size_y / 2)), (int(3 * frame_size_x /4), int(frame_size_y / 2))]

# Game Over
def game_over():
    my_font = pygame.font.SysFont('SF Pro', 90)
    game_over_surface = my_font.render('Game Over', True, green)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(white)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, green, 'SF Pro', 40)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = ((frame_size_x / 2), 20)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/2)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    count = count + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Spawning food on the screen
    if not food_spawn or count >= 180:
        
        opr = random.randint(0,3)
        if opr == 2 or opr == 4:
            num1 = random.randrange(2, 10)
            num2 = random.randrange(2, 10)
            num3 = random.randrange(2, 10)
            num4 = random.randrange(2, 10)
        else:
            num1 = random.randrange(1, 10)
            num2 = random.randrange(2, 10) 
            num3 = random.randrange(1, 10)
            num4 = random.randrange(1, 20)   

        pos_list = position_list
        #to evenly and randomly distribute the food throughout the window
        random.shuffle(pos_list)
        x1 = pos_list[0][0]
        x2 = pos_list[1][0]
        x3 = pos_list[2][0]
        x4 = pos_list[3][0]
        x5 = pos_list[4][0]
        x6 = pos_list[5][0]
        x7 = pos_list[6][0]
        x8 = pos_list[7][0]
        y1 = pos_list[0][1]
        y2 = pos_list[1][1]
        y3 = pos_list[2][1]
        y4 = pos_list[3][1]
        y5 = pos_list[4][1]
        y6 = pos_list[5][1]
        y7 = pos_list[6][1]
        y8 = pos_list[7][1]
        xdiff = int ((frame_size_x / 4) - 70)
        ydiff = int ((frame_size_y / 2) - 50)

        food_pos1 = [random.randrange(x1 + 40, (x1 + xdiff)), random.randrange(y1 + 40, (y1 + ydiff))]
        food_pos2 = [random.randrange(x2 + 40, (x2 + xdiff)), random.randrange(y2 + 40, (y2 + ydiff))]
        food_pos3 = [random.randrange(x3 + 40, (x3 + xdiff)), random.randrange(y3 + 40, (y3 + ydiff))]
        food_pos4 = [random.randrange(x4 + 40, (x4 + xdiff)), random.randrange(y4 + 40, (y4 + ydiff))]
        food_pos5 = [random.randrange(x5 + 40, (x5 + xdiff)), random.randrange(y5 + 40, (y5 + ydiff))]
        food_pos6 = [random.randrange(x6 + 40, (x6 + xdiff)), random.randrange(y6 + 40, (y6 + ydiff))]
        food_pos7 = [random.randrange(x7 + 40, (x7 + xdiff)), random.randrange(y7 + 40, (y7 + ydiff))]
        food_pos8 = [random.randrange(x8 + 40, (x8 + xdiff)), random.randrange(y8 + 40, (y8 + ydiff))]
        food_spawn = True
        count = 0
    
    # Snake body moving, growing and reducing mechanism
    # The snake will continue to move in one direction until a button is pressed. 
    # To move the snake, we need to add one unit to the head and remove one unit from the tail.
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] >= (food_pos1[0] - 5) and snake_pos[0] <= (food_pos1[0] + 40) and snake_pos[1] >= (food_pos1[1] - 5) and snake_pos[1] <= (food_pos1[1] + 40):
        score += 1
        food_spawn = False  #growing
    elif snake_pos[0] >= (food_pos5[0] - 5) and snake_pos[0] <= (food_pos5[0] + 40) and snake_pos[1] >= (food_pos5[1] - 5) and snake_pos[1] <= (food_pos5[1] + 40):
        score += 1
        food_spawn = False  #growing
    elif snake_pos[0] >= (food_pos2[0] - 5) and snake_pos[0] <= (food_pos2[0] + 40) and snake_pos[1] >= (food_pos2[1] - 5) and snake_pos[1] <= (food_pos2[1] + 40):
        snake_body.pop()  #reducing
        food_spawn = False
        if len(snake_body) == 1:
            game_over()
        else:
            snake_body.pop() 
    elif snake_pos[0] >= (food_pos6[0] - 5) and snake_pos[0] <= (food_pos6[0] + 40) and snake_pos[1] >= (food_pos6[1] - 5) and snake_pos[1] <= (food_pos6[1] + 40):
        snake_body.pop()  #reducing
        food_spawn = False
        if len(snake_body) == 1:
            game_over()
        else:
            snake_body.pop() 
    elif snake_pos[0] >= (food_pos3[0] - 5) and snake_pos[0] <= (food_pos3[0] + 40) and snake_pos[1] >= (food_pos3[1] - 5) and snake_pos[1] <= (food_pos3[1] + 40):
        snake_body.pop()  #reducing
        food_spawn = False
        if len(snake_body) == 1:
            game_over()
        else:
            snake_body.pop() 
    elif snake_pos[0] >= (food_pos7[0] - 5) and snake_pos[0] <= (food_pos7[0] + 40) and snake_pos[1] >= (food_pos7[1] - 5) and snake_pos[1] <= (food_pos7[1] + 40):
        snake_body.pop()  #reducing
        food_spawn = False
        if len(snake_body) == 1:
            game_over()
        else:
            snake_body.pop() 
    elif snake_pos[0] >= (food_pos4[0] - 5) and snake_pos[0] <= (food_pos4[0] + 40) and snake_pos[1] >= (food_pos4[1] - 5) and snake_pos[1] <= (food_pos4[1] + 40):
        snake_body.pop()  #reducing
        food_spawn = False
        if len(snake_body) == 1:
            game_over()
        else:
            snake_body.pop() 
    elif snake_pos[0] >= (food_pos8[0] - 5) and snake_pos[0] <= (food_pos8[0] + 40) and snake_pos[1] >= (food_pos8[1] - 5) and snake_pos[1] <= (food_pos8[1] + 40):
        snake_body.pop()  #reducing
        food_spawn = False
        if len(snake_body) == 1:
            game_over()
        else:
            snake_body.pop() 
    else:
        snake_body.pop() #no change in length

    # GFX
    game_window.fill(white)
    for pos in snake_body:
        # Snake body
        if pos == snake_body[0]:
            pygame.draw.circle(game_window, black, (pos[0], pos[1]), 12)
        else:
            pygame.draw.circle(game_window, green, (pos[0], pos[1]), 10)    


    # Expression display i.e. snake food
    if opr == 0:
        out = num1 + num2
        ex2out = num3 + num4
        opr_sign = "+"
    elif opr == 1:
        out = num1 - num2
        ex2out = num3 - num4
        opr_sign = "-"
    elif opr == 2:
        out = num1 * num2
        ex2out = num3 * num4
        opr_sign = "*"
    else:
        out = num1 / num2
        out = round(out, 2)
        ex2out = num3 / num4
        ex2out = round(ex2out, 2)
        opr_sign = "/"

    out1 = round(out + 10, 2)
    out2 = round(out - 10, 2)
    out3 = round(out + 15, 2)
    ex2out1 = round(ex2out + 10, 10)
    ex2out2 = round(ex2out - 10, 2)
    ex2out3 = round(ex2out + 15, 2)
    expr1 = str(num1) + "  " + opr_sign + "  " + str(num2)
    expr2 = str(num3) + "  " + opr_sign + "  " + str(num4)

    exp1 = Font.render(expr1, True, blue)
    exp2 = Font.render(expr2, True, blue)
    out_food = Font.render(str(out), True, green, black)
    out1_food = Font.render(str(out1), True, green, black)
    out2_food = Font.render(str(out2), True, green, black)
    out3_food = Font.render(str(out3), True, green, black)
    ex2out_food = Font.render(str(ex2out), True, green, black)
    ex2out1_food = Font.render(str(ex2out1), True, green, black)
    ex2out2_food = Font.render(str(ex2out2), True, green, black)
    ex2out3_food = Font.render(str(ex2out3), True, green, black)

    game_window.blit(exp1, ((frame_size_x / 2) - 300, 20))
    game_window.blit(out_food, (food_pos1[0], food_pos1[1]))
    game_window.blit(out1_food, (food_pos2[0], food_pos2[1]))
    game_window.blit(out2_food, (food_pos3[0], food_pos3[1]))
    game_window.blit(out3_food, (food_pos4[0], food_pos4[1]))
    game_window.blit(exp2, ((frame_size_x / 2) + 200, 20))
    game_window.blit(ex2out_food, (food_pos5[0], food_pos5[1]))
    game_window.blit(ex2out1_food, (food_pos6[0], food_pos6[1]))
    game_window.blit(ex2out2_food, (food_pos7[0], food_pos7[1]))
    game_window.blit(ex2out3_food, (food_pos8[0], food_pos8[1]))

    #out of frame to frame
    if snake_pos[0] < 0:
        snake_pos[0] = frame_size_x - 10
    if snake_pos[0] > frame_size_x-10:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = frame_size_y - 10
    if snake_pos[1] > frame_size_y-10:
        snake_pos[1] = 0

    # Game Over condition    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, green, 'SF Pro', 30)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(framescount)