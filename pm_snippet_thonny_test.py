import pymunk as pm

space = pm.Space()
shapes = []

def settings():
    size(500, 500)

def setup():
    space.gravity = (0, 600)
    
    seg = pm.Segment(space.static_body, (100, 400), (400, 400), 3)
    seg.elasticity = 0.8    
    
    shapes.append(seg)
    space.add(seg)
    
def draw():
    background(222)
    
    mass = 5
    moi = pm.moment_for_circle(mass, 0, 5)
    
    body = pm.Body(mass, moi)
    body.position = (random(100, 400), 200)
    
    shp = pm.Circle(body, 5, (0, 0)) 
    shp.friction = 0.8
    shp.elasticity = 1
    
    shapes.append(shp)
    space.add(body, shp)
    
    for shp in shapes:
        if isinstance(shp, pm.Segment):
            line(100, 400, 400, 400)
        elif isinstance(shp, pm.Circle):
            x, y = shp.body.position
            circle(x, y, 8)
    
    space.step(0.01)