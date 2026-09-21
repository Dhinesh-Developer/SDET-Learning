import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import com.unittesting.Calculator;

class CalculatorTest {

	@Test
	void test() {
		var calculator = new Calculator();
		int actual = calculator.add(2, 3);
		assertEquals(5, actual);
		
		
	}

}
