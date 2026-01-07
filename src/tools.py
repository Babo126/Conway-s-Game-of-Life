from random import randint
import numpy as np
import pygame
from perlin_noise import PerlinNoise

class NoiseGenerator(object):
    def __init__(self, seed=0):
        self.seed = seed
        self.isRand = True
        self.randomSeedRange = (0, 100000)
        
        self.octaves_layers = [3, 6, 12, 24] 
        # 權重
        self.layer_weights = [1.0, 0.5, 0.25, 0.125]

    # =================================== 噪聲生成邏輯 ===================================
    def getNoise2d(self, width: int, height: int):
        # 決定種子
        a, b = self.randomSeedRange
        self.seed = randint(a, b) if self.isRand else self.seed
        
        # 初始化各層噪聲生成器
        noises = [PerlinNoise(octaves=oct, seed=self.seed) for oct in self.octaves_layers]

        pic = []
        for i in range(height):
            row = []
            for j in range(width):
                # 疊加多層噪聲
                noise_val = 0
                for idx, noise_obj in enumerate(noises):
                    weight = self.layer_weights[idx]
                    noise_val += weight * noise_obj([i/height, j/width])

                row.append(noise_val)
            pic.append(row)

        return self._normalize(np.array(pic))

    def _normalize(self, ndarr: np.ndarray) -> np.ndarray:
        # 將數值歸一化至 0.0 ~ 1.0
        minimumValue = np.min(ndarr)
        fullRange = np.max(ndarr) - np.min(ndarr)
        # 避免除以零
        if fullRange == 0:
            return ndarr - minimumValue
        return (ndarr - minimumValue) / fullRange

# =================================== 輔助 Debug 工具 ===================================
def debug(info, x=10, y=10):
    font = pygame.font.Font(None, 30)

    debugSurface = font.render(str(info), True, 'White')
    debugRect = debugSurface.get_rect(topleft=(x, y))
    
    screen = pygame.display.get_surface()
    rectSurface = pygame.Surface(debugRect.size)
    rectSurface.set_alpha(64)
    rectSurface.fill((0, 0, 0))
    
    pygame.draw.rect(rectSurface, (0, 0, 0), debugRect)

    screen.blit(rectSurface, debugRect)
    screen.blit(debugSurface, debugRect)