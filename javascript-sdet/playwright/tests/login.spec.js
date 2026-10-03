import {test, expect} from "@playwright/test"

test("Verify login form" ,async ({page}) => {
    await page.goto("https://the-internet.herokuapp.com/login")
    await page.getByLabel("Username").fill("kumar")
    await page.getByLabel("Password").fill("SuperSecretPassword!")
    await page.getByRole("button", {name: "Login"}).click()

    await expect(page.locator("#flash"))
        .toContainText("You logged into a secure area!")

})


