package com.automationTesting;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class ConditionalMethods {
	
	public static void main(String[] args) {
		
		WebDriver driver = new ChromeDriver();
		driver.get("https://demo.nopcommerce.com/register");
		driver.manage().window().maximize();
		
		// isDisplayed() - 
//		WebElement logo = driver.findElement(By.xpath("//img[@alt='nopcommerce dmoe's core']"));
//		boolean res = logo.isDisplayed();
//		System.out.println(res);
//		
		boolean status = driver.findElement(By.xpath("//img[@alt='nopcommerce demo store']")).isDisplayed();
		System.out.println("Displayed status: "+status);
		
		// isEnabled()
		boolean status1 = driver.findElement(By.xpath("//input[@id='FirstName']")).isEnabled();
		System.out.println("Enabled status: "+status1);
		
		// isSelected()
		WebElement male_rd = driver.findElement(By.xpath("//input[@id='gender-male']"));
		WebElement female_rd = driver.findElement(By.xpath("//input[@id='gender-female']"));
		boolean res1 = male_rd.isSelected();
		male_rd.click(); 
		System.out.println(res1);
		boolean res2 = female_rd.isSelected();
		System.out.println(res2);
		
	}
}
