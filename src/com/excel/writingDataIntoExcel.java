package excel;

import java.io.FileOutputStream;
import java.io.IOException;

import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class writingDataIntoExcel {
	public static void main(String[] args) throws IOException {

		// if file present no problem or if file does not present then it will create
		// automatically
		FileOutputStream file = new FileOutputStream(System.getProperty("user.dir") + "\\testdata\\myfile.xlsx");
		// FileOutputStream file = new
		// FileOutputStream("\"/home/dhinesh/eclipse-workspace/SeleniumWebDriver/testdata/Myfile.xlsx\"");
		System.out.println(file);

		XSSFWorkbook workbook = new XSSFWorkbook();

		XSSFSheet sheet = workbook.createSheet("Data");
		XSSFRow row1 = sheet.createRow(0);
		row1.createCell(0).setCellValue("Java");
		row1.createCell(1).setCellValue(1234);
		row1.createCell(2).setCellValue("Automation");

		XSSFRow row2 = sheet.createRow(1);
		row2.createCell(0).setCellValue("Python");
		row2.createCell(1).setCellValue(5678);
		row2.createCell(2).setCellValue("PyTest");

		XSSFRow row3 = sheet.createRow(2);
		row3.createCell(0).setCellValue("Java Script");
		row3.createCell(1).setCellValue(8234);
		row3.createCell(2).setCellValue("Playwrite");

		workbook.write(file);

		workbook.close();
		file.close();

		System.out.println("File is created!!!");

	}
}
