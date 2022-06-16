'''
1. importar lib
2. setup: config inicial
    a. size

3. draw: desenho no canva
    a. background (cor/limpeza dos steps/frames do desenho)

4. steps do pm
    a. setup - space
        aa. gravity
        ab.
    b. setup - shapes
        ba. append (1 item) ou extend (varios itens) + segment ("paredes")
        bb. space.add shapes
    c. draw - shapes [add_ball/ mouse_pressed/ mouse_dragged]
        ca. body
        cb. body > mass
        cc. body > moi
        cd. body > position
        ce. shape > geometry type (circle)
        cf. shape > friction
        cg. shape > elasticity
        ch. shape append
        ci. space.add body and shape
    d. draw - simular
        da. space.step
'''

import pymunk as pm # importa lib de simulacao

space = pm.Space()
shapes = []

def settings():
    size(800, 800) #area do desenho

def setup(): #config inicial
    space.gravity = (0, 600) #tupla vetor da acel

    #inserir o shape no space e definir o shape/ pm.Segment(corpo estatico, (a.x, a.y), (b.x, b.y), espessura)
    shapes.extend((
        pm.Segment(space.static_body, (0, height / 2), (width / 2 - 25, height * 0.6), 3),
        pm.Segment(space.static_body, (width, height / 2), (width / 2 + 25, height * 0.6), 3),
        )) # funil

    #insere shapes no space
    for shp in shapes:
        space.add(shp)

def add_ball(x, y, r):
    mass = 0.2 * PI * r ** 2
    moi = pm.moment_for_circle(mass, 0, r, (0, 0)) # momento de inercia/ massa, raio interno, raio, centro
    body = pm.Body(mass, moi)
    body.position = (x, y)

    shp = pm.Circle(body, r, (0, 0)) # corpo, raio, coordenadas relativa ao body (offset)
    shp.friction = 0.5
    shp.elasticity = 0.5
    shapes.append(shp)
    space.add(body, shp)

def draw():
    background(222)

    #desenhar os shapes
    for shp in shapes:
        if isinstance(shp, pm.Segment):
            stroke_weight(shp.radius * 2)
            line(shp.a.x, shp.a.y, shp.b.x, shp.b.y)
        elif isinstance(shp, pm.Circle):
            stroke_weight(1)
            x, y = shp.body.position
            circle(x, y, shp.radius * 2)

    # simular
    space.step(0.01)

def mouse_dragged():
    add_ball(mouse_x, mouse_y, 10)