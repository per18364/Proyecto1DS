import pandas as pd

read_file = pd.read_excel(r"C:\Users\javie\Desktop\U\2023s\data-science\Proyecto1DS\establecimientoav.xlsx")
read_file.to_csv(r"C:\Users\javie\Desktop\U\2023s\data-science\Proyecto1DS\establecimientoavcsv.csv", index = None, header=True)