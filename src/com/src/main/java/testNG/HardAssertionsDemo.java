package testNG;

import org.testng.Assert;
import org.testng.annotations.Test;

public class HardAssertionsDemo {
	
	@Test
	void test() {
//		Assert.assertEquals("xyz", "xyz");
//		Assert.assertEquals(1, 1);
		Assert.assertTrue(true); // pass
		Assert.assertTrue(false); // fail
		Assert.assertNotEquals("abs", null);
	}
}




