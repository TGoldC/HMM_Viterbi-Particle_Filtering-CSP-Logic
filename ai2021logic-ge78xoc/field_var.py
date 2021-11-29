
def field_var(vehicle_nr,position):
    # The variable V_nx is defined by the vehicle number and the turn at which it drives through the intersection
    assert type(vehicle_nr) == int and type(position) == int
    return "V%i%i" % (vehicle_nr, position)
