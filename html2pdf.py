from selenium import webdriver
import chromedriver_binary  # 83.0.4103.61
from pathlib import Path
from time import sleep
import json
from datetime import datetime
import os


class HTML2PDF:
    def __init__(self):
        self.PROJ_DIRNAME = Path(__file__).parent.resolve()
        self.DOWNLOAD_DIRNAME = self.PROJ_DIRNAME / 'downloads'
        self.DOWNLOAD_DIRNAME.mkdir(exist_ok=True)
        print(self.DOWNLOAD_DIRNAME)
        self.SELENIUM_DELAY_TIME = 4

    def html2pdf(self, html_filename: str) -> str:
        html_title = self.save_as_pdf_file(html_filename)
        defalut_pdf_filename = os.path.join(
            str(self.DOWNLOAD_DIRNAME),
            # os.path.basename(html_filename).replace(
            #     ".html",
            #     ".pdf"
            # )
            "{}.pdf".format(html_title)
        )
        saved_pdf_filename = defalut_pdf_filename.replace(
            ".pdf", "_{0:%Y%m%d_%H%M%S}.pdf".format(datetime.now())
        )
        os.rename(defalut_pdf_filename, saved_pdf_filename)

        return saved_pdf_filename

    def save_as_pdf_file(self, html_filename: str) -> str:

        options = webdriver.ChromeOptions()
        appState = {
            "recentDestinations": [
                {
                    "id": "Save as PDF",
                    "origin": "local",
                    "account": ""
                }
            ],
            "selectedDestinationId": "Save as PDF",
            "version": 2,
            "isHeaderFooterEnabled": False
        }

        prefs = {
            'savefile.default_directory': str(self.DOWNLOAD_DIRNAME),
            'printing.print_preview_sticky_settings.appState':
            json.dumps(appState)
        }
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--kiosk-printing')
        driver = webdriver.Chrome(options=options)

        driver.get("file:///{}".format(html_filename))
        # driver.implicitly_wait(self.SELENIUM_DELAY_TIME)
        sleep(self.SELENIUM_DELAY_TIME)
        driver.execute_script('window.print();')
        sleep(self.SELENIUM_DELAY_TIME)
        html_title = driver.title
        driver.quit()

        return html_title


if __name__ == "__main__":
    h2p = HTML2PDF()
    test_html_filename = str(h2p.PROJ_DIRNAME / "test" / "test.html")
    h2p.html2pdf(test_html_filename)
