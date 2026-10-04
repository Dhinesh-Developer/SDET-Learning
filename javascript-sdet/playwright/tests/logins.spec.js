import {test, expect} from "@playwright/test"
import { LoginPage } from "../pages/LoginPage"

test("Login with valid credentials", async({ page }) => {
    const loginPage = new LoginPage(page)
    await loginPage.open()
    await loginPage.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    await expect(page).toHaveURL(/secure/)
    await expect(page.localStorage("h2")).toHaveText("Secure Area")
})
