package com.unittesting;

public class MoneyTransactionService {
	public boolean transferMoney(Account accountFrom,Account accountTo,double moneyAmountToSend) {
		
		if(accountFrom == null || accountTo == null) {
			throw new IllegalArgumentException("Accounts shouldn't be null");
		}
		if(moneyAmountToSend <= 0) {
			throw new IllegalArgumentException("Money amount should be greater than zero.");
		}
		
		if (accountFrom.getMoneyAmount() < moneyAmountToSend) {
			throw new IllegalArgumentException("Insufficient balance");
		}
		
		accountFrom.setMoneyAmount(accountFrom.getMoneyAmount() - moneyAmountToSend);
		accountTo.setMoneyAmount(accountTo.getMoneyAmount() + moneyAmountToSend);
		
		return true;
		
	}
}
