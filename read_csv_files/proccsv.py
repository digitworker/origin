import csv
from tabulate import tabulate
import operator
from filterstr import FilterStr,FilterDate
from typing_extensions import Annotated
from typing import Union

class ProcCSV():
    result_table = []
    table_headers = []
    csv_reader = None
    filters = []
    flrt_col = 0
    
    def add_filter(self, reg_expr: str, fltr_col: int):
        f = FilterStr()
        f.set_reg_expr(reg_expr)
        self.filters.append([f, fltr_col])
    '''
    def remove_filters(self):
        self.filters = []
        
    def pop_filter(self):
        self.filters.pop()
        
    def get_filters(self):
        return self.filters
    '''    
    def process_csv(self, csv_file_path, filtered: bool = False, start: int = None, end: int = None):
        reader = None
        if start:
            if start < 0: start = None
            if start > 0: start = int(start)
        if end:
            if end < 0: end = None
            if end > 0: end = int(end)
        #if filtered:
        #    print("filter is on")
        
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            line_count = -1
            headers = []
            table_csv = []
            cols_number = 0
            for row in reader:
                next_row = False 
                if end and (line_count == end): 
                    break
                line_count += 1
                if line_count > 0 and line_count < start: 
                    #print("skip line index ", line_count)
                    continue
                if line_count == 0:
                    table_csv.append(row)
                    #print(f'Column names are {", ".join(row)}')
                    self.table_headers = row
                    #print("self.table_headers",self.table_headers)
                    cols_number = len(row)
                    if filtered:
                        for c_n in self.filters:
                            if c_n[1]>cols_number-1:
                                #? throw Exception("Exception: Filtering index ("+filters[c_n][1]+") out of range for file: "+csv_file_path)
                                return False
                else:
                    if filtered:
                        for f in self.filters:
                            f[0].set_str(row[f[1]])
                            if not f[0].result():
                                next_row = True
                                break
                        if next_row:
                            #print("next_row")
                            continue
                        table_csv.append(row)
                        #print("added")
                    else:
                        table_csv.append(row)

            #print("ended on line count ", line_count)  
            if len(table_csv)>0:
                print("Updating_result_table...")
                self.result_table = table_csv
                print("OK.")
                return True
            return False
                
    def get_result_table(self):
        return self.result_table
        
    def show_result_table(self, sort_col: int = None, reverse: bool = None):
        if reverse and sort_col:
            self.result_table = sorted(self.result_table,key=operator.itemgetter(sort_col), reverse=True)
        elif sort_col: 
            self.result_table = sorted(self.result_table,key=operator.itemgetter(sort_col))  
        print(tabulate(self.result_table[1:100], headers=self.table_headers))
        
if __name__=="__main__":
    pcsv = ProcCSV()
    pcsv.add_filter("\d{2}.\d{2}.201[6-6]",0)
    pcsv.add_filter("^\d+\.\d+$",2)
    if pcsv.process_csv('D:/FastAPIserver/uploads/jena_climate_2009_2016.csv', filtered = False, start = 5, end = 400000):
        pcsv.show_result_table(sort_col = 1, reverse = False)
    