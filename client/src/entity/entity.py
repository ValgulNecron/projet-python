import pygame
import random
import pytmx

def play(screen, tmx_data):
    # Camera variables
    cameraX = 0
    cameraY = 0

    # Base Entity Class
    class Entity(pygame.sprite.Sprite):
        def __init__(self, image_path, x, y):
            super().__init__()
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self, screen):
            # Adjust the entity's position based on the camera's position
            screen.blit(self.image, (self.rect.x - cameraX, self.rect.y - cameraY))

    # Player Class
    class Player(Entity):
        def __init__(self, image_path, x, y):
            super().__init__(image_path, x, y)

    # Monster Class
    class Monster(Entity):
        def __init__(self, image_path, x, y):
            super().__init__(image_path, x, y)
            self.direction = random.randint(0, 3) # 0: left, 1: right, 2: up, 3: down
            self.steps = random.randint(3, 6) * 32 # Random number of steps

        def move(self):
            direction_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
            dx, dy = direction_list[self.direction]
            next_x = self.rect.x + dx
            next_y = self.rect.y + dy

            # Check for collisions with collision_objects
            next_rect = pygame.Rect(next_x, next_y, self.rect.width, self.rect.height)
            for obj_rect in collision_objects:
                if next_rect.colliderect(obj_rect):
                    return # Do not move if the next position would collide with a collision_object

            # Check for collisions with other monsters
            collide = False
            for wall in monsters:
                if wall != self and wall.rect.colliderect(next_rect):
                    collide = True
                    break

            if not collide:
                self.rect.x = next_x
                self.rect.y = next_y

            self.steps -= 1
            if collide or self.steps == 0:
                # Change direction and reset steps
                self.direction = random.randint(0, 3)
                self.steps = random.randint(3, 6) * 32

    # Spawn the player on a fixed tile
    player = Player('Player.png', 400, 300) # Example fixed position

    # Spawn monsters randomly within the map bounds
    monsters = pygame.sprite.Group()
    for _ in range(10): # Spawn 10 monsters
        x = random.randint(0, tmx_data.width * tmx_data.tilewidth)
        y = random.randint(0, tmx_data.height * tmx_data.tileheight)
        i=random.randint(1,5)
        if i==1:
              monster = Monster('monstre1.png', x, y)
        if i==2:
            monster = Monster('monstre2.png', x, y)
        if i==3:
            monster = Monster('monstre3.png', x, y)
        if i==4:
            monster = Monster('monstre4.png', x, y)
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

        # Initialize collision_objects list
        collision_objects = []

        # Populate collision_objects with objects marked for collision
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if obj.properties.get('collision', False):
                        obj_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                        collision_objects.append(obj_rect)

        print(collision_objects)

        # load the collision objects
        for obj_rect in collision_objects:
            pygame.draw.rect(screen, (255, 0, 0), obj_rect.move(-cameraX, -cameraY), 2)
            # add a border around the collision objects

        # Update camera position based on player's position
        cameraX = player.rect.x - screen.get_width() // 2
        cameraY = player.rect.y - screen.get_height() // 2

        # Draw the map
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * tmx_data.tilewidth - cameraX, y * tmx_data.tileheight - cameraY))

        # Draw the player and monsters
        player.draw(screen)
        monsters.draw(screen)
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

        # Check for collisions with collision_objects
        player_rect = pygame.Rect(player.rect.x, player.rect.y, player.rect.width, player.rect.height)
        for obj_rect in collision_objects:
            if player_rect.colliderect(obj_rect):
                # Handle collision here
                print("Collision detected!")

        # Monster movement
        for monster in monsters:
            monster.move()

        # Check for collisions between players
        collisions = pygame.sprite.groupcollide(all_players, all_players, False, False)
        for player, collided_players in collisions.items():
            # Handle collision logic here
            print(f"Player {player} collided with {len(collided_players)} other players.")
            # print player position
            print(player.rect.x, player.rect.y)

    pygame.quit()
