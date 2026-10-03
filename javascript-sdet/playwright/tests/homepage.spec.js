
import { test, expect } from "@playwright/test";

test("Verify OpenCart homepage", async ({ page }) => {
    await page.goto("https://demo.opencart.com/");

    await expect(page).toHaveTitle(/Your Store/);
});