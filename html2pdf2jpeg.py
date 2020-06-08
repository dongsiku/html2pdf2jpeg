import sys
from pathlib import Path
import argparse

from html2pdf import HTML2PDF
from pdf2jpeg import pdf2jpeg


def main():
    h2p = HTML2PDF()
    html_filename, image_resolution = get_filename_and_resolution()
    saved_pdf_filename = h2p.html2pdf(html_filename)
    pdf2jpeg(saved_pdf_filename, image_resolution)


def get_filename_and_resolution():
    parser = argparse.ArgumentParser(
        description='Specify the filename and output image file resolution')
    parser.add_argument('--filename', help='Specify the file name')
    parser.add_argument(
        '--resolution', '-r', type=int, default=600,
        help='Specify output image resolution (dpi)')
    args = parser.parse_args()

    if args.filename is not None:
        html_filename = args.filename
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
    return html_filename, args.resolution


if __name__ == "__main__":
    main()
