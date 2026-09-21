package com.unittesting;

public class Account {
	private double moneyAmount;

	public double getMoneyAmount() {
		return moneyAmount;
	}

	public void setMoneyAmount(double moneyAmount) {
		this.moneyAmount = moneyAmount;
	}

	public Account(double moneyAmount) {
		super();
		this.moneyAmount = moneyAmount;
	}

	public Account() {
		super();
	}
	
	
}
