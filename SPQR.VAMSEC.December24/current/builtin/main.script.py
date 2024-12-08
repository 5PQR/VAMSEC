


print("------------------------------------------------------------------------------------")
print("                                                                              ")
print("                    .M\"\"\"bgd `7MM\"\"\"Mq.   .g8\"\"8q. `7MM\"\"\"Mq.         ")
print("                   ,MI    \"Y   MM   `MM..dP'    `YM. MM   `MM.                  ")
print("                   `MMb.       MM   ,M9 dM'      `MM MM   ,M9                    ")
print("                     `YMMNq.   MMmmdM9  MM        MM MMmmdM9                     ")
print("                   .     `MM   MM       MM.      ,MP MM  YM.                     ")
print("                   Mb     dM   MM       `Mb.    ,dP' MM   `Mb.                   ")
print("                   P\"Ybmmd\"  .JMML.       `\"bmmd\"' .JMML. .JMM.              ")
print("                                              MMb                                ")
print("                                               `Ybm9'                            ")
print("====================================================================================")
print("------------------------------------------------------------------------------------")
print("    HELP ME MAKE MORE VAM TOOLS AT: PATREON.COM/SPQR_AETERNUM !")
print("====================================================================================")
print(f"Starting! This might take a while depending on your vam folder size.")
import os
import html
import zipfile
import re
import csv
import config
import webbrowser

def find_openurl_in_var(path):
    results = []

    # Traverse through the folder AddonPackages recursively
    for root, dirs, files in os.walk(path):
        
        if any(f.lower().endswith('.var') for f in files):
            print(f"=== CHECKING VAR ARCHIVES ===")
            # Handle .var files (which are zip archives)
            for file in files:
                if file.lower().endswith('.var'):
                    var_path = os.path.join(root, file)
                    try:
                        with zipfile.ZipFile(var_path, 'r') as zip_ref:
                            for zip_file in zip_ref.namelist():
                                if zip_file.lower().endswith('.cs'):
                                    print(f"= CHECKING FILE: "+zip_file+"=")
                                    with zip_ref.open(zip_file) as f:
                                        # Read the bytes and decode them
                                        lines = f.read().decode('utf-8', errors='ignore').splitlines()
                                        # Split lines by ';' and process
                                        split_lines = ''.join(lines).split(';')
                                        for i, line in enumerate(split_lines):
                                            if config.search_for.encode('utf-8') in line.encode('utf-8'):
                                                # Get 3 lines before and after, if available
                                                context = []
                                                for j in range(max(0, i - 3), min(len(split_lines), i + 4)):
                                                    context.append(split_lines[j].strip() + ';\n')
                                                results.append((var_path, ' '.join(context)))
                    except Exception as e:
                        print(f"Error reading .var zip file {var_path}: {e}")

        else:
            print(f"=== CHECKING LOOSE SCRIPTS ===")
            # Third case: Check .cs files directly in the current directory
            for file in files:
                if file.lower().endswith('.cs'):
                    print(f"= CHECKING FILE: "+file+"=")
                    with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        # Split lines by ';' and process
                        split_lines = ''.join(lines).split(';')
                        for i, line in enumerate(split_lines):
                            if config.search_for in line:
                                # Get 3 lines before and after, if available
                                context = []
                                for j in range(max(0, i - 3), min(len(split_lines), i + 4)):
                                    context.append(split_lines[j].strip()+';\n')
                                results.append((root, ' '.join(context)))

    return results

def write_to_csv(results, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(results)
        
def apply_highlights(content, highlights):
    for highlight in highlights:
        content = content.replace(highlight, f'<span class="highlight">{highlight}</span>')
    return content
    

def format_table_row(res, search_for, highlights):
    # Extract the name and path from res[0]
    file_name = res[0].split('\\')[-1]
    file_path = '\\'.join(res[0].split('\\')[:-1])
    
    # Format res[1] to replace search_for and highlights
    res = (res[0], html.escape(res[1]))  
    formatted_content = res[1].replace(search_for, f'<span>{search_for}</span>')
    for highlight in highlights:
        formatted_content = formatted_content.replace(highlight, f'<span class="highlight">{highlight}</span>')
    
    # Check if any highlight exists in res[1]
    highlight_found = any(highlight in res[1] for highlight in highlights)
    
    # Build the table row
    row = (
        f"<tr>"
        f"<td>{file_name}</td>"
        f"<td>{file_path}</td>"
        f"<td><div>{formatted_content}</div></td>"
        f"<td class=\"{'found' if highlight_found else ''}\"></td>"
        f"</tr>"
    )
    return row
    
def write_to_html(results):
    
    if results == '':
        table_rows = '<h5>No entries found!</h5>'
    else: 
        table_rows = ''.join([format_table_row(res, config.search_for, config.highlights) for res in results])
    try:
        with open('html/results.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        html_content = html_content.replace('[!table!]', table_rows)
        html_content = html_content.replace('[!searchfor!]', config.search_for)
        
        with open('../../result.html', 'w', encoding='utf-8') as result_file:
            result_file.write(html_content)
        
        # Get the absolute path of the file
        file_path = os.path.abspath('../../result.html')

        # Open the file in the default web browser
        webbrowser.open('file://' + file_path)
    
    except FileNotFoundError:
        print("Error: The file 'html/results.html' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    path = config.vam_path
    
    if path == 'PUT VAM PATH HERE':
        print(f"Installed! Open the config.py file in notepad or any text editor and put your VAM folder path, then run this again!")
    else:
    
        results = find_openurl_in_var(path)
        if results:
            write_to_html(results)
            
        else:
            write_to_html('')
        print(f"Done! result.html created and should open now in your browser.")
