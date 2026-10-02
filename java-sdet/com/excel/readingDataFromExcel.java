package excel;

import java.io.FileInputStream;
import java.io.IOException;

import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

//Excel File : ----> workbook ----> Sheets ----> Rows ------> Cells
//Excel sheet -> right click ->  properties -> location ->  copy paste

public class readingDataFromExcel {

	public static void main(String[] args) throws IOException {

		FileInputStream file = new FileInputStream(
				"/home/dhinesh/eclipse-workspace/SeleniumWebDriver/testdata/Book_Purchases_Sample.xlsx");
		// or for dynamic -- user.dir means current working project
		// FileInputStream file = new
		// FileInputStream(System.getProperty("user.dir")+"/testdata/Book_Purchases_Sample.xlsx");

		XSSFWorkbook workbook = new XSSFWorkbook(file);

		XSSFSheet sheet = workbook.getSheet("Book Purchases");
		// or
		// here we passing the index of the sheet
//		XSSFSheet sheet = workbook.getSheetAt(0);

		int totalRows = sheet.getLastRowNum();
		int totalCells = sheet.getRow(1).getLastCellNum();

		System.out.println("Number of rows: " + totalRows);
		System.out.println("Number of cells: " + totalCells);

		// row and column for reading the data from the excel
		for (int i = 0; i < totalRows; i++) {
			XSSFRow currentRow = sheet.getRow(i);
			for (int j = 0; j < totalCells; j++) {
				String cellValue = currentRow.getCell(j).toString();
				System.out.print(cellValue + " | ");
			}
			System.out.println();
		}

		workbook.close();
		file.close();
	}

}

/*
 * Number of rows: 5 Number of cells: 4 BookName | PurchasedDate | Amount |
 * Location | Atomic Habits | 2026-09-01 | 499.0 | Chennai | The Alchemist |
 * 2026-09-05 | 299.0 | Salem | Clean Code | 2026-09-10 | 850.0 | Bengaluru |
 * Deep Work | 2026-09-15 | 399.0 | Coimbatore |
 */
