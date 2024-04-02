import pygame
import random
import pytmx
from pytmx.util_pygame import load_pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load the Tiled map
tmx_data = load_pygame("map.tmx")

# Base Entity Class
class Entity(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Player Class
class Player(Entity):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        # Additional player-specific attributes or methods

# Monster Class
class Monster(Entity):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.direction = random.randint(0, 3) # 0: left, 1: right, 2: up, 3: down
        self.steps = random.randint(3, 6) * 32 # Random number of steps

    def move(self):
        direction_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
        dx, dy = direction_list[self.direction]
        self.rect.x += dx
        self.rect.y += dy

        # Collision detection with walls or other monsters
        # Assuming 'walls' is a list of wall rectangles
        collide = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                collide = True
                if dx > 0: # Moving right, hit the left side of wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left, hit the right side of wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down, hit the top side of wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up, hit the bottom side of wall
                    self.rect.top = wall.rect.bottom

        self.steps -= 1
        if collide or self.steps == 0:
            # Change direction and reset steps
            self.direction = random.randint(0, 3)
            self.steps = random.randint(3, 6) * 32

# Spawn the player on a fixed tile
player = Player('player_image.png', 400, 300) # Example fixed position

# Spawn monsters randomly within the map bounds
monsters = pygame.sprite.Group()
for _ in range(10): # Spawn 10 monsters
    x = random.randint(0, tmx_data.width * tmx_data.tilewidth)
    y = random.randint(0, tmx_data.height * tmx_data.tileheight)
    monster = Monster('monster_image.png', x, y)
    monsters.add(monster)

# Create a group for players
all_players = pygame.sprite.Group()
all_players.add(player)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player and monsters
    player.draw(screen)
    monsters.draw(screen)

    # Draw the map
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

    # Update the display
    pygame.display.flip()

    # Player movement based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    # Monster movement
    for monster in monsters:
        monster.move()

    # Check for collisions between players
    collisions = pygame.sprite.groupcollide(all_players, all_players, False, False)
    for player, collided_players in collisions.items():
        # Handle collision logic here
        print(f"Player {player} collided with {len(collided_players)} other players.")

pygame.quit()
