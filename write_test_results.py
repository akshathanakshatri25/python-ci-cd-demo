import pytest
import openpyxl

def run_tests():
    # Run pytest programmatically and capture results
    # returns exit code (0 = all passed)
    result = pytest.main(["--maxfail=5", "--disable-warnings", "--tb=short"])
    return result

def write_result_to_excel(result):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Test Results"
    
    sheet.append(["Test Name", "Status"])
    
    # For demo: we only have one test
    status = "PASSED" if result == 0 else "FAILED"
    sheet.append(["test_add", status])
    
    wb.save("test_results.xlsx")

if __name__ == "__main__":
    test_result = run_tests()
    write_result_to_excel(test_result)
