import pytest
from products import Products

class TestProducts:

    products = Products()

    def testProductsClass(self):
        # Проверка правильности созданных Spark объектов
        products_data = [("Product1", ["Category1", "Category2"]),
                     ("Product2", ["Category2", "Category3"]),
                     ("Product3", ["Category1", "Category3"]),
                     ("Product4", []),
                     ("Product5", ["Category4"])]
        self.products.initTable(products_data)
        assert self.products.spark.__class__.__name__ == 'SparkSession'
        assert self.products.products_df.__class__.__name__ == 'DataFrame'
        assert self.products.product_category_df.__class__.__name__ == 'DataFrame'

        # Проверка реакции на неправильные входные данные
        products_data = [("Product1", ["Category1", "Category2"],["AnotherData"]),
                     ("Product2", ["Category2", "Category3"]),
                     ("Product3", ["Category1", "Category3"]),
                     ("Product4", []),
                     ("Product5", ["Category4"])]
        with pytest.raises(Exception):
            assert self.products.initTable(products_data)
        products_data = [("Product1", ["Category1", "Category2"]),
                     ("Product2", ["Category2", 5]),
                     ("Product3", ["Category1", "Category3"]),
                     ("Product4", []),
                     ("Product5", ["Category4"])]
        with pytest.raises(Exception):
            assert self.products.initTable(products_data)
        products_data = [(5, ["Category1", "Category2"]),
                     ("Product2", ["Category2", "Category3"]),
                     ("Product3", ["Category1", "Category3"]),
                     ("Product4", []),
                     ("Product5", ["Category4"])]
        with pytest.raises(Exception):
            assert self.products.initTable(products_data)
        