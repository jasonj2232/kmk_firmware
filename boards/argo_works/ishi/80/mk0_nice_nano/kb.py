import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.nice_nano import pinout as pins
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        board.pins[14],
        board.pins[15],
        board.pins[12],
        board.pins[13],
        board.pins[4],
        board.pins[5],
        board.pins[11],
        board.pins[10],
        board.pins[9]
    )
    col_pins = (
        board.pins[0],
        board.pins[19],
        board.pins[18],
        board.pins[17],
        board.pins[16],
        board.pins[8],
        board.pins[7],
        board.pins[6],
        board.pins[1]
    )
    diode_orientation = DiodeOrientation.COL2ROW
    coord_mapping = [
         9,  0, 10,  1,    11,  2, 12,  3, 13,  4, 14,  5, 15,  6, 16,  7, 17,  8,
        27, 18, 28, 19,    29, 20, 30, 21, 31, 22, 32, 23, 33, 24, 34, 25, 35, 26,
            36, 46, 37,    47, 38, 48, 39, 49, 40, 50, 41, 51, 42, 52, 43,     44,
        63, 54, 64, 55,    65, 66, 57, 67, 58, 68, 59, 69, 60, 70, 61,         62,
            72, 73,        74, 56, 75,             76,             77, 78, 79, 71,   80 
    ]