package com.junitlearning;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class BankAccountTest {

	@Test
	void test() {
		BankAccount account = new BankAccount("ACC123");
		assertEquals(0.0, account.getBalance());
	}

}

class BankAccount {
    private String accountNumber;
    private double balance = 0.0;
    BankAccount(String accountNumber) { this.accountNumber = accountNumber; }
    double getBalance() { return balance; }
}