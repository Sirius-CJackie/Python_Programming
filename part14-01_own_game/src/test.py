import pygame
import random
 
class Game:
    def __init__(self, width=1280, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Robottipeli")
 
        # load images
        self.robot_img = pygame.image.load('robot.png')
        self.coin_img = pygame.image.load('coin.png')
        self.door_img = pygame.image.load('door.png')
        self.monster_img = pygame.image.load('monster.png')
 
        self.clock = pygame.time.Clock()
        self.level = 0
        self.max_levels = 5
        self.running = True
 
        self.bg_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
 
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 48)
 
        self.show_start_screen()
        self.init_game()
 
    
    def show_start_screen(self):
        self.window.fill(self.bg_color)
        instructions = [
            "Welcome to Robot Game!",
            "Objective: Collect all coins and reach the door.",
            "Avoid the monsters! They get faster every level.",
            "Press any key to start."
        ]
        for index, line in enumerate(instructions):
            text = self.big_font.render(line, True, self.text_color)
            self.window.blit(text, (self.width // 2 - text.get_width() // 2, 100 + 50 * index))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
 
 
    def init_game(self):
        self.level += 1
        if self.level > self.max_levels:
            self.display_winning_screen()
            return
        
        self.robot_pos = [50, 50]
        self.door_pos = [random.randint(300, self.width-32), random.randint(300, self.height-32)]
        self.coins = [[random.randint(50, self.width-100), random.randint(50, self.height-100)] for _ in range(5)]
        self.monsters = [[random.randint(300, self.width-32), random.randint(300, self.height-32)] for _ in range(self.level * 2)]
        self.monster_velocities = [[random.choice([-1, 1]) * (1 + 0.2 * self.level), random.choice([-1, 1]) * (1 + 0.2 * self.level)] for _ in range(self.level * 2)]
        self.coins_collected = 0
 
 
    def move_monsters(self):
        for index, monster in enumerate(self.monsters):
            velocity = self.monster_velocities[index]
            monster[0] += velocity[0]
            monster[1] += velocity[1]
 
            # keep monsters in the window
            if monster[0] <= 0 or monster[0] >= self.width - self.monster_img.get_width():
                velocity[0] = -velocity[0]
            if monster[1] <= 0 or monster[1] >= self.height - self.monster_img.get_height():
                velocity[1] = -velocity[1]
 
 
    def move_robot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.robot_pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            self.robot_pos[0] += 5
        if keys[pygame.K_UP]:
            self.robot_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            self.robot_pos[1] += 5
 
    def check_collision(self):
        robot_rect = pygame.Rect(self.robot_pos[0], self.robot_pos[1], self.robot_img.get_width(), self.robot_img.get_height())
 
        # collect coins
        self.coins = [coin for coin in self.coins if not robot_rect.collidepoint(coin[0], coin[1])]
 
        # check door collision
        door_rect = pygame.Rect(self.door_pos[0], self.door_pos[1], self.door_img.get_width(), self.door_img.get_height())
        if robot_rect.colliderect(door_rect) and not self.coins:
            self.init_game()
 
        # check monster collision
        for monster in self.monsters:
            monster_rect = pygame.Rect(monster[0], monster[1], self.monster_img.get_width(), self.monster_img.get_height())
            if robot_rect.colliderect(monster_rect):
                self.running = False  
 
    def draw_game(self):
        self.window.fill(self.bg_color)  
        self.window.blit(self.robot_img, self.robot_pos)
        for coin in self.coins:
            self.window.blit(self.coin_img, coin)
        self.window.blit(self.door_img, self.door_pos)
        for monster in self.monsters:
            self.window.blit(self.monster_img, monster)
 
        level_text = self.font.render(f'Level: {self.level}/{self.max_levels}', True, self.text_color)
        self.window.blit(level_text, (10, 10))
        pygame.display.flip() 
 
    def display_winning_screen(self):
        self.window.fill(self.bg_color)
        win_text = self.big_font.render('You Won!', True, self.text_color)
        self.window.blit(win_text, (self.width // 2 - win_text.get_width() // 2, self.height // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        self.running = False
 
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.move_robot()
            self.move_monsters()
            self.check_collision()
            self.draw_game()
            self.clock.tick(60)
 
        pygame.quit()
 
if __name__ == "__main__":
    game = Game()
    game.run()