
import {test, expect} from "@playwright/test"

test("Pratice CSS and XPath", async({page}) => {
    await page.goto("https://the-internet.herokuapp.com/login")

    const username = page.locator("#username")
    const password = page.locator("//input[@id='password']")

    await username.fill("tomsmith")
    await password.fill("SuperSecretPassword!")

    await expect(username).toHaveValue("tomsmith")
    await expect(password).toHaveValue("SuperSecretPassword!")


})

//dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/playwright$ npx playwright test tests/xpath.spec.js