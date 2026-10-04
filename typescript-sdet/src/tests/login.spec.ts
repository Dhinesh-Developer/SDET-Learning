import {test, expect} from "@playwright/test"

interface Credentials{
    username: string
    password: string
}

const validUser: Credentials = {
    username: "tomsmith",
    password: " SuperSecretPassword!"
} 

test("Login using TypeScript", async ({ page }) =>{
    await page.goto("https://the-internet.herokuapp.com/login")

    await page.getByLabel("Username").fill(validUser.username)
    await page.getByLabel("Password").fill(validUser.password)
    await page.getByRole("button", {name: "Login"}).click()

    await expect(page).toHaveURL(/secure/)
    await expect(page.locator("h2")).toHaveText("Secure Area")

})


