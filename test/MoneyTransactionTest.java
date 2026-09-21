import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.unittesting.Account;
import com.unittesting.MoneyTransactionService;


// sit up - and think about all possible inputs, 

public class MoneyTransactionTest {
	
	private static final String MONEY_AMOUNT_EXCEPTION_MSG = "Money amount shoud be greater than zero.";
	private static final String ACCOUNT_EXCEPTION_MSG =  "Accounts shouldn't be null";
	private static final double RANDOM_MONEY_AMOUNT = 100;
	private static final double ZERO_MONEY_AMOUNT = 0;
	private static final double MORE_THAN_RANDOM_AMOUNT = 200;
	private static final double NEGATIVE_MONEY_AMOUNT = -1;
	
	private MoneyTransactionService testInstance;
	
	@BeforeEach
	void setup() {
		testInstance = new MoneyTransactionService();
	}
	
	@AfterEach
	void tearDown() {
		//this method will be executed after each test method
	}
	
	@BeforeAll
	static void beforeAll() {
		// this method will be executed  before all tests
	}
	
	
	@Test
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
		var exception = assertThrows(IllegalArgumentException.class,() -> 
		testInstance.transferMoney(account1, account2, RANDOM_MONEY_AMOUNT));
		
		// THEN
		assertEquals(ACCOUNT_EXCEPTION_MSG,exception.getMessage());
	}
	
	@Test
	void shouldThrowExceptionWhenTransferNegativeAmount() {
		// GIVEN
		var account1 = new Account();
		var account2 = new Account();
		
		// when
		var exception = assertThrows(IllegalArgumentException.class, ()->
		testInstance.transferMoney(account1, account2, NEGATIVE_MONEY_AMOUNT));
		
		//then
		assertEquals(MONEY_AMOUNT_EXCEPTION_MSG, exception.getMessage());
	}
	
	
	
	}
