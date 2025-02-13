import random

def wrap(tag, content):
    """Wraps content in an HTML tag."""
    return f"{tag}{content}{tag.replace('<', '</')}"

def read_config(filename="config.txt"):
    """Reads a simple config file and returns settings."""
    config = {}
    
    with open(filename, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
    
    return config

def generate_table(rows, cols, bg1, bg2):
    """Creates a table of random letters with alternating colors."""
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", rows * cols)
    rows_html = []

    for i in range(rows):
        row_html = "<tr>"
        for j in range(cols):
            bg_color = bg1 if (i + j) % 2 == 0 else bg2
            row_html += wrap("<td style='padding: 20px; font-size: 24px; background-color:" + bg_color + "; text-align:center;'", letters.pop())
        row_html += "</tr>"
        rows_html.append(row_html)

    return wrap("<table border='1' style='border-collapse: collapse; margin: auto;'", "\n".join(rows_html))

def generate_html():
    """Creates an HTML file using config settings."""
    config = read_config()
    
    rows, cols = map(int, config["TABLE_SIZE"].split("x"))
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
            body {{ background-color: {body_bg}; text-align: center; font-family: Arial, sans-serif; color: white; }}
            table {{ border: 2px solid {border_color}; }}
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

    with open("pa1.html", "w") as file:
        file.write(html_content)

    print("HTML file 'pa1.html' has been created.")

if __name__ == "__main__":
    generate_html()
