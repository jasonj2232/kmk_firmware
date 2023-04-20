from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.frood import pinout as pins
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        pins[19],
        pins[20],
        pins[17],
        pins[18],
        pins[16],
        pins[15],
        pins[11],
        pins[10],
        pins[9]
    )
    col_pins = (
        pins[0],
        pins[24],
        pins[23],
        pins[22],
        pins[21],
        pins[8],
        pins[7],
        pins[6],
        pins[1]
    )
    diode_orientation = DiodeOrientation.COL2ROW
    coord_mapping = [
         9,  0, 10,  1,    11,  2, 12,  3, 13,  4, 14,  5, 15,  6, 16,  7, 17,  8,
        27, 18, 28, 19,    29, 20, 30, 21, 31, 22, 32, 23, 33, 24, 34, 25, 35, 26,
            36, 46, 37,    47, 38, 48, 39, 49, 40, 50, 41, 51, 42, 52, 43,     44,
        63, 54, 64, 55,    65, 66, 57, 67, 58, 68, 59, 69, 60, 70, 61,         62,
            72, 73,        74, 56, 75,             76,             77, 78, 79, 71,   80 
    ]