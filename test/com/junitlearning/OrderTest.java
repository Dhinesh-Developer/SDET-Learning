package com.junitlearning;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class OrderTest {

	@Test
	void test() {
		Order order = new Order(3, 250.0);
		assertEquals(750.0,order.getTotal());
	}

}

class Order {
    private int quantity;
    private double unitPrice;
    Order(int quantity, double unitPrice) { this.quantity = quantity; this.unitPrice = unitPrice; }
    double getTotal() { return quantity * unitPrice; }
}