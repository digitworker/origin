from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, collect_list

class Products():
    products_data = None
    spark = None
    products_df = None
    product_category_df = None
    result_df = None
    
    # Генерируем объект SparkSession при создании класса 
    def __init__(self):
        self.spark = SparkSession.builder.appName("ProductCategory").getOrCreate()
    
    # Создаем таблицу
    def initTable(self,pd): 
        # Проверим, что данные имеют правильный формат
        try:
            if len(pd[0])!=2:
                raise Exception("Products data format is not correct!")
            for i in range(0, len(pd)):
                if len(pd[i])!=2:
                    raise Exception("Products data format is not correct!")
                elif not isinstance(pd[i][0],str):
                    raise Exception("Products data type is not correct!")
                elif not isinstance(pd[i][0],str) or not isinstance(pd[i][1],list):
                    raise Exception("Products data type is not correct!")
                        
                for j in range(0,len(pd[i][1])):
                    if not isinstance(pd[i][1][j],str):
                        raise Exception("Products data type is not correct!")
        except Exception:
            print("An exception occurred: Products data is not correct!")
        
        # Генерируем обьект для вывода таблицы на экран
        self.products_data = pd
        self.products_df = self.spark.createDataFrame(self.products_data, ["Product", "Categories"])
        self.product_category_df = self.products_df.select("Product", explode("Categories").alias("Category")).na.drop()
        self.result_df = self.products_df.select("Product").join(self.product_category_df, "Product", "left_outer")
    
    # Показываем таблицу
    def show(self):
        self.result_df.show()
    
    # Завершить работу SparkSession в ручную
    def finishSession(self):
        self.spark.stop()

    # Завершить работу SparkSession при уничтожении обьекта Products
    def __del__(self):
        self.spark.stop()