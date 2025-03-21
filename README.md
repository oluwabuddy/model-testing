# Model Testing

This repository contains automated UI, API tests for the Model Training Workflow using Cypress with the Page Object Model (POM) and Pytest for the api test.

## 📌 Prerequisites

- Node.js (Download: https://nodejs.org/)
- Git
- Cypress (`npm install cypress --save-dev`)

## 🚀 How to Run Locally

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/cypress-model-testing.git
   cd cypress-model-testing
   
2. Navigate to the project directory
   ```sh
   cd model-testing
3. Install dependencies
   For UI Tests (Cypress):
   ```sh
   npm install
   
4. For API Tests:
   ```sh
   pip install -r requirements.txt

## Running the Application
   
- Start the application using Docker:
   ```sh
   docker-compose -f docker-compose.local.yml up
   
 The frontend will be available at:
 http://127.0.0.1:8001/


## Running Tests

- Run UI Tests (Cypress)
  To run all Cypress tests in headless mode:
   ```sh
  npx cypress run

 - To open Cypress Test Runner GUI
   ```sh
   npx cypress open

 - Run API Tests (test_api.py)
   Execute the API tests using pytest:
    ```sh
    cd api
    pytest test_api.py
    
## Project Structure

```bash
📦 cypress-model-testing
│── 📂 cypress
│   ├── 📂 e2e               # Cypress UI test cases
│   ├── 📂 pageObjects       # Page Object Model files
│   ├── 📂 fixtures          # Test data
│   ├── 📂 support           # Cypress support files
│── 📂 tests
│   ├── test_api.py          # API test cases using pytest
│── 📜 docker-compose.local.yml
│── 📜 cypress.config.js
│── 📜 package.json
│── 📜 requirements.txt
│── 📜 README.md



