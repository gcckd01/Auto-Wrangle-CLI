import os
import pandas as pd
import typer
from groq import Groq
from dotenv import load_dotenv
from typing import List

load_dotenv()
# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app = typer.Typer()

def get_cleaning_code(df_sample, instruction):
    """Generates Python code using Groq's Llama model."""
    prompt = f"""
    You are a Senior Data Engineer. 
    DATASET SAMPLE:
    {df_sample.to_string()}
    
    USER INSTRUCTION: "{instruction}"
    
    TASK: Write a Python function `clean_data(df)` that performs the requested task.
    - Use pandas as `pd`.
    - Return ONLY the Python code. No markdown, no backticks, no explanations.
    - Ensure the function returns the modified DataFrame.
    """
    
    # Using Llama-3.3-70b-versatile for high-quality code generation
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    
    raw_code = completion.choices[0].message.content.strip()
    return raw_code.replace("```python", "").replace("```", "").strip()

@app.callback(invoke_without_command=True)
def main(
    file: str, 
    task: List[str]
):
    full_task = " ".join(task)
    typer.echo(f"Processing: {file}")
    
    try:
        df = pd.read_csv(file)
        
        typer.echo("AI (Groq) is drafting the cleaning script...")
        cleaning_script = get_cleaning_code(df.head(5), full_task)
        
        typer.echo("Executing logic...")
        exec_globals = {"pd": pd}
        exec_locals = {}
        exec(cleaning_script, exec_globals, exec_locals)
        
        if "clean_data" in exec_locals:
            df_final = exec_locals["clean_data"](df)
            df_final.to_csv("cleaned_output.csv", index=False)
            typer.echo("Success! File saved as cleaned_output.csv")
        else:
            typer.echo("Error: AI failed to generate the function.")

    except Exception as e:
        typer.echo(f"Error: {e}")

if __name__ == "__main__":
    app()