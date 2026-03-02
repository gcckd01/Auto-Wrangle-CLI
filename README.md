Auto-Wrangle CLI: AI-Powered Data Cleaning Agent
While managing some dataset I found that manual data wrangling was the biggest bottleneck in my workflow. I built this CLI tool to automate the "boring" parts of data science, allowing you to go from raw CSV to analysis-ready data using simple English commands.

Practical Examples 
To give you a better idea of what the agent can do, try these commands on any messy dataset:

1. The "Analyst Special" (Handling Nulls & Text)
Command: python main.py "leads.csv" Fill nulls in Customer Rating with 0 and convert Store Name to uppercase


Scenario: You have a retail sheet where 30% of ratings are missing.


AI Action: Instead of deleting rows, it intelligently fills missing ratings and standardizes store names for consistent Power BI reporting.

2. Time-Series Preparation
Command: python main.py "sales.csv" Convert all columns ending in 'Date' to datetime and calculate a new column 'Lead_Age' as today minus Lead Date


Scenario: Your dates are stored as strings, making time analysis impossible.


AI Action: It identifies date columns, converts their types, and performs feature engineering on the fly.

3. Data Segmenting
Command: python main.py "leads.csv" Filter for Lead Type 'Warm' or 'Hot' and remove the 'Cancellation Reason' column


Scenario: You want to focus only on high-conversion leads.


AI Action: It performs row filtering and column dropping in one step, reducing your file size for faster processing.

API Security & Setup
To protect your credentials, this tool uses a .env file. Never share your .env file or commit it to GitHub.

1. Installation
2. Add Your Own API Key
Create a file named .env in the root folder.

Paste your key inside (Get one for free at ):

Note: Ensure .env is listed in your .gitignore file so it stays private.

Tech Stack

Python (Pandas): Core data engine.

Type: Professional CLI interface.

Groq: LLM-powered code generation.

Python-Dotenv: Secure environment management.

Impact Analysis
On a sample of 1,000 retail leads, this tool reduced the time spent on "Initial EDA and Cleaning" from 45 minutes of manual coding to under 15 seconds of CLI execution.

I am also attatching a raw data sheet for you to try !!
