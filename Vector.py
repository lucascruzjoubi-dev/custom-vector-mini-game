from dataclasses import dataclass
import math
import pygame

@dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y) 

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)    

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def magnitude(self):
        return math.hypot(self.x, self.y)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0) 
        return Vector2D(self.x / mag, self.y / mag)

    def __iter__(self):
        return iter((int(self.x), int(int(self.y))))

    def scalar(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector('{self.x}', {self.y})"

a = Vector2D(1, 2)
b = Vector2D(3, 4)

class Inimigo:
    def __init__(self, x, y):
        # Sempre guarde a posição em Float para não perder precisão no DeltaTime
        self.posicao = Vector2D(x, y)
        self.velocidade = 2  # Pixels por segundo
        
        # O Rect do Pygame serve para desenhar e checar colisões
        self.rect = pygame.Rect(x, y, 32, 32)

    def perseguir(self, posicao_player, dt):
        pos_alvo = Vector2D(float(posicao_player.x), float(posicao_player.y))
        # 1. Calcula a direção (Vetor apontando pro Player)
        direcao = posicao_player - self.posicao
        
        # 2. Normaliza (Evita que a velocidade mude com a distância)
        direcao_normalizada = direcao.normalize()
        
        # 3. Multiplica tudo: Direção * Velocidade * Tempo (dt)
        movimento = direcao_normalizada * float(self.velocidade) # * dt
        
        
        # 4. ATUALIZA A POSIÇÃO REAL (Onde a mágica acontece!)
        self.posicao.x +=  movimento.x
        self.posicao.y +=  movimento.y
        
        # 5. Atualiza o Rect usado pelo Pygame para renderizar na tela
        self.rect.x = int(self.posicao.x)
        self.rect.y = int(self.posicao.y)

