import subprocess
from os import path

PROJ_DIRNAME = path.dirname(path.abspath(__file__))


def pdf2jpeg(pdf_filename: str):
    PDF2JPEG_SH_FILENAME = path.join(PROJ_DIRNAME, "pdf2jpeg.sh")
    cmd = 'wsl bash {} {}'.format(
        windows_filename_to_linux_filename(PDF2JPEG_SH_FILENAME),
        windows_filename_to_linux_filename(pdf_filename)
    )
    subprocess.run(cmd.split())


def windows_filename_to_linux_filename(windows_filename: str) -> str:
    if not path.exists(windows_filename):
        raise FileNotFoundError

    windows_drive_name, windows_filename_under_drive =\
        windows_filename.split(":", 1)
    linux_filename = "/mnt/{}{}".format(
        windows_drive_name.lower(),
        windows_filename_under_drive.replace("\\", "/")
    )
    print("{} -> {}".format(windows_filename, linux_filename))
    return linux_filename


if __name__ == "__main__":
    pdf2jpeg(path.join(PROJ_DIRNAME, "test", "test.pdf"))
