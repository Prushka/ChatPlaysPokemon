STATE_OUT_OF_SYNC = 0
STATE_SYNC_START = 1
STATE_SYNC_1 = 2
STATE_SYNC_2 = 3
STATE_SYNC_OK = 4

# Commands to send to MCU
COMMAND_NOP = 0x00
COMMAND_SYNC_1 = 0x33
COMMAND_SYNC_2 = 0xCC
COMMAND_SYNC_START = 0xFF

# Responses from MCU
RESP_USB_ACK = 0x90
RESP_UPDATE_ACK = 0x91
RESP_UPDATE_NACK = 0x92
RESP_SYNC_START = 0xFF
RESP_SYNC_1 = 0xCC
RESP_SYNC_OK = 0x33

# Actual Switch DPAD Values
A_DPAD_CENTER = 0x08
A_DPAD_U = 0x00
A_DPAD_U_R = 0x01
A_DPAD_R = 0x02
A_DPAD_D_R = 0x03
A_DPAD_D = 0x04
A_DPAD_D_L = 0x05
A_DPAD_L = 0x06
A_DPAD_U_L = 0x07

# Enum DIR Values
DIR_CENTER = 0x00
DIR_U = 0x01
DIR_R = 0x02
DIR_D = 0x04
DIR_L = 0x08
DIR_U_R = DIR_U + DIR_R
DIR_D_R = DIR_D + DIR_R
DIR_U_L = DIR_U + DIR_L
DIR_D_L = DIR_D + DIR_L

DPAD_CENTER = 0x0000000000000000
DPAD_U = 0x0000000000010000
DPAD_R = 0x0000000000020000
DPAD_D = 0x0000000000040000
DPAD_L = 0x0000000000080000
DPAD_U_R = DPAD_U + DPAD_R
DPAD_D_R = DPAD_D + DPAD_R
DPAD_U_L = DPAD_U + DPAD_L
DPAD_D_L = DPAD_D + DPAD_L

BTN_NONE = 0x0000000000000000
BTN_Y = 0x0000000000000001
BTN_B = 0x0000000000000002
BTN_A = 0x0000000000000004
BTN_X = 0x0000000000000008
BTN_L = 0x0000000000000010
BTN_R = 0x0000000000000020
BTN_ZL = 0x0000000000000040
BTN_ZR = 0x0000000000000080
BTN_MINUS = 0x0000000000000100
BTN_PLUS = 0x0000000000000200
BTN_LCLICK = 0x0000000000000400
BTN_RCLICK = 0x0000000000000800
BTN_HOME = 0x0000000000001000
BTN_CAPTURE = 0x0000000000002000

LSTICK_CENTER = 0x0000000000000000
LSTICK_R = 0x00000000FF000000  # 0 (000)
LSTICK_U_R = 0x0000002DFF000000  # 45 (02D)
LSTICK_U = 0x0000005AFF000000  # 90 (05A)
LSTICK_U_L = 0x00000087FF000000  # 135 (087)
LSTICK_L = 0x000000B4FF000000  # 180 (0B4)
LSTICK_D_L = 0x000000E1FF000000  # 225 (0E1)
LSTICK_D = 0x0000010EFF000000  # 270 (10E)
LSTICK_D_R = 0x0000013BFF000000  # 315 (13B)

RSTICK_CENTER = 0x0000000000000000
RSTICK_R = 0x000FF00000000000  # 0 (000)
RSTICK_U_R = 0x02DFF00000000000  # 45 (02D)
RSTICK_U = 0x05AFF00000000000  # 90 (05A)
RSTICK_U_L = 0x087FF00000000000  # 135 (087)
RSTICK_L = 0x0B4FF00000000000  # 180 (0B4)
RSTICK_D_L = 0x0E1FF00000000000  # 225 (0E1)
RSTICK_D = 0x10EFF00000000000  # 270 (10E)
RSTICK_D_R = 0x13BFF00000000000  # 315 (13B)

NO_INPUT = BTN_NONE + DPAD_CENTER + LSTICK_CENTER + RSTICK_CENTER

ACTIVEEVENT = 1

ANYFORMAT = 268435456

ASYNCBLIT = 4

AUDIODEVICEADDED = -1
AUDIODEVICEREMOVED = -1

AUDIO_ALLOW_ANY_CHANGE = -1

AUDIO_ALLOW_CHANNELS_CHANGE = -1

AUDIO_ALLOW_FORMAT_CHANGE = -1

AUDIO_ALLOW_FREQUENCY_CHANGE = -1

AUDIO_S16 = 32784
AUDIO_S16LSB = 32784
AUDIO_S16MSB = 36880
AUDIO_S16SYS = 32784
AUDIO_S8 = 32776
AUDIO_U16 = 16
AUDIO_U16LSB = 16
AUDIO_U16MSB = 4112
AUDIO_U16SYS = 16
AUDIO_U8 = 8

BIG_ENDIAN = 4321

BLEND_ADD = 1
BLEND_MAX = 5
BLEND_MIN = 4
BLEND_MULT = 3
BLEND_PREMULTIPLIED = 17

BLEND_RGBA_ADD = 6
BLEND_RGBA_MAX = 16
BLEND_RGBA_MIN = 9
BLEND_RGBA_MULT = 8
BLEND_RGBA_SUB = 7

BLEND_RGB_ADD = 1
BLEND_RGB_MAX = 5
BLEND_RGB_MIN = 4
BLEND_RGB_MULT = 3
BLEND_RGB_SUB = 2

BLEND_SUB = 2

BUTTON_LEFT = 1
BUTTON_MIDDLE = 2
BUTTON_RIGHT = 3
BUTTON_WHEELDOWN = 5
BUTTON_WHEELUP = 4
BUTTON_X1 = 6
BUTTON_X2 = 7

DOUBLEBUF = 1073741824

DROPBEGIN = -1
DROPCOMPLETE = -1
DROPFILE = -1
DROPTEXT = -1

FINGERDOWN = -1
FINGERMOTION = -1
FINGERUP = -1

FULLSCREEN = -2147483648

GL_ACCELERATED_VISUAL = 15

GL_ACCUM_ALPHA_SIZE = 11

GL_ACCUM_BLUE_SIZE = 10

GL_ACCUM_GREEN_SIZE = 9

GL_ACCUM_RED_SIZE = 8

GL_ALPHA_SIZE = 3

GL_BLUE_SIZE = 2

GL_BUFFER_SIZE = 4

GL_DEPTH_SIZE = 6

GL_DOUBLEBUFFER = 5

GL_GREEN_SIZE = 1

GL_MULTISAMPLEBUFFERS = 13
GL_MULTISAMPLESAMPLES = 14

GL_RED_SIZE = 0

GL_STENCIL_SIZE = 7

GL_STEREO = 12

GL_SWAP_CONTROL = 16

HAT_CENTERED = 0
HAT_DOWN = 4
HAT_LEFT = 8
HAT_LEFTDOWN = 12
HAT_LEFTUP = 9
HAT_RIGHT = 2
HAT_RIGHTDOWN = 6
HAT_RIGHTUP = 3
HAT_UP = 1

HWACCEL = 256
HWPALETTE = 536870912
HWSURFACE = 1

IYUV_OVERLAY = 1448433993

JOYAXISMOTION = 7
JOYBALLMOTION = 8
JOYBUTTONDOWN = 10
JOYBUTTONUP = 11
JOYHATMOTION = 9

KEYDOWN = 2
KEYUP = 3

KMOD_ALT = 768
KMOD_CAPS = 8192
KMOD_CTRL = 192
KMOD_LALT = 256
KMOD_LCTRL = 64
KMOD_LMETA = 1024
KMOD_LSHIFT = 1
KMOD_META = 3072
KMOD_MODE = 16384
KMOD_NONE = 0
KMOD_NUM = 4096
KMOD_RALT = 512
KMOD_RCTRL = 128
KMOD_RMETA = 2048
KMOD_RSHIFT = 2
KMOD_SHIFT = 3

K_0 = 48
K_1 = 49
K_2 = 50
K_3 = 51
K_4 = 52
K_5 = 53
K_6 = 54
K_7 = 55
K_8 = 56
K_9 = 57
K_a = 97
K_AMPERSAND = 38
K_ASTERISK = 42
K_AT = 64
K_b = 98
K_BACKQUOTE = 96
K_BACKSLASH = 92
K_BACKSPACE = 8
K_BREAK = 318
K_c = 99
K_CAPSLOCK = 301
K_CARET = 94
K_CLEAR = 12
K_COLON = 58
K_COMMA = 44
K_d = 100
K_DELETE = 127
K_DOLLAR = 36
K_DOWN = 274
K_e = 101
K_END = 279
K_EQUALS = 61
K_ESCAPE = 27
K_EURO = 321
K_EXCLAIM = 33
K_f = 102
K_F1 = 282
K_F10 = 291
K_F11 = 292
K_F12 = 293
K_F13 = 294
K_F14 = 295
K_F15 = 296
K_F2 = 283
K_F3 = 284
K_F4 = 285
K_F5 = 286
K_F6 = 287
K_F7 = 288
K_F8 = 289
K_F9 = 290
K_FIRST = 0
K_g = 103
K_GREATER = 62
K_h = 104
K_HASH = 35
K_HELP = 315
K_HOME = 278
K_i = 105
K_INSERT = 277
K_j = 106
K_k = 107
K_KP0 = 256
K_KP1 = 257
K_KP2 = 258
K_KP3 = 259
K_KP4 = 260
K_KP5 = 261
K_KP6 = 262
K_KP7 = 263
K_KP8 = 264
K_KP9 = 265

K_KP_DIVIDE = 267
K_KP_ENTER = 271
K_KP_EQUALS = 272
K_KP_MINUS = 269
K_KP_MULTIPLY = 268
K_KP_PERIOD = 266
K_KP_PLUS = 270

K_l = 108
K_LALT = 308
K_LAST = 323
K_LCTRL = 306
K_LEFT = 276
K_LEFTBRACKET = 91
K_LEFTPAREN = 40
K_LESS = 60
K_LMETA = 310
K_LSHIFT = 304
K_LSUPER = 311
K_m = 109
K_MENU = 319
K_MINUS = 45
K_MODE = 313
K_n = 110
K_NUMLOCK = 300
K_o = 111
K_p = 112
K_PAGEDOWN = 281
K_PAGEUP = 280
K_PAUSE = 19
K_PERIOD = 46
K_PLUS = 43
K_POWER = 320
K_PRINT = 316
K_q = 113
K_QUESTION = 63
K_QUOTE = 39
K_QUOTEDBL = 34
K_r = 114
K_RALT = 307
K_RCTRL = 305
K_RETURN = 13
K_RIGHT = 275
K_RIGHTBRACKET = 93
K_RIGHTPAREN = 41
K_RMETA = 309
K_RSHIFT = 303
K_RSUPER = 312
K_s = 115
K_SCROLLOCK = 302
K_SEMICOLON = 59
K_SLASH = 47
K_SPACE = 32
K_SYSREQ = 317
K_t = 116
K_TAB = 9
K_u = 117
K_UNDERSCORE = 95
K_UNKNOWN = 0
K_UP = 273
K_v = 118
K_w = 119
K_x = 120
K_y = 121
K_z = 122

LIL_ENDIAN = 1234

MOUSEBUTTONDOWN = 5
MOUSEBUTTONUP = 6
MOUSEMOTION = 4
MOUSEWHEEL = -1

MULTIGESTURE = -1

NOEVENT = 0
NOFRAME = 32

NUMEVENTS = 32

OPENGL = 2
OPENGLBLIT = 10

PREALLOC = 16777216

QUIT = 12

RESIZABLE = 16

MOUSE_LEFT = 1
MOUSE_MIDDLE = 2
MOUSE_RIGHT = 3
MOUSE_DEEP = 7
MOUSE_SHALLOW = 6

# Gamepad to Joycon
# No customization

JOYCON_DICT = {"A": BTN_A,
               "B": BTN_B,
               "X": BTN_X,
               "Y": BTN_Y,

               "🏘": BTN_HOME,
               "📷": BTN_CAPTURE,

               # "HOME": BTN_HOME,
               # "CAPTURE": BTN_CAPTURE,

               "L": BTN_L,
               "R": BTN_R,
               "LB": BTN_L,
               "RB": BTN_R,
               "ZR": BTN_ZR,
               "ZL": BTN_ZL,
               "RT": BTN_ZR,
               "LT": BTN_ZL,

               "+": BTN_MINUS,
               "-": BTN_PLUS,

               "SELECT": BTN_MINUS,
               "START": BTN_PLUS,

               "LCLICK": BTN_LCLICK,
               "RCLICK": BTN_RCLICK,

               "DPAD_U": DPAD_U,
               "DPAD_L": DPAD_L,
               "DPAD_D": DPAD_D,
               "DPAD_R": DPAD_R,

               "十字键-上": DPAD_U,
               "十字键-左": DPAD_L,
               "十字键-下": DPAD_D,
               "十字键-右": DPAD_R,

               "DPAD_U_R": DPAD_U_R,
               "DPAD_U_L": DPAD_U_L,
               "DPAD_D_R": DPAD_D_R,
               "DPAD_D_L": DPAD_D_L,

               "RSTICK_CENTER": RSTICK_CENTER,
               "RSTICK_U": RSTICK_U,
               "RSTICK_L": RSTICK_L,
               "RSTICK_D": RSTICK_D,
               "RSTICK_R": RSTICK_R,
               "RSTICK_U_R": RSTICK_U_R,
               "RSTICK_U_L": RSTICK_U_L,
               "RSTICK_D_R": RSTICK_D_R,
               "RSTICK_D_L": RSTICK_D_L,
               "R_STICK": RSTICK_U,

               "LSTICK_CENTER": LSTICK_CENTER,
               "LSTICK_U": LSTICK_U,
               "LSTICK_L": LSTICK_L,
               "LSTICK_D": LSTICK_D,
               "LSTICK_R": LSTICK_R,
               "LSTICK_U_R": LSTICK_U_R,
               "LSTICK_U_L": LSTICK_U_L,
               "LSTICK_D_R": LSTICK_D_R,
               "LSTICK_D_L": LSTICK_D_L,
               "L_STICK": LSTICK_U,
               }
