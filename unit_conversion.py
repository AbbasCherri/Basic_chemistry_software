def volume_convert(num, unit):
    conversions = {
        'ml': num * 0.001,
        'cl': num * 0.01,
        'dl': num * 0.1,
        'dal': num * 10,
        'hl': num * 100,
        'kl': num * 1000,
        'Ml': num * 1000000, 
        'Gl': num * 1000000000
    }
    return conversions.get(unit, 'Invalid unit. Please use a valid volume unit.')

def weight_convert(num, unit):
    conversions = {
        'mg': num * 0.001,
        'cg': num * 0.01,
        'dg': num * 0.1,
        'dag': num * 10,
        'hg': num * 100,
        'kg': num * 1000,
        'Mg': num * 1000000, 
        'Gg': num * 1000000000
    }
    return conversions.get(unit, 'Invalid unit. Please use a valid weight unit.')

def dist_convert(num, unit):
    conversions = {
        'mm': num * 0.001,
        'cm': num * 0.01,
        'dm': num * 0.1,
        'dam': num * 10,
        'hm': num * 100,
        'km': num * 1000,
        'Mm': num * 1000000,  
        'Gm': num * 1000000000
    }
    return conversions.get(unit, 'Invalid unit. Please use a valid distance unit.')