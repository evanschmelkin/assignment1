import random
import datetime

def wrap_in_tag(tag, content):
    """Wraps the given content in the specified HTML tag."""
    return f"{tag}{content}{tag.replace('<', '</')}"

def load_config(filename="config.txt"):
    """Reads configuration from the file and returns necessary settings."""
    config = {}
    table_data = []
    mode = None

    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        raise ValueError(f"File '{filename}' not found. Please ensure the config file is in the correct directory.")

    for line in lines:
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            key, value = parts
            config[key] = value
        elif parts[0] in ("IMAGES", "LETTERS"):
            mode = parts[0]
            config["MODE"] = mode
        elif mode and mode == "LETTERS":  
            table_data.append(parts)

    if "MODE" not in config or not table_data:
        raise ValueError("Invalid config format! Ensure that 'LETTERS' mode and table size are properly defined.")

    return config, table_data

def create_table(config, table_size):
    """Generates an HTML table with random, non-repeating letters based on the config."""
    try:
        rows, cols = map(int, table_size[0][0].split('x'))
    except (IndexError, ValueError):
        raise ValueError("Invalid table size in config.txt. Please use the format 'NxM' for the table dimensions.")

    if rows * cols > 52:
        raise ValueError("Oops! The grid can't have more than 52 cells to fit unique letters. Please adjust the dimensions.")

    # Select random letters from the alphabet
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", rows * cols)
    table_data = [letters[i * cols: (i + 1) * cols] for i in range(rows)]

    table_html = []
    for i, row in enumerate(table_data):
        row_html = "<tr>"
        for j, letter in enumerate(row):
            bg_color = config["CELL_BACKGROUND1"] if (i + j) % 2 == 0 else config["CELL_BACKGROUND2"]
            row_html += f'''
                <td style="background-color:{bg_color}; 
                           text-align:center; 
                           padding:20px; 
                           font-size:28px; 
                           font-weight:bold; 
                           font-family: 'Courier New', monospace; 
                           border-radius: 10px;
                           transition: transform 0.3s;">
                    {letter}
                </td>
            '''
        row_html += "</tr>"
        table_html.append(row_html)

    return wrap_in_tag(f'''
        <table style="margin:auto; 
                      width:60%; 
                      border-collapse:collapse; 
                      border: {config["TABLE_BORDER_PX"]}px solid {config["TABLE_BORDER_COLOR"]}; 
                      box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);">
    ''', "\n".join(table_html))

def generate_html_page():
    """Generates an HTML page based on the config settings and the table data."""
    config, table_size = load_config()

    date_today = datetime.datetime.now().strftime("%Y-%m-%d")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{config["TITLE"]}</title>
        <style>
            body {{ 
                background-color: {config["BODY_BACKGROUND"]}; 
                text-align: center; 
                font-family: Arial, sans-serif; 
                color: white;
            }}
            table, td {{ 
                border: {config["TABLE_BORDER_PX"]}px solid {config["TABLE_BORDER_COLOR"]}; 
            }}
            td:hover {{
                transform: scale(1.1);
                transition: transform 0.3s;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <h1 style="color: {config["TABLE_BORDER_COLOR"]}; font-size: 40px;">{config["TITLE"]}</h1>
        <h3 style="color: #F8BD7F;">By {config["AUTHORS"]}</h3>
        {create_table(config, table_size)}
        <p style="margin-top: 20px;">Generated on {date_today}</p>
    </body>
    </html>
    """

    # Save the generated HTML to a file
    try:
        with open("pa1.html", "w") as file:
            file.write(html_content)
        print("HTML file 'pa1.html' has been successfully generated.")
    except Exception as e:
        print(f"An error occurred while writing the HTML file: {e}")

if __name__ == "__main__":
    generate_html_page()
