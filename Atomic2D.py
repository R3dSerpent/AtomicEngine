import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pyg
from dataclasses import dataclass


class StartAtomic():
    def __init__(self, HIDE_INIT_PROMPT=False):
        pyg.init()

        # Credits and stuff
        self.credits = 'Built on top of pygame and PyOpenGl'
        self.version = '0.0.v1'
        self.updates = 'More Color effects & Keys are coming soon'
        self.init_prompt = f"Atomic Version {self.version}\nThank you for choosing Atomic! \n CREDS: {self.credits} \n Updates Coming: {self.updates}" if not HIDE_INIT_PROMPT else ''
        print(self.init_prompt)


        # COLORS
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BROWN = (139,131,120)
        self.AQUA = (0,255,255)
        self.AQUAMARINE = (69,139,116)
        self.GRAY = (131,139,139)
        self.YELLOW = (227,207,87)
        self.BEIGE = (245,245,220)
        self.DARKBLUE = (0,0,139)
        self.ORANGE = (255,153,18)
        self.PURPLE = (191,62,255)
        self.DEEPPINK = (255,20,147)
        self.SKYBLUE = (0,191,255)
        self.EMERALDGREEN = (0,201,87)
        self.SUPERDARKGRAY = (26,26,26)
        self.DARKGRAY = (33,33,33)
        self.LOWERGRAY = (48,48,48)
        self.PINK = (255,52,179)
        self.DARKPINK = (139,28,98)

        #TODO: pyg = pygame ##

        # KEYS

        self.K_ACBACK = pyg.K_AC_BACK
        self.K_AMPERSAND = pyg.K_AMPERSAND
        self.K_ASTERISK = pyg.K_ASTERISK
        self.K_AT = pyg.K_AT
        self.K_TAB = pyg.K_TAB
        self.K_SPACE = pyg.K_SPACE
        self.K_BSPACE = pyg.K_BACKSPACE
        self.K_BSLASH = pyg.K_BACKSLASH
        self.K_BQUOTE = pyg.K_BACKQUOTE
        self.K_BREAK = pyg.K_BREAK
        self.K_CAPS = pyg.K_CAPSLOCK
        self.K_QUOTE = pyg.K_QUOTE
        self.K_CARET = pyg.K_CARET
        self.K_CLEAR = pyg.K_CLEAR
        self.K_COLON = pyg.K_COLON
        self.K_COMMA = pyg.K_COMMA
        self.K_CUR_SUB_UNIT = pyg.K_CURRENCYSUBUNIT
        self.K_CUR_UNIT = pyg.K_CURRENCYUNIT
        self.K_DEL = pyg.K_DELETE
        self.K_DOLLAR = pyg.K_DOLLAR
        self.K_EQUALS = pyg.K_EQUALS
        self.K_END = pyg.K_END
        self.K_ESC = pyg.K_ESCAPE
        self.K_EURO = pyg.K_EURO
        self.K_EXCLAIM_MARK = pyg.K_EXCLAIM

        self.K_ZERO   = pyg.K_0
        self.K_ONE    = pyg.K_1
        self.K_TWO    = pyg.K_2
        self.K_THREE  = pyg.K_3
        self.K_FOUR   = pyg.K_4
        self.K_FIVE   = pyg.K_5
        self.K_SIX    = pyg.K_6
        self.K_SEVEN  = pyg.K_7
        self.K_EIGHT  = pyg.K_8
        self.K_NINE   = pyg.K_9




        self.K_A = pyg.K_a
        self.K_B = pyg.K_b
        self.K_C = pyg.K_c
        self.K_D = pyg.K_d
        self.K_E = pyg.K_e
        self.K_F = pyg.K_f
        self.K_G = pyg.K_g
        self.K_H = pyg.K_h
        self.K_I = pyg.K_i
        self.K_J = pyg.K_j
        self.K_K = pyg.K_k
        self.K_L = pyg.K_l
        self.K_M = pyg.K_m
        self.K_N = pyg.K_n
        self.K_O = pyg.K_o
        self.K_P = pyg.K_p
        self.K_Q = pyg.K_q
        self.K_R = pyg.K_r
        self.K_S = pyg.K_s
        self.K_T = pyg.K_t
        self.K_U = pyg.K_u
        self.K_V = pyg.K_v
        self.K_W = pyg.K_w
        self.K_X = pyg.K_x
        self.K_Y = pyg.K_y
        self.K_Z = pyg.K_z

        self.K_F1 = pyg.K_F1
        self.K_F2 = pyg.K_F2
        self.K_F3 = pyg.K_F3
        self.K_F4 = pyg.K_F4
        self.K_F5 = pyg.K_F5
        self.K_F6 = pyg.K_F6
        self.K_F7 = pyg.K_F7
        self.K_F8 = pyg.K_F8
        self.K_F9 = pyg.K_F9
        self.K_F10 = pyg.K_F10
        self.K_F11 = pyg.K_F11
        self.K_F12 = pyg.K_F12
        self.K_F13 = pyg.K_F13
        self.K_F14 = pyg.K_F14
        self.K_F15 = pyg.K_F15

        self.K_UP_ARROW = pyg.K_UP
        self.K_DOWN_ARROW = pyg.K_DOWN
        self.K_LEFT_ARROW = pyg.K_LEFT
        self.K_RIGHT_ARROW = pyg.K_RIGHT


        self.K_RBRACKET = pyg.K_RIGHTBRACKET
        self.K_LBRACKET = pyg.K_LEFTBRACKET
        self.K_LPARA = pyg.K_LEFTPAREN
        self.K_RPARA = pyg.K_RIGHTPAREN
        self.K_LEFTSHIFT = pyg.K_LSHIFT
        self.K_RIGHTSHIFT = pyg.K_RSHIFT
        self.K_LEFTALT = pyg.K_LALT
        self.K_RIGHTALT = pyg.K_RALT

        self.K_GREATER = pyg.K_GREATER
        self.K_LESS = pyg.K_LESS

        self.K_PERC = pyg.K_PERCENT

        self.QUIT = pyg.QUIT




    def GetActiveKeys(self):
        return pyg.key.get_pressed()

    def WindowShouldClose(self, closeWindowKey='StartAtomic().K_ESC') -> bool:
        if closeWindowKey == 'StartAtomic().K_ESC':
            closeWindowKey = self.K_ESC

        keys = self.GetActiveKeys()
        if keys[closeWindowKey]:
            return True
        else:
            return False

    def Close(self): pyg.quit()


class Window(StartAtomic):
    def __init__(self, title, size: tuple):
        self.Size = size
        self.Width, self.Height = self.Size
        self.BgColor = (255, 255, 255)
        self.screen = pyg.display.set_mode(self.Size)
        self.screen.fill(self.BgColor)
        self.Default_Icon = pyg.image.load('./AtomicEngine/GameDefaultIcon.PNG')
        pyg.display.set_icon(self.Default_Icon)
        self.caption = title
        pyg.display.set_caption(self.caption)

    def SetBGColor(self, color: tuple) -> None:
        self.BgColor = color
        self.screen.fill(self.BgColor)


    def SetCaption(self, caption: str) -> None:
        self.caption = str(caption)
        pyg.display.set_caption(self.caption)

    def DrawRectangle(self, rect) -> None:
        Rect = pyg.Rect(rect.position.x, rect.position.y,
                 rect.width, rect.height)
        pyg.draw.rect(self.screen, rect.RGB, Rect)

    def Update(self) -> None:
        try:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()

            pyg.display.update()

        except pyg.error:
            pyg.quit()
            return

class GetMouse(StartAtomic):
    def __init__(self):
        self.position = Vector2(pyg.mouse.get_pos()[0], pyg.mouse.get_pos()[1])
        self.MouseVisible = True
        pyg.mouse.set_visible(self.MouseVisible)
class Clock(StartAtomic):
    def __init__(self):
        self.__Clock = pyg.time.Clock()

    def GET_FPS(self) -> float: return float(self.__Clock.get_fps())

    def GET_TIME(self): return self.__Clock.get_time()

    def GET_RAW_TIME(self): return self.__Clock.get_rawtime()

    def Tick(self, frames: int) -> None:
        self.__Clock.tick(frames)

class Events(StartAtomic):
    def __init__(self):
        self.events = []

    def Get_Events(self) -> list:
        return pyg.event.get()


@dataclass
class Vector2:
    x: float
    y: float

@dataclass
class Vector3:
    x: float
    y: float
    z: float

@dataclass
class File_Path:
    Path: str

class Rectangle(StartAtomic):
    def __init__(self, color: tuple, position: Vector2, size: tuple):
        self.width, self.height = size
        self.position = position
        self.RGB = color
        self.Surface = pyg.Rect(self.position.x, self.position.y,self.width, self.height)
    def Anchor(self, surface): pyg.clamp()

    def __str__(self):
        return {
            'width': self.width,
            'height': self.height,
            'x': self.position.x,
            'y': self.position.y
        }
