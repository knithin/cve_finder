# CVE Finder

This project is a simple Django application that retrieves CVEs (Common Vulnerabilities and Exposures) from the National Vulnerability Database (NVD) API and displays them in a web page.

## Prerequisites

- Python 3.x
- Django 3.x
- requests library

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/knithin/cve_finder.git
   
2. Navigate to the project directory:
cd cve_finder

3. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate

4. Install the dependencies:
pip install -r requirements.txt

5. Run the Django development server:

python manage.py runserver

Open your web browser and navigate to http://localhost:8000/cves/ to see the list of new CVEs.
