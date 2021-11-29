from utils import expr
from field_var import field_var


def ask_solution(kb):
    vehicle_solution = [-1 for i in range(4)]
    for position in range(5): # position of the ith vehicle
        for i in range(0,4): # ith vehicle
                result = kb.ask(expr(field_var(i, position)))
                if result:
                    vehicle_solution[i] = position
    return vehicle_solution
