package com.junitlearning;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ProductTest {

	@Test
	void test() {
		Product product = new Product("Laptop", 55000.0);
		assertEquals(55000.0,product.getPrice());
	}
	
//	@Test
//	void productShouldBEInStockByDefault() {
//		Product p = new Product("Mouse",500.0);
//		assertTrue(p.isInStock());
//	}

}

class Product{
	private String name;
	private double price;
	public Product(String name, double price) {
		super();
		this.name = name;
		this.price = price;
	}
	public Product() {
		super();
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	
	
}