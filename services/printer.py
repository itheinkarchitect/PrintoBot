import win32print
import win32ui

PRINTER_NAME = "Canon LBP2900"

def print_text(text: str):
    try:
        dc = win32ui.CreateDC()
        dc.CreatePrinterDC(PRINTER_NAME)

        dc.StartDoc("Telegram Print")
        dc.StartPage()

        dc.TextOut(100, 100, text)

        dc.EndPage()
        dc.EndDoc()

        dc.DeleteDC()
        return True
    except Exception:
        return False