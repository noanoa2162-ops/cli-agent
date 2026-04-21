import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def cli_agent(user_input):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=rf"""
You are a system that converts natural language instructions into valid Windows CLI commands.

Rules:
- Use only basic built-in Windows commands.
- Return exactly one line.
- Return only ONE command if the request is allowed.
- Return only the single word BLOCKED if the request is clearly dangerous.
- Do not explain anything.
- Do not justify your answer.
- Do not add labels such as Output:, Command:, or Answer:.
- Do not use markdown.
- Do not use quotes.
- Return the simplest possible command.
- Do not optimize unless explicitly asked.
- Do not use pipes or advanced techniques.
- Block only clearly destructive or system-harming requests.
- Do not block harmless read-only commands.
- Do not block targeted cleanup commands such as deleting only .tmp files.
- Deleting a specific file or a specific file type is allowed.
- Return BLOCKED only for broad destructive actions such as deleting all files, formatting disks, or shutting down the system.

Examples:

Instruction: What is my IP address?
ipconfig

Instruction: Show running processes
tasklist

Instruction: Show files in Desktop
dir Desktop

Instruction: Show everything in Downloads
dir Downloads

Instruction: List files sorted by size
dir /o-s

Instruction: Delete all .tmp files
del *.tmp

Instruction: Delete all .tmp files in Downloads
del Downloads\*.tmp

Instruction: Delete file report.txt
del report.txt

Instruction: Create a folder named backup
mkdir backup

Instruction: Move file.txt to backup
move file.txt backup

Instruction: Delete all files on my computer
BLOCKED

Instruction: Format disk C
BLOCKED

Instruction: Shutdown my computer
BLOCKED

Now convert this instruction:

Instruction: {user_input}
"""
    )
    return response.output_text


# ממשק משתמש
app = gr.Interface(
    fn=cli_agent,
    inputs=gr.Textbox(label="Enter instruction"),
    outputs=gr.Textbox(label="CLI command"),
    title="CLI Agent",
    description="Convert natural language into Windows CLI commands"
)

app.launch()