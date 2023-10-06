from products import Products

# Пример использования класса Products:
if __name__ == "__main__":
    products_table = Products()
    products_data = [("Product1", ["Category1", "Category2"]),
                     ("Product2", ["Category2", "Category3"]),
                     ("Product3", ["Category1", "Category3"]),
                     ("Product4", []),
                     ("Product5", ["Category4"])]
    products_table.initTable(products_data)
    products_table.show()