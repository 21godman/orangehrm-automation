### Overview

This project automates the login functionality of the OrangeHRM demo website. The test runs on Google Chrome and shows GUI interactions.

### Prerequisites

1. Python 3.7+: [Download Python](https://www.python.org/downloads/)
2. Google Chrome: Ensure Chrome is installed.
3. ChromeDriver: Download the matching version for your Chrome browser from ChromeDriver Downloads.

### Installation Steps

1. Clone this repository:
    
    git clone <repository_url>
    cd orangehrm-automati
    
2. Install dependencies:
    
    pip install -r requirements.txt
    
3. Place `chromedriver.exe` in the `drivers` folder.
4. Update `config.py`:
    - Set `BASE_URL`, `USERNAME`, and `PASSWORD` as needed.

### Running the Test

1. Run the test:
    
    pytest --html=report.html
    
2. Open `report.html` to view the test results.
3. The browser will launch and show the GUI steps.