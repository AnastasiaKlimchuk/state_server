should_stop = False
normal_state = {
            'tp': (0, 1000),
            'tc': (0, 1000),
            'T': (0, 1000),
            'b': (0, 1000),
            'h': (0, 1000)
        }


def set_should_stop(stop):
    global should_stop
    should_stop = stop


def get_error(state, norm=normal_state):
    new_state = list()

    for attr, value in state.__dict__.items():
        if attr in norm.keys():
            new_state.append({
                attr: {'value': value,
                       'error': is_in_bounds(value, norm.get(attr))}
            })
        elif attr == 'id' or attr == 'timestamp':
            new_state.append({attr: value})

    return {key: value for d in new_state for key, value in d.items()}


def is_in_bounds(val, limit):
    return -1 if val < limit[0] else 1 if val > limit[1] else 0


