package seleniumWebDriver.demo;

import org.jspecify.annotations.Nullable;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

/*
Test case
---------

1. Launch browser (chrome)
2. Open URL https://demo.opencart.com/
3. Validate title should be "Your Store"
4. Close browser

 * */

public class FirstTestCase {

	public static void main(String[] args) {

		WebDriver driver = new ChromeDriver();

		try {
			driver.get("https://www.google.com/");

			String actualTitle = driver.getTitle();
			String expectedTitle = "Google";

			if (actualTitle.equals(expectedTitle)) {
				System.out.println("Test Passed");
			} else {
				System.out.println("Test Failed");
				System.out.println("Expected: " + expectedTitle);
				System.out.println("Actual: " + actualTitle);
			}
		} finally {
			driver.quit();
		}
	}
}
