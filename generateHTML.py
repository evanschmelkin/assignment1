import random
import datetime

# generateHTML.py
# Evan, Antonio, and Ibrahim
# 2/11/2025
# Takes the user input and automatically generates an HTML file using Python
# Includes an automatic datetime function to show when the page was generated
# Programming Assignment 1

def wrap(tag, content):
    #wraps the content in an html tag
    return f"{tag}{content}{tag.replace('<', '</')}"

def read_config():
    #this turns config.txt file into usable tags for the code
    config = {}

    config_file = open("config.txt", "r")
    lines = config_file.readlines()

    #this takes the 9th line which is the stuff for the number of rows and columns
    table_size = lines[8].strip()  # get the 9th line
    table_size = table_size.split("x")  # split rows and columns with the x

    rows = int(table_size[0])  #left of x is the rows
    cols = int(table_size[1])  #right of x is the columns

    config["ROWS"] = rows
    config["COLS"] = cols

    # read the rest of the config file
    for line in lines:
        if "=" in line:
            line = line.strip()
            split_line = line.split("=")
            key = split_line[0]
            value = split_line[1]
            config[key] = value

    return config

def generate_table(rows, cols, bg1, bg2):
    #creates a table of random upper case and lower case letters
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", rows * cols)
    rows_html = []

    for i in range(rows):
        row_html = "<tr>"
        for j in range(cols):
            if (i + j) % 2 == 0:
                bg_color = bg1
            else:
                bg_color = bg2
            row_html = row_html + f"<td class='{bg_color}'>{letters.pop()}</td>"
        row_html = row_html + "</tr>"
        rows_html.append(row_html)

    return wrap("<table>", "\n".join(rows_html))

def generate_html():
    #this function creates an html file based on the config.txt
    config = read_config()

    rows = config["ROWS"]
    cols = config["COLS"]

    title = config["TITLE"]
    authors = config["AUTHORS"]
    body_bg = config["BODY_BACKGROUND"]
    border_color = config["TABLE_BORDER_COLOR"]
    cell_bg1 = config["CELL_BACKGROUND1"]
    cell_bg2 = config["CELL_BACKGROUND2"]
    table_border_px = config["TABLE_BORDER_PX"]

    html_content = f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{ background-color: {body_bg}; text-align: center; font-family: Arial, serif; color: white; }}
            table {{ border: {table_border_px}px solid {border_color}; width: 60%; margin: auto; }}
            td {{ font-size: 24px; text-align: center; padding: 20px; }}
            .{cell_bg1} {{ background-color: {cell_bg1}; }}
            .{cell_bg2} {{ background-color: {cell_bg2}; }}
        </style>
    </head>
    <body>
        {wrap('<h1>', title)}
        {wrap('<h3>', 'By ' + authors)}
        {generate_table(rows, cols, cell_bg1, cell_bg2)}
        {wrap('<p>', "Created automatically for COM214 HW1 on: " + str(datetime.datetime.now()))}
    </body>
    </html>
    """

    #even if pa1.html isn't created yet, this will create the file
    #and then will write the html_content (the string from generate_html
    #into this file
    html_file = open("pa1.html", "w")
    html_file.write(html_content)

    #debug line for the console so we know what's going on
    print("HTML file 'pa1.html' has been created.")

#calls the function
generate_html()
