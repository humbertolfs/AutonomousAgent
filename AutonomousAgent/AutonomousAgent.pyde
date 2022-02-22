from Vehicle import Vehicle
from Food import Food



def setup():
    global car
    global food
    global circleCenterX
    global circleCenterY
    global circleRadius
    
    size(640, 360)
    
    car = Vehicle(width / 2, height / 2)
    
    foodPosition = PVector(int(random(0, width)), int(random(0, height)))
    food = Food(foodPosition.x, foodPosition.y)
    
    circleCenterX = foodPosition.x
    circleCenterY = foodPosition.y
    circleRadius = 10
    
def draw():
    global food
    global circleCenterX
    global circleCenterY
    global circleRadius
    background(127)
    
    fill(127)
    stroke(200)
    strokeWeight(2)
    
    if(dist(car.localAtual.x, car.localAtual.y, circleCenterX, circleCenterY) < circleRadius):
        car.pontuou()
        foodPosition = PVector(int(random(0, width)), int(random(0, height)))
        food = Food(foodPosition.x, foodPosition.y)
        circleCenterX = foodPosition.x
        circleCenterY = foodPosition.y
        circleRadius = 10

    car.buscaSuave(food.localAtual)
    car.update()
    car.display()
    food.update()
    food.display()

    
