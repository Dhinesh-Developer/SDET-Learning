package com.automationTesting;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class cssLocaters {
	public static void main(String[] args) {
		
		WebDriver driver = new ChromeDriver();
		driver.get("https://www.automationexercise.com/products");
		
		// maximize the browser window
		driver.manage().window().maximize();
		
		// tag#value of id
//		driver.findElement(By.cssSelector("input#search_product")).sendKeys("Men Tshirt");
		
		// tag class  tag.classname  [form-control input-lg] // className => first part is ok, second part not mandatory
		//driver.findElement(By.cssSelector("input.form-control")).sendKeys("Men Tshirt");
		
		// tag attribute
		//driver.findElement(By.cssSelector("input[Placeholder='Search Product']")).sendKeys("T-Shirts");
		
		// tag class attribute  [] square brackets means attribute
		driver.findElement(By.cssSelector("input.search-box-text[name='q']")).sendKeys("T-shirts");
		
		
	}
}
