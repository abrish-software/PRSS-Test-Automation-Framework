
## PRSS Test Automation Framework

This repository contains a test automation framework developed for the Property Registration subsystem (PRSS).

### Structure Overview

The repository comprises the following seven subfolders:

- **base**: Contains base classes for all test cases, such as login and logout functionalities, primarily consisting of the driver class.
  
- **page**: Stores role-specific modules (officer, expert, supervisor) for various test cases.

- **reports**: Holds reports and error screenshots generated after running test automation.

- **testcases**: Contains the actual test cases along with the `conftest.py` file, which centralizes configuration for all files.

- **testdata**: Stores test data utilized by different test cases.

- **utilities**: Contains shared methods utilized by test cases.

### Pre-automation Setup

Before initiating test automation, follow these steps:

1. Clone the repository onto your local machine.

2. Download PyCharm and import the test automation project into PyCharm.

3. Navigate to the `testcases` folder and edit the URL in the `conftest.py` file.

4. Adjust attachments locations by accessing the `testdata` folder.

### Running Automation Tests

To run automation tests on your machine:

1. Navigate to the project directory using the terminal. For example: `C:\Python-Selenium\TestFrameWorkDemo`.

2. Move to the test case you want to execute, preceding it with `pytest`. For instance: `pytest testcases/specialcase_test.py`.

3. Optionally, append a report to the command. For example: `pytest testcases/specialcase_test.py --html=reports/specialcase.html`.

4. Hit Enter to start the test automation process.

### Note
For test cases involving CMSS tasks, the system will wait for a specified amount of time, as outlined in the script, until the user completes the respective CMSS tasks. If the user fails to input the data within the specified timeframe, the automation test will fail.
