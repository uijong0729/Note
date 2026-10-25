from pathlib import Path

from openpyxl import Workbook


output_path = Path(__file__).with_name("newfile.xlsx")

workbook = Workbook()
workbook.save(output_path)

print(f"만들었습니다: {output_path}")