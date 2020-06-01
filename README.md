# HTML -> PDF -> JPEG

This application converts html file to jpeg file through pdf file. It can be useful for [diagrams.net](https://www.diagrams.net/). 

## Installation

1. Install additional packages through pip command. 
    ```bash:install_requirements.txt
    python -m venv .env
    .env/Scripts/pip.exe install -r requirements.txt
    ```
1. Install Windows Subsystem for Linux (WSL). 
1. Install xpdf through apt command on WSL. 
    ```bash:install_xpdf
    sudo apt install xpdf
    ```

## Usage

Run the application. 

```bash:how_to_use
python3 /to/the/path/html2pdf2jpeg/html2pdf2jpeg.py
```

And then open-file-dialog will be open and you will be able to select the html file which you want to convert. 
