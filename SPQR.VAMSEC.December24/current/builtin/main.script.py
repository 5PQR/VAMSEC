


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
import zipfile
import re
import csv
import config
import webbrowser

def find_openurl_in_var(path):
    results = []

    # Traverse through the folder AddonPackages recursively
    for root, dirs, files in os.walk(path):
        print(f"=== CHECKING VAR FOLDERS ===")
        # Check for .var files or folders ending with .var
        if root.endswith('.var'):
            # If it's a folder ending with .var, search recursively for .cs files
            for subroot, subdirs, subfiles in os.walk(root):
                for file in subfiles:
                    if file.lower().endswith('.cs'):
                        print(f"= CHECKING FILE: "+file+"=")
                        with open(os.path.join(subroot, file), 'r', encoding='utf-8', errors='ignore') as f:
                            for line in f:
                                if config.search_for in line:
                                    results.append((root, line.strip()))
        elif any(f.lower().endswith('.var') for f in files):
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
                                        for line in f:
                                            if config.search_for.encode('utf-8') in line:
                                                results.append((var_path, line.decode('utf-8').strip()))
                    except Exception as e:
                        print(f"Error reading .var zip file {var_path}: {e}")
        else:
            print(f"=== CHECKING LOOSE SCRIPTS ===")
            # Third case: Check .cs files directly in the current directory
            for file in files:
                if file.lower().endswith('.cs'):
                    print(f"= CHECKING FILE: "+file+"=")
                    with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if config.search_for in line:
                                results.append((root, line.strip()))

    return results

def write_to_csv(results, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(results)

def write_to_html(results):
    
    if not results:
        table_rows = ''
    else: 
        table_rows = ''.join([ 
            "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                res[0].split('\\')[-1] if res[0].split('\\')[-1].endswith('.var') else "file:"+res[0].split('\\')[-1],
                '\\'.join(res[0].split('\\')[:-1]),
                res[1].replace(config.search_for, '<span>'+config.search_for+'</span>')
            ) for res in results
        ])
    try:
        with open('html/results.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        html_content = html_content.replace('[!table!]', table_rows)
        
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
            write_to_html()
        print(f"Done! result.html created and should open now in your browser.")
