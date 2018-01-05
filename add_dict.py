def add(d1, d2):
    d3 = {}
    d3.update(d1)
    for key, value in d2.iteritems():
        val = d3.get(key, None)

        if val:
            if isinstance(val, dict):
                if isinstance(value, dict):
                    d3[key] = add(val, value)
                else:
                    raise TypeError("unsupported operand type(s) for add: '{}' and '{}'".format(type(val), type(value)))
            else:
                if isinstance(value, dict):
                    raise TypeError("unsupported operand type(s) for add: '{}' and '{}'".format(type(val), type(value)))
                else:
                    d3[key] = val + value
        else:
            d3[key] = value

    return d3
