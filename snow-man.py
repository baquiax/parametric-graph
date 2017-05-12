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

#body (Ellipsoid)
##upper torax
a = 9
b = 9
c = 8

x = 0
y = 0
z = -12

body = parametric_plot3d([x + a*cos(u)*sin(v), y + b*sin(u)*sin(v), z + c*cos(v)], (u, 0, 2*pi), (v, 0, pi), color='white')

##lower torax
a = 12
b = 12
c = 11

x = 0
y = 0
z = -25

body += parametric_plot3d([x + a*cos(u)*sin(v), y + b*sin(u)*sin(v), z + c*cos(v)], (u, 0, 2*pi), (v, 0, pi), color='white')



rabit = body + face
rabit.show(aspect_ratio=[1,1,1])


