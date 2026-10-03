import { test, expect } from "@playwright/test";

test("Verify page elements", async ({ page }) => {
    await page.goto("https://the-internet.herokuapp.com/login");

    const username = page.getByRole("textbox", {
        name: "Username"
    });

    const password = page.getByRole("textbox", {
        name: "Password"
    });

    const loginButton = page.getByRole("button", {
        name: "Login"
    });

    await expect(username).toBeVisible();
    await expect(password).toBeVisible();
    await expect(loginButton).toBeEnabled();
});