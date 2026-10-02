package testNG;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/*
TC1:
----
1. Login ---> @BeforeMethod
2. search ---> @Test
3. Logout ---> @AfterMethod
4. Login  
5. Adv search ---> @Test
6. Logout 

 * */

public class Annotations {
	
	@BeforeMethod
	void login() {
		System.out.println("This is Login...");
	}
	
	@Test(priority = 1)
	void search() {
		System.out.println("This is search...");
	}
	
	@Test(priority = 2)
	void advancedSearch() {
		System.out.println("advanced search...");
	}
	
	@AfterMethod
	void logout() {
		System.out.println("logout...");
	}
	
}
