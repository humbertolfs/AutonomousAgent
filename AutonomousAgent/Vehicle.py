class Vehicle():
    def __init__(self, x, y):
        self.localAtual = PVector(x, y)
        self.velocidade = PVector(0, 0)
        self.aceleracao = PVector(0, 0)
        
        self.r = 5
        self.velMaxima = 6
        self.forcaMaxima = 0.2
        self.pontos = 0
        
    def update(self):
        self.velocidade.add(self.aceleracao)
        self.velocidade.limit(self.velMaxima)
        self.localAtual.add(self.velocidade)
        self.aceleracao.mult(0)
    
    def aplicarForca(self, forca):
        self.aceleracao.add(forca)
        
    def buscaSuave(self, alvo):
        velDesejada = alvo - self.localAtual
        d = velDesejada.mag()
        
        if(d < 100):
            m = map(d, 0, 100, 0, self.velMaxima)
            velDesejada.setMag(m)
        else:
            velDesejada.setMag(self.velMaxima)
        
        direcao = velDesejada - self.velocidade
        direcao.limit(self.forcaMaxima)
        
        self.aplicarForca(direcao)
        
    def pontuou(self):
        self.pontos += 1
        
    def display(self):
        theta = self.velocidade.heading() + PI / 2
        fill(255, 0, 0)
        stroke(255, 0, 0)
        strokeWeight(1)
        with pushMatrix():
            translate(self.localAtual.x, self.localAtual.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
        
