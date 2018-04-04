class Rectangle:
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

def is_colliding(a,b):
    """
    rect colliding has points inside the other point
    let's check this
    """
    def is_inside(d,e,f):
        if d[0]>=e[0] and d[0]<=f[0] and d[1]>=e[1] and d[1]<=f[1]:
            return True
        else:
            return False

    a_topleft = a.corner
    a_topright = (a.corner[0]+a.width, a.corner[1])
    a_bottomleft = (a.corner[0], a.corner[1]+a.height)
    a_bottomright = (a.corner[0]+a.width, a.corner[1]+a.height)

    b_topleft = b.corner
    b_topright = (b.corner[0]+b.width, b.corner[1])
    b_bottomleft = (b.corner[0], b.corner[1]+b.height)
    b_bottomright = (b.corner[0]+b.width, b.corner[1]+b.height)

    # test if b is inside a
    if is_inside(b_topleft, a_topleft, a_bottomright) or \
      is_inside(b_topright, a_topleft, a_bottomright) or \
      is_inside(b_bottomright, a_topleft, a_bottomright) or \
      is_inside(b_bottomleft, a_topleft, a_bottomright):
        return True
    # test if a is inside b
    if is_inside(a_topleft, b_topleft, b_bottomright) or \
       is_inside(a_topright, b_topleft, b_bottomright) or \
       is_inside(a_bottomright, b_topleft, b_bottomright) or \
       is_inside(a_bottomleft, b_topleft, b_bottomright):
        return True


    return False


rec1 = Rectangle((0,0), 10, 10)
rec2 = Rectangle((15,0), 10, 10)

print(is_colliding(rec1, rec2))