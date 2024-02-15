import os
import time
from datetime import datetime

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = None


@pytest.fixture(autouse=True)
def setup(request):
    global driver
    # launching chrome and opening NRLAIS website
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.implicitly_wait(60)
    driver.get("http://192.168.56.101:8888//")
    driver.maximize_window()
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://10.235.37.118:8888/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = str(int(round(time.time() * 1000))) + ".png"
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "NRLAIS Automation Report"


# def pytest_html_results_table_header(cells):
#     cells.insert(2, "<th>Description</th>")
#     cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')
#
#
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, f"<td>{report.description}</td>")
#     cells.insert(1, f'<td class="col-time">{datetime.utcnow()}</td>')
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
