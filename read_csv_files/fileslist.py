import os
import csv

def get_files_list(filedir: str, fileext: str):
    path = "./"
    dir_list = os.listdir(path) 
      
    print("Files and directories in '", path, "' :")
      
    # print the list 
    print(dir_list)
    csv_files = []

    for f in dir_list:             
        if f.split('.')[-1]==fileext:
            csv_files.append(f)
    return csv_files
    
def get_csv_head(csv_file_path: str):
    with open(csv_file_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        headers = []
        cols_number = 0
        line_count = 0
        for row in reader:
            if line_count == 0:
                return row

if __name__ == "__main__":
    fl_csv = get_files_list('./', 'csv')
    print("csv_files", fl_csv)
    for f in fl_csv:
        print("csv_head", get_csv_head('./'+f))