Project Documentation: Auto-Wrangle CLI
AI-Powered Automated Data Engineering Tool
While analyzing datasets of 1,000+ retail leads, the manual effort required for data cleaning became a significant bottleneck. This tool was developed to automate exploratory data analysis (EDA) and preprocessing by utilizing LLMs to generate and execute local Python code.

1. Functional Overview
The Auto-Wrangle CLI acts as an autonomous agent that bridges the gap between natural language instructions and technical data manipulation. It takes a raw CSV file and a task description, then synthesizes a custom Pandas script to perform the requested operations.

Key Technical Features:

Context-Aware Synthesis: The agent analyzes a sample of the data schema to ensure the generated code is compatible with existing column names and types.

Local Processing Engine: AI generates the logic, but the actual execution happens on the user's local machine, ensuring data remains private and secure.

High-Performance Inference: Integration with Groq (Llama 3.3) and Gemini 2.0 provides near-instant response times for complex cleaning logic.

2. Practical Use Cases
Example A: Missing Value Imputation
Command: python main.py "leads.csv" Fill nulls in Customer Rating with 0 and fill Cancellation Reason with 'N/A'

Analysis: Prevents data loss during modeling by replacing nulls instead of dropping rows.

Example B: Feature Engineering and Type Conversion
Command: python main.py "sales.csv" Convert all columns ending in 'Date' to datetime and calculate 'Lead_Age' as today minus Lead Date


Analysis: Prepares the dataset for time-series forecasting by standardizing types and creating new metrics.

Example C: Categorical Standardization
Command: python main.py "leads.csv" Convert Store Name to uppercase and Lead Type to lowercase


Analysis: Ensures consistency in categorical variables, which is critical for accurate SQL grouping and Power BI visualization.

3. Configuration and Security
This project utilizes environment variables to manage sensitive credentials. You must provide your own API key to use the tool.

Installation Steps:
Clone the Repository:

Set up Environment:
Create a .env file in the root directory and add your key (you can use groq for free API keys)



4. Performance Metrics
Testing conducted on a standard retail lead dataset showed significant efficiency gains over manual scripting:


Manual Scripting (Pandas): ~45 minutes for full cleaning and validation.

Auto-Wrangle CLI: <15 seconds for code generation and execution.

Accuracy: 95%+ for standard data cleaning tasks, including type conversion and null handling.

5. Technical Skills Demonstrated
Backend Development: Python, Typer, CLI Architecture.


Data Engineering: Pandas, ETL Pipelines, Schema Analysis.


AI/ML Integration: LLM Prompt Engineering, API Orchestration, Code Synthesis.


#also attatching a dataset u can try to !!
