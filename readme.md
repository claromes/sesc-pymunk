# Desenvolvimento de Simulações Físicas 2D - SESC Av. Paulista

AULA 01
---

Pymunk: lib para criar simulações físicas em python
http://www.pymunk.org

Py5: processing para python (alternativa ao Processing.py)
https://py5.ixora.io

Thonny: IDE para iniciantes (ambiente prontinho!)
https://thonny.org
* ative o "Imported mode for py5"

Materias extras: https://github.com/villares/material-aulas

Colinha Py5: https://github.com/villares/processing.py-cheat-sheet/blob/pt-br/py5/py5_cc.pdf

Outras refs:
- Pygame
- Pyxel


AULA 02
---

Revisão de como iniciar uma simulação com Pymunk

- arquivo de aula: ex_aula02.py

- snippet: pm_snippet_thonny.py

```
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
```

AULA 03
---

Criação de shapes compostos (shapes no mesmo body)

Exemplos vistos:
- Tetris (Poly e points)
- Pêndulo (Constraints, PinJoint, DampedSpring)


AULA 04
---

Criação de soft-body

Ref: https://github.com/villares/sketch-a-day/blob/main/2022/sketch_2022_04_07pymunk/sketch_2022_04_07pymunk.py


AULA 05 e 06
---

Projeto final - Pinball

https://github.com/villares/pymunk-pinball-paulista


EXTRAS
---

- LERP (linear interpolation)
```
lerp(start, end, t)
```

- Debug com click

Para descobrir uma posição no sketch
```
def mouse_clicked():
  print(mouse_x, mouse_y)
```

- Keyword arguments
```
**kwargs
```