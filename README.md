# _Browser use_ browser automation agent setup guide

# Overview

This guide explains how to set up a browser automation agent Browser use, which can automate web interactions using AI.

You can learn more about Browser use on its [GitHub repository](https://github.com/browser-use/browser-use).

# Steps

## 1. Activate Virtual Environment
On Windows:
```sh
.\venv\Scripts\activate
```

On macOS/Linux:
```sh
source venv/bin/activate
```

## 2. Install Requirements
```sh
pip install -r requirements.txt
```

## 3. Install Browser Engine
```sh
playwright install
```

## 4. Set Environment Variables
Copy the `.env.example` file to an `.env` file and fill in the directives.

## 5. Run Example Scripts
```sh
# Run Coursera example
python example-coursera.py

# Run other examples by modifying the TASK variable in the script
```

## 6. Watch the Agent
The agent will automatically:
- Launch a browser
- Navigate to specified websites
- Interact with pages using AI to complete the given task
- Save interaction history to history.json
