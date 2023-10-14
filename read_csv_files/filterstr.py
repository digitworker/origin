import datetime
import re

class FilterStr():
    text = ''
    pattern_text = ''
    pattern = None
    def set_str(self, s: str):
        self.text = s
    def set_reg_expr(self, pattern):
        self.pattern_text = pattern
        
    def result(self):
        self.pattern = re.compile(self.pattern_text)
        m = self.pattern.match(self.text)
        
        if m:
            return True
        return False
        
class FilterDate(FilterStr):
    date_min = None
    date_max = None
    
    #Так как в Kaggle данных часто в полях содержатся даты, я решил сделать возможность фильтрации по дате (устаревший метод. Сейчас для простоты использую регулярные выражения, примененные к столбикам .csv файла) 
    def set_dates(self, date_min: datetime.date, date_max: datetime.date):
        self.date_min = date_min
        self.date_max = date_max
        
    def result(self):
        raw_dates_list = []
        #print ("self.text = ", self.text)
        if self.text:
            raw_dates_list = re.split(r"[^\d^\.]|[\s]", self.text) #разделитель это все кроме цифры и точки
            #print("raw_dates_list",raw_dates_list)
            #print("self.date_min",self.date_min)
            #print("self.date_max",self.date_max)
        if self.text and not(self.date_min==None) and not(self.date_max==None):
            #print("IN min max filtr")
            for d in raw_dates_list:
                if len(d)>=6:
                    #print("IN min max filtr")
                    #print("d",d)
                    date_dict = re.search(r"(?P<day>\d{2}).(?P<month>\d{2}).(?P<year>\d{4})",d)
                    if not(date_dict is None):
                        date_dict = date_dict.groupdict()
                        date = datetime.date(int(date_dict['year']),int(date_dict['month']),int(date_dict['day']))
                    #print("date", date)
                    if self.date_min > date or self.date_max < date:
                        #print("False")
                        return False
            return True      
        if self.text and not(self.date_min==None) and (self.date_max==None):
            #print("IN min max filtr")
            for d in raw_dates_list:
                if len(d)>=6:
                    #print("IN min max filtr")
                    #print("d",d)
                    date_dict = re.search(r"(?P<day>\d{2}).(?P<month>\d{2}).(?P<year>\d{4})",d)
                    if not(date_dict is None):
                        date_dict = date_dict.groupdict()
                        date = datetime.date(int(date_dict['year']),int(date_dict['month']),int(date_dict['day']))
                    #print("date", date)
                    if self.date_min > date:
                        #print("False")
                        return False
            return True      
        if self.text and (self.date_min==None) and not(self.date_max==None):
            #print("IN min max filtr")
            for d in raw_dates_list:
                if len(d)>=6:
                    #print("IN min max filtr")
                    #print("d",d)
                    date_dict = re.search(r"(?P<day>\d{2}).(?P<month>\d{2}).(?P<year>\d{4})",d)
                    if not(date_dict is None):
                        date_dict = date_dict.groupdict()
                        date = datetime.date(int(date_dict['year']),int(date_dict['month']),int(date_dict['day']))
                    #print("date", date)
                    if self.date_max < date:
                        #print("False")
                        return False
            return True      
        return False