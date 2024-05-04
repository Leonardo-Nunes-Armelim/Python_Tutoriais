from openpyxl import Workbook

# Cria um objeto de um Excel
work_book = Workbook()

# Pega a aba da planilha ativa
work_sheet = work_book.active

# Modo 1 de inserir valores no Excel (pela chave da celula)
work_sheet['A1'] = 'teste 1'

# Modo 2 de inserir valores no Excel (pela posição da celula)
work_sheet.cell(row=2, column=1, value='teste 2')

# Modo 3 de inserir valores no Excel (pelo objeto da celula)
cell = work_sheet['A3']
cell.value = 'teste 3'

# Modo 4 de inserir valores no Excel (atravéz de uma lista)
data = [[ 'Nome', 'Idade', 'Altura'],
        [  'Leo',      25,     1.75],
        ['Cesar',      18,     1.65],
        [ 'Davi',      50,     1.70],
        ['Carol',      26,     1.70]]

for row in data:
    work_sheet.append(row)

# Salvando o objeto em um arquivos excel
work_book.save('sample.xlsx')
