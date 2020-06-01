import sys
from pathlib import Path

from html2pdf import HTML2PDF
from pdf2jpeg import pdf2jpeg


def main():
    h2p = HTML2PDF()
    saved_pdf_filename = h2p.html2pdf(get_filename())
    pdf2jpeg(saved_pdf_filename)


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
