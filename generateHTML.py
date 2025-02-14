import random
#generateHTML.py
#Evan, Antonio, and Ibrahim
#2/11/2025
#Takes the user input and generates an HTML file
def wrap(tag, content):
    """Wraps content in an HTML tag."""
    return f"{tag}{content}{tag.replace('<', '</')}"

def read_config():
    """Reads a simple config file and returns settings."""
    config = {}

    config_file = open("config.txt", "r")
    lines = config_file.readlines()

    # Read the 9th line for rows and columns (line 9, index 8)
    table_size = lines[8].strip()  # Get the 9th line
    rows, cols = map(int, table_size.split("x"))  # Split by 'x' and convert to integers

    config["ROWS"] = rows
    config["COLS"] = cols

    # Read the rest of the config file
    for line in lines:
        if "=" in line:
            line = line.strip()
            split_line = line.split("=")
            key = split_line[0]
            value = split_line[1]
            config[key] = value

    return config

def generate_table(rows, cols, bg1, bg2):
    """Creates a table of random letters with alternating colors."""
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", rows * cols)
    rows_html = []

    for i in range(rows):
        row_html = "<tr>"
        for j in range(cols):
            if (i + j) % 2 == 0:
                bg_color = "bg1"
            else:
                bg_color = "bg2"
            row_html += f"<td class='{bg_color}'>{letters.pop()}</td>"
        row_html += "</tr>"
        rows_html.append(row_html)

    return wrap("<table class='letter-table'>", "\n".join(rows_html))

def generate_html():
    """Creates an HTML file using config settings."""
    config = read_config()
    rows = config["ROWS"]
    cols = config["COLS"]

    title = config["TITLE"]
    authors = config["AUTHORS"]
    body_bg = config["BODY_BACKGROUND"]
    border_color = config["TABLE_BORDER_COLOR"]
    cell_bg1 = config["CELL_BACKGROUND1"]
    cell_bg2 = config["CELL_BACKGROUND2"]

    html_content = f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                background-color: {body_bg};
                text-align: center;
                font-family: Arial, sans-serif;
                color: white;
            }}
            .letter-table {{
                border-collapse: collapse;
                margin: auto;
                border: 2px solid {border_color};
            }}
            .letter-table td {{
                padding: 20px;
                font-size: 24px;
                text-align: center;
            }}
            .bg1 {{ background-color: {cell_bg1}; }}
            .bg2 {{ background-color: {cell_bg2}; }}
        </style>
    </head>
    <body>
        {wrap('<h1>', title)}
        {wrap('<h3>', 'By ' + authors)}
        {generate_table(rows, cols, cell_bg1, cell_bg2)}
        {wrap('<p>', 'Generated with Python')}
    </body>
    </html>
    """

    html_file = open("pa1.html", "w")
    html_file.write(html_content)

    # Debug line for the console so we know what's going on
    print("HTML file 'pa1.html' has been created.")

generate_html()
