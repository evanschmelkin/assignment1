import random

def wrap(tag, content):
    """Wraps content in an HTML tag."""
    return f"{tag}{content}{tag.replace('<', '</')}"

def read_config():
    """Reads a simple config file and returns settings."""
    config = {}

    config_file = open("config.txt", "r")
    for line in config_file:
        #splits everything left of = into key and right of = into value
        if "=" in line:
            line = line.strip()
            split_line = line.split("=")

            key = split_line[0]
            value = split_line[1]
            config[key] = value




    return config

def generate_table(rows, cols, bg1, bg2):
    """Creates a table of random letters with alternating colors."""
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", rows * cols)
    rows_html = []

    for i in range(rows):
        row_html = "<tr>"
        for j in range(cols):
            if (i + j) % 2 == 0:
                bg_color = bg1
            else:
                bg_color = bg2
            row_html = row_html + f"<td style='padding: 20px; font-size: 24px; background-color:{bg_color}; text-align:center;'>{letters.pop()}</td>"
        row_html = row_html + "</tr>"
        rows_html.append(row_html)

    return wrap("<table border='1' style='border-collapse: collapse; margin: auto;'>", "\n".join(rows_html))

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

    html_file = open("pa1.html", "w")
    html_file.write(html_content)

    #debug line for the console so we know what's going on
    print("HTML file 'pa1.html' has been created.")

generate_html()
