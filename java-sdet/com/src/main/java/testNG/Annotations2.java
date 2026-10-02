package testNG;

import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

/*

TC2:
----
1. Login ---> @BeforeClass
2. search ---> @Test
3. Adv search ---> @Test 
4. Logout ---> AfterClass

 * */

public class Annotations2 {
	@BeforeClass
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
	
	@AfterClass
	void logout() {
		System.out.println("logout...");
	}
}
