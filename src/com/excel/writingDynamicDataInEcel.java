package excel;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class writingDynamicDataInEcel {
	public static void main(String[] args) throws IOException {
		// if file present no problem or if file does not present then it will create
		// automatically
		FileOutputStream file = new FileOutputStream(
				System.getProperty("user.dir") + "\\testdata\\myfile_dynamic.xlsx");
		// FileOutputStream file = new
		// FileOutputStream("\"/home/dhinesh/eclipse-workspace/SeleniumWebDriver/testdata/Myfile.xlsx\"");
		System.out.println(file);

		XSSFWorkbook workbook = new XSSFWorkbook();

		XSSFSheet sheet = workbook.createSheet("Data");

		Scanner in = new Scanner(System.in);
		System.out.println("Enter how many rows: ");
		int rows = in.nextInt();

		System.out.println("Enter how many cell in each rows: ");
		int noOfCells = in.nextInt();

		for (int i = 0; i < rows; i++) {
			XSSFRow currentRow = sheet.createRow(i);
			for (int j = 0; j < noOfCells; j++) {
				XSSFCell cell = currentRow.createCell(j);
				cell.setCellValue(in.next());
			}
		}
		
		
		workbook.write(file); // attach workbook to the file
		workbook.close();
		file.close();

		System.out.println("File is created!!!");
		in.close();
	}
}
