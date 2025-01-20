import pygame
import random
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
game_over_font = pygame.font.SysFont("Arial", 64)  # Set font for game over text
level_up_font = pygame.font.SysFont("Arial", 48)   # Set font for level up text

# Define colors
black = (15, 15, 40)
white = (255, 255, 255)

# Define user class
class User:
    def __init__(self):
        self.level = 1
        self.points = 0
        self.hp = 3
        self.coefficient = 0
        self.monster_density = 0.03  # Initial monster generation probability is 30%

    def restart(self):
        """Reset user data"""
        self.points = 0
        self.hp = 3
        self.coefficient = 0

    def add_points(self):
        """Increase user points"""
        self.points += 1

    def add_level(self):
        """Increase user level and monster generation density"""
        self.level += 1
        self.monster_density += 0.03

    def red_hp(self):
        """Reduce user health points"""
        if self.hp >= 1:
            self.hp -= 1
            return True
        else:
            return False

# Define star class
class Star:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = white

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)

# Create stars
stars = []
for _ in range(100):
    x = random.randint(0, 640)
    y = random.randint(0, 380)
    size = random.randint(1, 3)
    stars.append(Star(x, y, size))

pygame.display.set_caption("A rain of coins")
font = pygame.font.SysFont("Arial", 32)

clock = pygame.time.Clock()

robot = pygame.image.load("robot.png")
coin = pygame.image.load("coin.png")
monster = pygame.image.load("monster.png")

position = 0
controls = []
controls.append((pygame.K_LEFT, -5))
controls.append((pygame.K_RIGHT, 5))
key_pressed = {}

list_coins = []
list_monsters = []

user = User()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True

        if event.type == pygame.KEYUP:
            del key_pressed[event.key]

        if event.type == pygame.QUIT:
            quit()

    for key in controls:
        if key[0] in key_pressed:
            position += key[1]
    
    # Generate monsters
    if random.random() < user.monster_density:  
        x = randint(0, 640 - monster.get_width())
        y = randint(-1000, -monster.get_height()) - randint(20, 40)
        list_monsters.append([x, y])

    # Generate coins
    if user.coefficient % 10 == 0:  
        x = randint(0, 640 - coin.get_width())
        y = randint(-1000, -coin.get_height()) - randint(20, 40)
        list_coins.append([x, y])

    window.fill(black)
    for star in stars:
        star.draw()
    window.blit(robot, (position, 480 - robot.get_height()))

    # Handle coins
    for astr in list_coins:
        astr[1] += 2
        window.blit(coin, (astr[0], astr[1]))
        
        if position <= astr[0] + coin.get_width() <= position + robot.get_width() or position <= astr[0] <= position + robot.get_width():
            if 480 - robot.get_height() <= astr[1] + coin.get_height() <= 480 or 480 - robot.get_height() <= astr[1] <= 480:
                astr[1] = 1000
                user.add_points()
                if user.points % 20 == 0 and user.points != 0:
                    level_up_text = level_up_font.render("Level up!", True, (255, 255, 0))  # Yellow text
                    level_up_rect = level_up_text.get_rect(center=(window.get_width() // 2, window.get_height() // 2))  # Centered
                    window.blit(level_up_text, level_up_rect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    user.add_level()
                    list_coins = []
                    list_monsters = []
                    break

    # Handle monsters
    for monst in list_monsters:
        monst[1] += 2
        window.blit(monster, (monst[0], monst[1]))
        
        if position <= monst[0] + monster.get_width() <= position + robot.get_width() or position <= monst[0] <= position + robot.get_width():
            if 480 - robot.get_height() <= monst[1] + monster.get_height() <= 480 or 480 - robot.get_height() <= monst[1] <= 480:
                monst[1] = 1000
                if user.red_hp() == False:
                    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
                    window.blit(game_over_text, (180, 200))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    user.restart()
                    list_coins = []
                    list_monsters = []
                    break
    
    # Draw text info
    text = font.render(f"Points: {user.points}", True, (255, 0, 0))
    text2 = font.render(f"HP:{user.hp}", True, (255, 0, 0))
    text3 = font.render(f"Level:{user.level}", True, (255, 0, 0))
    window.blit(text, (510, 5))
    window.blit(text2, (10, 5))
    window.blit(text3, (280, 5))
    
    pygame.display.flip()

    user.coefficient += 1
 
    clock.tick(60)
