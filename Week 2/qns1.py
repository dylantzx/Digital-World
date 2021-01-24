def position_velocity(vo, t):
    g = 9.81
    y = vo*t - 0.5*g*t**2
    yp = vo - g*t
    return round(y, 2), round(yp, 2)
print(position_velocity(5.0, 10.0))
print(position_velocity(5.0, 0.0))
print(position_velocity(0.0, 5.0))
