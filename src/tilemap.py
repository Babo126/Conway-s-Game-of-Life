import pygame

from tools import NoiseGenerator
from misc import SpriteSheet
from constants import *

# 定義地形貼圖的裁切區域 (x, y, width, height)
tileTypes = {
    "water": (0, 0, 16, 16),
    "grass1": (16, 0, 16, 16),
    "grass2": (32, 0, 16, 16),
    "sand1": (48, 0, 16, 16),
    "sand2": (64, 0, 16, 16)
}

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.tileSize = TILE_SIZE
        self.image = pygame.transform.scale(image, (self.tileSize, self.tileSize))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Tileset(object):
    def __init__(self):
        self.tileSheet = SpriteSheet(TILE_IMAGE_PATH)
        self.tileImages = {}
        
        # 預先載入並轉換所有地形圖片
        for tileType, tileRect in tileTypes.items():
            self.tileImages[tileType] = self.tileSheet.imageAt(tileRect).convert_alpha()

    def getTileImage(self, tileType):
        return self.tileImages[tileType]

class Terrains(object):
    def __init__(self, width, height):
        self.width, self.height = width, height
        
        # 資源與狀態初始化
        self.tileset = Tileset()
        self.noise = NoiseGenerator()
        
        # 地形閾值設定
        self.threshold_water = 0.3
        self.threshold_sand = 0.35
        # >0.35 則為草地
        
        # 儲存座標與群組
        self.grassCoords = [] 
        self.landTiles = pygame.sprite.Group()
        self.waterTiles = pygame.sprite.Group()
        self.offset = [0, 0]

        self.generateWorldMap(width, height)

    # =================================== 地圖生成邏輯 ===================================
    def generateWorldMap(self, width, height):
        noise2d = self.noise.getNoise2d(width, height) # 柏林噪聲

        for y in range(height):
            for x in range(width):
                noise_val = noise2d[y][x]
                posX, posY = int(TILE_SIZE * x), int(TILE_SIZE * y)

                # 地形類型
                if noise_val < self.threshold_water:
                    # 水域
                    self.waterTiles.add(
                        Tile(posX, posY, self.tileset.getTileImage("water"))
                    )
                elif self.threshold_water <= noise_val < self.threshold_sand:
                    # 沙地
                    self.landTiles.add(
                        Tile(posX, posY, self.tileset.getTileImage("sand1"))
                    )
                elif noise_val >= self.threshold_sand:
                    # 草地 (紀錄座標供牧草生成使用)
                    self.grassCoords.append((x, y))
                    self.landTiles.add(
                        Tile(posX, posY, self.tileset.getTileImage("grass1"))
                    )

    # =================================== 繪製與操作 ===================================
    def draw(self, screen):
        self.landTiles.draw(screen)
        self.waterTiles.draw(screen)

    def shift(self, dx, dy):
        for tile in self.landTiles:
            tile.rect.x += dx
            tile.rect.y += dy

        for tile in self.waterTiles:
            tile.rect.x += dx
            tile.rect.y += dy

        self.offset[0] += dx
        self.offset[1] += dy