from sage.all import *

u, v = var('u,v')


#face (esphere)
r = 6
face = parametric_plot3d([r*cos(u)*sin(v), r*sin(u)*sin(v), r*cos(v)], (u, 0, 2*pi), (v, 0, pi), color='white')

##face + eyes (more espheres)
r = 1
face += parametric_plot3d([5 + r*cos(u)*sin(v), -2.5 + r*sin(u)*sin(v), 1 + r*cos(v)],  (u, 0, 2*pi), (v, 0, pi), color='black')
face += parametric_plot3d([5 + r*cos(u)*sin(v), +2.5 + r*sin(u)*sin(v), 1 + r*cos(v)],  (u, 0, 2*pi), (v, 0, pi), color='black')

##face + nose (cone)
r = 0.9
h = 6
face += parametric_plot3d([6 + u, ((h-u)/h) * r*sin(v), -0.5 + ((h-u)/h) * r*cos(v) ], (u, 0, h),(v, 0, 2*pi), color='orange')

##face + mouth (parabola)
face += parametric_plot3d([v, u,-3 + .2*pow(u ,2)], (u, -2, 2), (v, 4, 5.3), color='brown');

#hat (cilinder & circumference)
thickness = 6
r = 8
face += parametric_plot3d([thickness*cos(v), thickness*sin(v), 4 + u],  (u, 0, 8), (v, 0, 2*pi), color=Color('black'))
face += parametric_plot3d([v*sin(u), v*cos(u), 4], (u, 0, 2*pi), (v, 0, 8), color=Color('black'))
face += parametric_plot3d([v*sin(u), v*cos(u), 8], (u, 0, 2*pi), (v, 0, 6), color=Color('black'))
face += parametric_plot3d([v*sin(u), v*cos(u), 4.1], (u, 0, 2*pi), (v, 0, 7), color=Color('red'))

#body 
##upper torax (ellipsoid)
a = 9
b = 9
c = 8

x = 0
y = 0
z = -12
body = parametric_plot3d([x + a*cos(u)*sin(v), y + b*sin(u)*sin(v), z + c*cos(v)], (u, 0, 2*pi), (v, 0, pi), color='white')

###buttons (spheres)
r = 1
body += parametric_plot3d([5.5 + r*cos(u)*sin(v), r*sin(u)*sin(v), (z + 6) + r*cos(v)],  (u, 0, 2*pi), (v, 0, pi), color='red')
body += parametric_plot3d([8 + r*cos(u)*sin(v), r*sin(u)*sin(v), (z + 2.8) + r*cos(v)],  (u, 0, 2*pi), (v, 0, pi), color='red')
body += parametric_plot3d([8.5 + r*cos(u)*sin(v), r*sin(u)*sin(v), (z - 1) + r*cos(v)],  (u, 0, 2*pi), (v, 0, pi), color='red')

###Arms (cilinders)
thickness = 0.4
body += parametric_plot3d([-8 + thickness*cos(v), u + 5, -8 + thickness*sin(v)],  (u, 0, 12), (v, 0, 2*pi), color=Color('#5D3521')).rotate((0,1,1), pi/4)
body += parametric_plot3d([-1 + thickness*cos(v), u - 7, -10 + thickness*sin(v)],  (u, -12, 0), (v, 0, 2*pi), color=Color('#5D3521'))

##lower torax (ellipsoid)
a = 12
b = 12
c = 11

x = 0
y = 0
z = -25
body += parametric_plot3d([x + a*cos(u)*sin(v), y + b*sin(u)*sin(v), z + c*cos(v)], (u, 0, 2*pi), (v, 0, pi), color='white')

##grass (circumference)
body += parametric_plot3d([v*sin(u), v*cos(u), z - 11], (u, 0, 2*pi), (v, 0, 20), color=Color('green'))

#generate final graph
rabit = body + face
rabit.save('snow-man.png')
rabit.show(aspect_ratio=[1,1,1])


