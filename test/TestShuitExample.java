import org.junit.jupiter.api.ClassOrderer.OrderAnnotation;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.junit.platform.runner.JUnitPlatform;
import org.junit.platform.suite.api.SelectClasses;
import org.junit.runner.RunWith;

@RunWith(JUnitPlatform.class)

//@SelectedPackages()

//@IncludeTags("production")

@SelectClasses(MoneyTransactionTest.class)


@Tag("production")
/*
 * There a different test method order implementation. They are: -DisplayName -MethodName -OrderAnnotation - Random
 * */

//@TestMethodOrder(OrderAnnotation.class)
public class TestShuitExample {
	
	@Test
	@Tag("production")
	void someTestForProdEnv() {
		
	}
	
}
