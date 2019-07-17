class PolyMap:
    def __init__(self):
        self._map = {}

    def __setitem__(self, key, value):
        self._map[key] = value

    def __getitem__(self, item):

        # FIXME: have to repopulate map every time, super ineffcient
        populate_map()

        for keys in self._map:
            if item == keys:
                return self._map[item]
            if item in keys:
                # print("item" + str(item))
                # val = self._map[keys]
                # # self._map[item] = val
                # self.__setitem__(keys, val)

                # print("val" + str(val))

                return self._map[keys]
        return None

NOTEMAP = PolyMap()


def populate_map():
    NOTEMAP[(12*n for n in range(0, 10))]   = 'C'
    NOTEMAP[(1+12*n for n in range(0, 10))] = 'C#'
    NOTEMAP[(2+12*n for n in range(0, 10))] = 'D'
    NOTEMAP[(3+12*n for n in range(0, 10))] = 'D#'
    NOTEMAP[(4+12*n for n in range(0, 10))] = 'E'
    NOTEMAP[(5+12*n for n in range(0, 10))] = 'F'
    NOTEMAP[(6+12*n for n in range(0, 10))] = 'F#'
    NOTEMAP[(7+12*n for n in range(0, 10))] = 'G'
    NOTEMAP[(8+12*n for n in range(0, 9))]  = 'G#'
    NOTEMAP[(9+12*n for n in range(0, 9))]  = 'A'
    NOTEMAP[(10+12*n for n in range(0, 9))] = 'A#'
    NOTEMAP[(11+12*n for n in range(0, 9))] = 'B'



B_MINOR_MAP = {
    'B':  1,
    'C#': 2,
    'D':  3,
    'E':  4,
    'F#': 5,
    'G':  6,
    'A':  7
}

B_MINOR_INTERVALS = {
    1: 0,
    2: 2,
    3: 3,
    4: 5,
    5: 7,
    6: 8,
    7: 10
}

def B_MINOR(note):
    # populate_map()
    # print("MAP {} {}".format(NOTEMAP[note], note))
    # print("MAP {} {}".format(NOTEMAP[note+12], note+12))

    return B_MINOR_MAP[NOTEMAP[note]]

def second(root):
    degree = B_MINOR_MAP[NOTEMAP[root]]
    if degree == 2 or degree == 5:
        # Half Step
        return root + 1
    else:
        # Whole Step
        return root + 2

def third(root):
    degree = B_MINOR_MAP[NOTEMAP[root]]
    if degree == 3 or degree == 6 or degree == 7:
        # Major 3rd
        return root + 4
    else:
        # Minor 3rd
        return root + 3

def fourth(root):
    degree = B_MINOR_MAP[NOTEMAP[root]]
    if degree == 6:
        # Augmented 4th
        return root + 6
    else:
        # Perfect 4th
        return root + 5

def fifth(root):
    degree = B_MINOR_MAP[NOTEMAP[root]]
    if degree == 2:
        # Diminished 5th
        return root + 4
    else: 
        # Perfect 5th
        return root + 7

def sixth(root):
    degree = B_MINOR_MAP[NOTEMAP[root]]
    if degree == 3 or degree == 4 or degree == 6 or degree == 7:
        # Major 6th
        return root + 9
    else:
        # Minor 6th
        return root + 8

def seventh(root):
    degree = B_MINOR_MAP[NOTEMAP[root]]
    if degree == 3 or degree == 6:
        # Major 7th
        return root + 11
    else:
        # Minor 7th
        return root + 10

def octave(root):
    return root + 12

INTERVALS = {
    'second': second,
    'third': third,
    'fourth': fourth,
    'fifth': fifth,
    'sixth': sixth,
    'seventh': seventh,
    'octave': octave
}




populate_map()

# print(B_MINOR(66))
# print(B_MINOR(59))
# print(third(1))

# print(B_MINOR(59))

# print(NOTEMAP[second((59))])
# print(NOTEMAP[second((61))])
# print(NOTEMAP[second((62))])
# print(NOTEMAP[second((64))])
# print(NOTEMAP[second((66))])
# print(NOTEMAP[second((67))])
# print(NOTEMAP[second(69)])

# print(NOTEMAP[59])
# print(NOTEMAP[third(59)])
# print(NOTEMAP[fifth(59)])
