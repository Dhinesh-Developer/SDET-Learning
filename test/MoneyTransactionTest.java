import static org.junit.Assert.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTimeout;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.time.Duration;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.DisplayNameGenerator;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Timeout;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.EmptySource;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.NullAndEmptySource;
import org.junit.jupiter.params.provider.NullSource;
import org.junit.jupiter.params.provider.ValueSource;

import com.unittesting.Account;
import com.unittesting.MoneyTransactionService;

// sit up - and think about all possible inputs, 

@DisplayName("Money Transaction service test")
@DisplayNameGeneration(DisplayNameGenerator.ReplaceUnderscores.class)

public class MoneyTransactionTest {

	private static final String MONEY_AMOUNT_EXCEPTION_MSG = "Money amount shoud be greater than zero.";
	private static final String ACCOUNT_EXCEPTION_MSG = "Accounts shouldn't be null";
	private static final double RANDOM_MONEY_AMOUNT = 100;
	private static final double ZERO_MONEY_AMOUNT = 0;
	private static final double MORE_THAN_RANDOM_AMOUNT = 200;
	private static final double NEGATIVE_MONEY_AMOUNT = -1;
	private static final String IS_KUMAR_LAPTOP = "KUMAR";

	private MoneyTransactionService testInstance;

	@BeforeEach
	void setup() {
		testInstance = new MoneyTransactionService();
	}

	@AfterEach
	void tearDown() {
		// this method will be executed after each test method
	}

	@BeforeAll
	static void beforeAll() {
		// this method will be executed before all tests
	}

	@Test
	@DisplayName("verfify money transaction from one account to another")
	void shouldTransferMoneyFromOneAccountToAnother() {
		// Given
		var account1 = new Account(RANDOM_MONEY_AMOUNT);
		var account2 = new Account(ZERO_MONEY_AMOUNT);

		// when
		testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT);

		// then
		assertEquals(ZERO_MONEY_AMOUNT, account1.getMoneyAmount());
		assertEquals(RANDOM_MONEY_AMOUNT, account2.getMoneyAmount());

	}

	@Test
	void shouldThrowExceptionIfAccountFromIsNull() {
		// GIVEN
		Account account1 = null;
		Account account2 = new Account(RANDOM_MONEY_AMOUNT);

		// WHEN
		var exception = assertThrows(IllegalArgumentException.class,
				() -> testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT));

		// THEN
		assertEquals(ACCOUNT_EXCEPTION_MSG, exception.getMessage());
	}

	@Test
	void shouldThrowExceptionWhenTransferNegativeAmount() {
		// GIVEN
		var account1 = new Account();
		var account2 = new Account();

		// when
		var exception = assertThrows(IllegalArgumentException.class,
				() -> testInstance.transferMoney(account1, account2, NEGATIVE_MONEY_AMOUNT));

		// then
		assertEquals(MONEY_AMOUNT_EXCEPTION_MSG, exception.getMessage());
	}

	@Test
	void groupedAssertionsExample() {
		// In a grouped assertion all assertions are executed, and all failures will be
		// reported together

		// GIVEN
		var account1 = new Account(RANDOM_MONEY_AMOUNT);
		var account2 = new Account(ZERO_MONEY_AMOUNT);

		// WHEN
		testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT);

		// THEN
		assertAll("Money transaction", () -> assertEquals(ZERO_MONEY_AMOUNT, account1.getMoneyAmount()),
				() -> assertEquals(RANDOM_MONEY_AMOUNT, account2.getMoneyAmount()));

	}

	@Test
	void dependentAssertionsExample() {
		// within a code block, if an assertion fails the subsequent code in the same
		// block will be skipped.

		// GIVEN
		var account1 = new Account(RANDOM_MONEY_AMOUNT);
		var account2 = new Account(ZERO_MONEY_AMOUNT);

		assertAll("Mone transaction", () -> {
			// WHEN
			boolean isTransactionSucced = testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT);
			assertTrue(isTransactionSucced);

			// Executed only if the previous assertion is valid.
			assertAll("Money amount is changed on eht accounts",
					() -> assertEquals(ZERO_MONEY_AMOUNT, account1.getMoneyAmount()),
					() -> assertEquals(RANDOM_MONEY_AMOUNT, account2.getMoneyAmount()));
		});
	}

	@Test
	void testWithTimeoutExample() {
		// GIVEN
		var account1 = new Account(RANDOM_MONEY_AMOUNT);
		var account2 = new Account(ZERO_MONEY_AMOUNT);

		assertTimeout(Duration.ofSeconds(1), () -> {
			testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT);
		});
	}

	@Test
	@Timeout(2)
	void timeoutNotExceededWithResults() {
		// GIVEN
		var account1 = new Account(RANDOM_MONEY_AMOUNT);
		var account2 = new Account(ZERO_MONEY_AMOUNT);

		// the following assertion succeeds, and returns the supplied object.
		boolean actualResults = assertTimeout(Duration.ofSeconds(1), () -> {
			return testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT);
		});

		assertTrue(actualResults);
	}

	@Test
	void testOnlyOnWorkStation() {
		assumeTrue("true".equals(System.getenv(IS_KUMAR_LAPTOP)),
				() -> "Aborting this test, because it is running not on laptop of kumar");

		// GIVEN
		var account1 = new Account(RANDOM_MONEY_AMOUNT);
		var account2 = new Account(ZERO_MONEY_AMOUNT);

		// the following assertion succeeds, and returns the supplied object.
		boolean actualResults = assertTimeout(Duration.ofSeconds(1), () -> {
			return testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT);
		});

		assertTrue(actualResults);
	}

	@ParameterizedTest
	@ValueSource(ints = { 100, 200, 50, -10 })
	void parameterizedTestExample(int moneyAmount) {
		assumeTrue(moneyAmount > 0, () -> "Money amount can't be negative");
		Account account1 = new Account(moneyAmount);
		Account account2 = new Account(ZERO_MONEY_AMOUNT);

		assertTrue(testInstance.transferMoney(account1, account2, moneyAmount));

	}
	
	@ParameterizedTest
	@NullSource
	@EmptySource
	@NullAndEmptySource
	void nullAndEmptySources(String text) {
		assertTrue(text == null || text.trim().isEmpty());
	}
	
	@ParameterizedTest
	@MethodSource("sourceMethod")
	@Disabled
	void testMethodSource(String arg) {
		assertNotNull(arg);
	}
	
	@ParameterizedTest
	@CsvSource({
		"Apple, 1",
		"banana, 2",
		"'lemon, lime', 0xF1"
	})
	void testWithCsvScource(String fruit,int rank) {
		assertNotNull(fruit);
		assertNotEquals(0, rank);
	}
	
	
	
	
	

}
