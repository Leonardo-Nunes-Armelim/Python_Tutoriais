from openpyxl import Workbook

# Cria um objeto de um Excel
work_book = Workbook()

# Salvando o objeto em um arquivos excel
work_book.save("sample.xlsx")
