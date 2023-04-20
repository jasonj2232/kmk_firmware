from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

media = MediaKeys()
layers_ext = Layers()

keyboard.modules = [layers_ext]
keyboard.extensions = [media]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    [
        KC.PMNS, KC.PAST, KC.PSLS, KC.NLCK,    KC.ESC,       KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.PPLS, KC.P9,   KC.P8,   KC.P7,      KC.TAB,       KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
                 KC.P6,   KC.P5,   KC.P4,      KC.CAPSLOCK,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,          KC.ENT,
        KC.PENT, KC.P3,   KC.P2,   KC.P1,      KC.LSFT,      KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,          KC.RSFT,
                 KC.PDOT, KC.P0,               KC.LCTL,      KC.LGUI, KC.LT(1, KC.LALT),                  KC.SPC,                             KC.RALT, KC.RGUI, KC.APP,  KC.RCTL,    KC.MUTE
    ],
    [
        _______, _______, _______, _______,    KC.GRAVE,     KC.F1,   KC.F2,  KC.F3,   KC.F4,   KC.F5,   KC.F6,    KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11, KC.F12,  KC.DEL,
        _______, _______, _______, _______,    _______,      _______, _______,_______, _______, _______, _______,  _______, _______, _______, _______, _______,_______, _______,
                 KC.PSCR, KC.SLCK, KC.PAUS,    _______,      _______, _______,_______, _______, _______, _______,  _______, _______, _______, _______, _______,         _______,
        _______, _______, _______, _______,    _______,      _______, _______,_______, _______, _______, _______,  _______, _______, _______, _______,         KC.UP,
                 _______, _______,             _______,      _______, _______,                           _______,                             _______, KC.LEFT,KC.DOWN, KC.RGHT,    KC.MPLY
    ]
]

if __name__ == '__main__':
    keyboard.go()