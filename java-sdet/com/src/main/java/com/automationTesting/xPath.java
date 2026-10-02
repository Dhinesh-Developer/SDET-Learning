package com.automationTesting;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class xPath {
	
	public static void main(String[] args) {
		
		WebDriver driver = new ChromeDriver();
		driver.get("https://demo.opencart.com/");
		driver.manage().window().maximize();
		
		// Xpath with sigle attribute
		driver.findElement(By.xpath("//input@placeholder='Search'")).sendKeys("T-shirt");
		
		// xpath with multiple attributes
		driver.findElement(By.xpath("//input[@name='search'][@placeholder='search']")).sendKeys("T-shirt");
		
		driver.close();
		
	}
}
