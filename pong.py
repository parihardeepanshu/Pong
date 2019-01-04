import simplegui
import random

height =350 
width = 700      
radius= 15
pad_height = 80
pad_width = 8
half_pad_height = pad_height / 2
half_pad_width = pad_width / 2
left = False
right = True
speed = 1.3
paddle1_speed = 0
paddle2_speed = 0



def create_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [width / 2, height /2]
    ball_vel = [random.randrange(120, 240), random.randrange(60,180)]
    if direction == right:
        ball_vel[1] = -ball_vel[1]
    if direction == left:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]

def start_game():
    global paddle1_pos, paddle2_pos, paddle1_speed, paddle2_speed
    global score1, score2
    score1 = 0
    score2 = 0
    paddle1_pos = height / 2
    paddle2_pos = height / 2
    create_ball(random.choice([left,right]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
  
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
        
   
    if ball_pos[1] <= radius or ball_pos[1] >= height-radius:  
        ball_vel[1] = -ball_vel[1]
        
    if ball_pos[0]-8 <= radius:  
        
        if paddle1_pos - half_pad_height <= ball_pos[1]<=paddle1_pos + half_pad_height:  
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * speed
            ball_vel[1] = ball_vel[1] * speed
        
        else:
            create_ball(right)
            score2 += 1
            
    if ball_pos[0] >= width - radius - pad_width:
        
        if paddle2_pos - half_pad_height <= ball_pos[1] <= paddle2_pos + half_pad_height:
                ball_vel[0] = -ball_vel[0]
        else:
            create_ball(left)
            score1 += 1
            
        
    ball_pos[0] += ball_vel[0]/100
    ball_pos[1] += ball_vel[1]/100
    
    canvas.draw_circle(ball_pos, radius, 2,"Black", "White")
    
 
    if half_pad_height <= paddle1_pos + paddle1_speed <= height - half_pad_height:
        paddle1_pos += paddle1_speed
    if half_pad_height <= paddle2_pos + paddle2_speed <= height - half_pad_height:
        paddle2_pos += paddle2_speed
    
    canvas.draw_line([half_pad_width, paddle1_pos + half_pad_height], [half_pad_width, paddle1_pos - half_pad_height], pad_width, "White")   
    canvas.draw_line([width - half_pad_width, paddle2_pos + half_pad_height], [width - half_pad_width, paddle2_pos - half_pad_height], pad_width, "White")
   
    canvas.draw_text(str(score1) + "     " + str(score2), (width / 2 - 36, 40), 30, "Green")      
    
        
def keydown(key):
    global paddle1_speed, paddle2_speed
    if key == simplegui.KEY_MAP['s']:  
        paddle1_speed = 3  
    elif key == simplegui.KEY_MAP['w']:  
        paddle1_speed = -3  
    elif key == simplegui.KEY_MAP['up']:  
        paddle2_speed = -3  
    elif key == simplegui.KEY_MAP['down']:  
        paddle2_speed = 3 
    pass

def keyup(key):
    global paddle1_speed, paddle2_speed
    if key == simplegui.KEY_MAP['s']:  
        paddle1_speed = 0  
    elif key == simplegui.KEY_MAP['w']:  
        paddle1_speed = 0
    elif key == simplegui.KEY_MAP['up']:  
        paddle2_speed = 0 
    elif key == simplegui.KEY_MAP['down']:  
        paddle2_speed = 0
    
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button2 = frame.add_button('Restart', start_game, 100)

start_game()
frame.start()
