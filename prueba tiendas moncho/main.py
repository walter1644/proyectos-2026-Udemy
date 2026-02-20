# ─── Punto de Entrada ────────────────────────────────────────────────────────
from tkinter import Tk
from interfaz import construir_ui


def main():
    app = Tk()
    construir_ui(app)
    app.mainloop()


if __name__ == '__main__':
    main()
