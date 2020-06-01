import sys
from pathlib import Path


def main():
    pass


def get_filename():
    if len(sys.argv) == 2:
        html_filename = sys.argv[1]
        if not Path.exists(html_filename):
            html_filename = ""
            raise FileNotFoundError
    else:
        import tkinter
        from tkinter.filedialog import askopenfilename
        root = tkinter.Tk()
        root.withdraw()
        html_filename = askopenfilename(
            filetypes=[
                ("HTML Files", "*.HTML;*.HTM")],
            initialdir=str(Path.home() / "Downloads")
        )

        if html_filename == "":
            raise FileNotFoundError

    print(html_filename)
    return html_filename


if __name__ == "__main__":
    main()
