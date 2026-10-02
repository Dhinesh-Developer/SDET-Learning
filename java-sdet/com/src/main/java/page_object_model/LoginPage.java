package page_object_model;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage {

	WebDriver driver;

	// constructor
	LoginPage(WebDriver driver) {
		this.driver = driver;
	}

	// Locaters means -> By loc = By.xpath("//input[@placeholder='Username']");
	By txt_username_loc = By.xpath("//input[@placeholder='username']");
	By txt_password_loc = By.xpath("//input[@placeholder='password']");
	By btn_login_loc = By.xpath("//button[normalize-space()='Login']");

	// action methods
	public void setUserName(String user) {
		driver.findElement(txt_username_loc).sendKeys(user);
	}
	
	public void setPassword(String password) {
		driver.findElement(txt_password_loc).sendKeys(password);
	}
	
	public void clickLogin() {
		driver.findElement(btn_login_loc).click();
	}
	
}
