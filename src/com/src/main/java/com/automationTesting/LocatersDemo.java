package com.automationTesting;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class LocatersDemo {
	public static void main(String[] args) {
		
		WebDriver driver = new ChromeDriver();
		
		// www will not work, only https will work
		driver.get("https://www.automationexercise.com/");
		
	/*
	 	// name
		WebElement searchBox = driver.findElement(By.name("search"));
		
		searchBox.sendKeys("Tshirt");
		
		// id
		WebElement id = driver.findElement(By.id("sale_image"));
		boolean res = id.isDisplayed();
		System.out.println("Displayed status: "+res);
	 * */
		
		// LinkText and partialLinkText --- only for link
		
//		driver.findElement(By.partialLinkText("Products")).click();
//		driver.findElement(By.linkText("Products")).click(); // preferable
//		
		// TagName and ClassName -> group of element
		// find the number of links in the header	
		// group of elements -> then uses findElements() -> s is added
		// className
		List<WebElement> elements = driver.findElements(By.className("header-middle"));
		System.out.println(elements.size());
		
		// find total no of link in one page
		// tagName
		List<WebElement> elements2 = driver.findElements(By.tagName("a"));
		System.out.println(elements2.size());
		
		
		// find the total no. of images
		List<WebElement> elements3 = driver.findElements(By.tagName("img"));
		System.out.println(elements3.size());
		
		driver.close();
	}
}
