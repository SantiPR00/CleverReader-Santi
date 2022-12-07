from tabula import read_pdf


def table_parser(file, numOfPages):
    tables = []
    for page in range(numOfPages):
        table = read_pdf(file, pages=page, multiple_tables=True)
        if table:
            tables.append(table)
    print("NUM OF TABLES IS " + str(len(tables)))
    for t in tables:
        print(t)
        print("===================================")
