import nbformat as nbf

# Path to your questions file
questions_file = "questions.txt"
output_notebook = "questions_with_solutions.ipynb"

# Create a new notebook object
nb = nbf.v4.new_notebook()
cells = []

# Read all questions
with open(questions_file, "r", encoding="utf-8") as file:
    questions = file.readlines()

# Loop over each question
for i, question in enumerate(questions):
    question = question.strip()
    if not question:
        continue  # skip empty lines

    # Markdown cell for question
    markdown_cell = nbf.v4.new_markdown_cell(f"### Question {i+1}:\n\n{question}")
    cells.append(markdown_cell)

    # Empty code cell for solution
    code_cell = nbf.v4.new_code_cell("# Write your solution here")
    cells.append(code_cell)

# Assign cells to notebook
nb['cells'] = cells

# Write notebook to file
with open(output_notebook, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook '{output_notebook}' created with {len(questions)} questions.")
