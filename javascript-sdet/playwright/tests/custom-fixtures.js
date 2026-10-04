import { test as base, expect } from "@playwright/test";

export const test = base.extend({
    loggedInPage: async ({ page }, use) => {
        await page.goto("https://the-internet.herokuapp.com/login");

        await page.getByLabel("Username").fill("tomsmith");
        await page.getByLabel("Password").fill("SuperSecretPassword!");
        await page.getByRole("button", { name: "Login" }).click();

        await expect(page).toHaveURL(/secure/);

        await use(page);
    }
});

export { expect };