import openpyxl

def write_result(test_name, status):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Test Results"

    sheet.append(["Test Name", "Status"])
    sheet.append([test_name, status])

    wb.save("test_results.xlsx")

if __name__ == "__main__":
    write_result("test_add", "PASSED")
