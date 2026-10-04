import {test, expect} from "./custom-fixtures.js"

test("Verify authenticated page", async ({ loggedInPage }) => {
    await expect(loggedInPage.locater("h2"))
        .toHaveText("Secure Area")
})

