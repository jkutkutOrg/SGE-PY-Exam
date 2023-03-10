# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    gui.py                                               ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/07 10:00:56 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 11:06:04 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter
import pathlib

from moneyconversor.style import ConversorStyle as STYLE

from moneyconversor.ui.textfield import TextField
from moneyconversor.ui.label import TitleLabel, SubTitleLabel, NormalLabel
from moneyconversor.ui.radiobutton import Radiobutton
from moneyconversor.ui.checkbutton import Checkbutton
from moneyconversor.ui.button import Button
from moneyconversor.ui.listbox import Listbox

class MoneyConversorGUI:

    D_2_E = 0
    E_2_D = 1

    _TITLE = "Conversor Euro – Dólar USA"
    _TITLE_LABEL = "Conversión de divisas Euro - Dólar USA"

    _WIDTH = 750
    _HEIGHT = 450
    _GEOMETRY = f"{_WIDTH}x{_HEIGHT}+0+0"
    _MIN_SIZE = (_WIDTH, _HEIGHT)
    _MAX_SIZE = (_WIDTH, _HEIGHT)

    def __init__(self):
        self._window = tkinter.Tk()
        self._config_window()
        self._init_components()

    def _config_window(self):
        self.w.title(self._TITLE)
        self.w.config(
           bg = STYLE.BG
        )
        root_dir = pathlib.Path(__name__).parent.resolve()
        self.w.iconphoto(True, tkinter.PhotoImage(file="res/img/logo.png"))
        self._window_frame = tkinter.Frame(
            self.w,
            width = self.width,
            height = self.height,
            bg = STYLE.BG
        )
        self._window_frame.pack_propagate(0)
        self.w.geometry(self._GEOMETRY)
        self.w.maxsize(*self._MAX_SIZE)
        self.w.minsize(*self._MIN_SIZE)
        self._window_frame.pack(
            padx = STYLE.WINDOW_PADDING,
            pady = STYLE.WINDOW_PADDING
        )

    def _init_components(self):
        self._init_title()
        self._init_money_txtbox()
        self._init_conversion_type()
        self._init_submmit()

    def _init_title(self) -> None:
        self._title_frame = tkinter.Frame(
            self.window,
            bg = STYLE.BG
        )
        self._title_frame.pack(
            fill = tkinter.X
        )
        # Title label
        TitleLabel(
            self._title_frame,
            self._TITLE_LABEL
        ).pack(
            side = tkinter.LEFT
        )
        # Logo
        size = 100
        self._canvas = tkinter.Canvas(
            self._title_frame,
            width = size,
            height = size,
            highlightthickness=0
        )
        self._img = tkinter.PhotoImage(file="res/img/logo.png")
        self._canvas.pack(
            side = tkinter.RIGHT
        )
        self._canvas.create_image(0,0, anchor=tkinter.NW, image = self._img)

    def _init_money_txtbox(self) -> None:
        self._data_container = tkinter.Frame(
            self.window,
            bg = STYLE.BG
        )
        self._data_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
        )
        # Section label
        SubTitleLabel(
            self._data_container,
            text = "Cantidad a convertir"
        ).pack(
            anchor = tkinter.NW
        )
        self._data_containers = []
        self._data_containers.append(tkinter.Frame(
            self._data_container,
            bg = STYLE.BG
        ))
        self._data_containers[-1].pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
        )
        self._txtf_money = TextField(
            self._data_containers[-1],
            hint = "Cantidad"
        )
        self._txtf_money.pack(
            side = tkinter.LEFT,
            padx = STYLE.NORMAL_MARGIN
        )

    def _init_conversion_type(self) -> None:
        self._conversion_type_container = tkinter.Frame(
            self.window,
            bg = STYLE.BG
        )
        self._conversion_type_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
        )
        # Section label
        SubTitleLabel(
            self._conversion_type_container,
            text = "Conversión:"
        ).pack(
            anchor = tkinter.NW
        )
        # Types
        self._conversion_types_container = tkinter.Frame(
            self._conversion_type_container,
            bg = STYLE.BG
        )
        self._conversion_types_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
        )
        self._rbtns_value = tkinter.StringVar()
        RADIO_BTNS = [
            ("1 dólar USA = 0,947983 euros", self.D_2_E),
            ("1 Euro = 1,054883 Dólares USA", self.E_2_D)
        ]
        for rbtn_label in RADIO_BTNS:
            Radiobutton(
                self._conversion_types_container,
                text = rbtn_label[0],
                value = rbtn_label[1],
                variable = self._rbtns_value
            ).pack(
                side = tkinter.LEFT,
                padx = STYLE.NORMAL_MARGIN
            )

    def _init_submmit(self) -> None:
        self.btn_submit = Button(
            self.window,
            text = "Convertir"
        )
        self.btn_submit.pack(
            fill = tkinter.X,
            padx = STYLE.NORMAL_MARGIN
        )
        SubTitleLabel(
            self.window,
            text = "Valor de la conversión:"
        ).pack(
            anchor = tkinter.NW,
            pady = STYLE.NORMAL_MARGIN
        )
        self._result_label = NormalLabel(
            self.window,
            text = ""
        )
        self._result_label.pack(
            anchor = tkinter.NW,
            padx = STYLE.NORMAL_MARGIN,
            pady = STYLE.NORMAL_MARGIN
        )


    def run(self) -> None:
        self.w.mainloop()

    # GETTERS
    @property
    def width(self) -> int:
        return self._WIDTH - 2 * STYLE.WINDOW_PADDING

    @property
    def height(self) -> int:
        return self._HEIGHT - 2 * STYLE.WINDOW_PADDING

    @property
    def window(self):
        return self._window_frame

    @property
    def w(self):
        return self._window

    @property
    def conversion_type(self) -> int | None:
        t = self._rbtns_value.get()
        return None if t == '' else int(t)

    @property
    def money(self) -> str:
        return self._txtf_money.get().strip()

    def convert(self, m: float, conversion_type: int, e: float) -> None:
        if conversion_type == self.D_2_E:
            icoin = "$"
            fcoin = "€"
        else:
            icoin = "€"
            fcoin = "$"
        result = f"{m}{icoin} son {e}{fcoin}"
        self._result_label.config(text = result)
