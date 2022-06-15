'''
Pymunk + Py5 snippet for Thonny (Imported mode for py5 on)

1. import lib

2. draw area
    a. size
    b. background
    
3. pm config
    a. setup
        aa. space
        ab. gravity
        ac. segment shapes
        ad. append or extend segment shape(s) 
        ae. add segment shape(s) into space
        
    b. draw
        ba. body > mass
        bb. body > moi
        bc. body
        bd. body > position
        be. shape > geometry type
        bf. shape > friction
        bg. shape > elasticity
        bh. shape append
        bi. add body + shape into space
        
    c. simulation
        ca. space.step
'''

import pymunk as pm

space = pm.Space()
shapes = []

def settings():
    size(1000, 1000)

def setup():
    space.gravity = (0, 600)
    
    seg = #pm.Segment(space.static_body, (100, 400), (400, 400), 3)
    seg.elasticity = 0.8
    
    shapes.append(seg)
    space.add(seg)
    
def draw():
    background(000)
    
    mass = 5
    moi = #pm.moment_for_circle(mass, 0, 5)
    
    body = pm.Body(mass, moi)
    body.position = #(random(100, 400), 200)
    
    shp = #pm.Circle(body, 10, (0, 0)) 
    shp.friction = 0.8 #Material: steel
    shp.elasticity = 1
    
    shapes.append(shp)
    space.add(body, shp)
    
    for shp in shapes:
        if isinstance(shp, pm.Segment):
            #line(100, 400, 400, 400)
        elif isinstance(shp, pm.Circle):
            no_stroke()
            x, y = shp.body.position
            #circle(x, y, 8)
    
    space.step(0.01)