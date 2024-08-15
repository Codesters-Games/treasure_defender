stage.set_background("baseballfield")
treasure = codesters.Sprite("treasurechest", 13, -13)
treasure.set_size(.4)

ninja = codesters.Sprite("ninja2")
ninja.set_size(.4)

# A list of positions where enemies will appear from.
enemies_pos_list = [-250, 250]
# Define a function to create enemies at random positions.
def create_enemies():
    # Create an enemy sprite at a random position from the enemies_pos_list.
    # Title: thief_bde
    # License: 
    # Source: https://cdn.pixabay.com/photo/2013/07/13/10/24/burglar-157142_640.png
    enemy = codesters.Sprite("thief_bde", random.choice(enemies_pos_list), random.randint(-300, 300))
    # Make the enemy move towards treasure.
    enemy.event_collision(enemy_collision)
    enemy.set_speed(1)  # Set the asteroid's speed.
    enemy.set_size(0.3)  # Make the asteroid quite big.
    enemy.glide_to(treasure.get_x(), treasure.get_y())  # Move the asteroid towards Earth.


# Set up the score to 0. This is how many points you have.
score = 0
# Set up lives to 5. You lose one life if you get hit by a thief.
lives = 5
# Treasure also has 5 lives. It loses one each time a thief hits it.
treasure_lives = 5
# create screens to display lives, score, and life if the treasure
score_screen = codesters.Display(score, 200, 200)
lives_screen = codesters.Display(lives, -200, 200)
treasure_lives_screen = codesters.Display(treasure_lives, -200, -200)

# Define what happens when collision happens.
def enemy_collision(sprite, hit_sprite):
    global lives, treasure_lives, score  # Use the global variables for lives, treasure_lives, and score.
    name = hit_sprite.get_image_name()  # Get the name of the sprite that was hit.
    
    if name == "ninja2":  # If the ninja was hit,
        stage.remove_sprite(sprite)  # remove the thief.
        lives -= 1  # Reduce the number of lives by one.
        lives_screen.update(lives)  # Update the display of lives.
        if lives <= 0:  # If no lives are left,
            text = codesters.Text("You Lose", 0, 0, "red")  # show a "You Lose" message.
            text.set_text_size(40)
            stage.remove_all_events()  # Stop all game events.
    if name == "treasurechest":  # If treasure was hit,
        stage.remove_sprite(sprite)  # remove the thief.
        treasure_lives -= 1  # Reduce the number of treasure's lives by one.
        treasure_lives_screen.update(treasure_lives)  # Update the display of treasure's lives.
        if treasure_lives <= 0:  # If treasure has no lives left,
            text = codesters.Text("You Lose", 0, 0, "red")  # show a "You Lose" message.
            stage.remove_all_events()  # Stop all game events.
    if name == "ninja-star_958":  # If the laser hits the thief,
        sprite.set_size(sprite.get_size() - 0.1)  # make the thief smaller.
        if sprite.get_size() < 0.1:  # If the thief is very small,
            stage.remove_sprite(sprite)  # remove it.
            score += 1  # Increase the score by one.
            score_screen.update(score)  # Update the score display.
            if score == 10:  # If the score reaches 10,
                text = codesters.Text("You Win!!!", 0, 0, "green")  # show a "You Win!!!" message.
                text.set_text_size(40)
                stage.remove_all_events()  # Stop all game events.

def shoot():
    ninja_x = ninja.get_x()
    ninja_y = ninja.get_y()
    ninja_direction = ninja.get_direction()
    # Title: ninja-star_958
    # License: 
    # Source: https://cdn.iconscout.com/icon/premium/png-256-thumb/ninja-star-1920872-1627960.png
    ninja_star = codesters.Sprite("ninja-star_958", ninja_x, ninja_y)
    ninja_star.set_size(0.1)
    ninja_star.set_speed(5)
    
    ninja_star.rotate_about(ninja_direction, ninja_x, ninja_y)
    ninja_star.move_forward(500)
    
stage.event_key("space", shoot)

# Define a function called teleport to move the ninja 
# to the opposite side if it goes off-screen.
def teleport(x_pos, y_pos):
    if x_pos > 270:
        ninja.go_to(-260, y_pos)
    if y_pos > 270:
        ninja.go_to(x_pos, -260)
    if x_pos < -270:
        ninja.go_to(260, y_pos)
    if y_pos < -270:
        ninja.go_to(x_pos, 260)

def move_forward():
    x_pos = ninja.get_x()
    y_pos = ninja.get_y()
    ninja.move_forward(25)
    teleport(x_pos, y_pos)
    
def move_back():
    x_pos = ninja.get_x()
    y_pos = ninja.get_y()
    ninja.move_back(25)
    teleport(x_pos, y_pos)
    
def turn_right():
    x_pos = ninja.get_x()
    y_pos = ninja.get_y()
    ninja.rotate_about(10, x_pos, y_pos)
    teleport(x_pos, y_pos)
    
def turn_left():
    x_pos = ninja.get_x()
    y_pos = ninja.get_y()
    ninja.rotate_about(-10, x_pos, y_pos)
    teleport(x_pos, y_pos)

stage.event_key("up", move_forward)
stage.event_key("down", move_back)
stage.event_key("left", turn_left)
stage.event_key("right", turn_right)
 
    
# Make enemies appear every 3 seconds.
stage.event_interval(create_enemies, 3)

