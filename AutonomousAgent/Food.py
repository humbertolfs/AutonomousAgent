class Food():
    def __init__(self, x, y):
        self.localAtual = PVector(x, y)
        self.velocidade = PVector(0, 0)
        self.aceleracao = PVector(0, 0)
        
        self.r = 6
        self.velMaxima = 1.0
        self.forcaMaxima = 0.01
        self.opacidade = 255
        self.bg = 0

    def update(self):
        self.velocidade.add(self.aceleracao)
        self.velocidade.limit(self.velMaxima)
        self.localAtual.add(self.velocidade)
        self.aceleracao.mult(0)

    def applyForce(self, force):
        self.aceleracao.add(force)

    def display(self):
        theta = self.velocidade.heading()
        
        if self.opacidade <= 80:
            self.opacidade = 255
            self.bg = (self.bg + 1) % 5
        else:
            self.opacidade = self.opacidade - 12
        
        if (self.bg == 0):
            fill(255, 0, 255, self.opacidade)
        elif (self.bg == 1):
            fill(255, 255, 0, self.opacidade)
        elif (self.bg == 2):
            fill(255, 0, 0, self.opacidade)
        elif (self.bg == 3):
            fill(0, 255, 0, self.opacidade)
        elif (self.bg == 4):
            fill(0, 0, 255, self.opacidade)
            
        noStroke()
        with pushMatrix():
            translate(self.localAtual.x - self.r / 2, self.localAtual.y - self.r / 2)
            rotate(theta)
            rect(0, 0, self.r, self.r)
