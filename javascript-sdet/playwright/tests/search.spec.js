import {test, expect} from "@playwright/test"

test("Search for a product", async ({page}) => {
    await page.goto("https://demo.opencart.com/")

    const searchBox = page.getByRole("textbox", {
        name: "Search"
    })

    await searchBox.fill("MacBook")
    await searchBox.press("Enter")

    await except(page).toHaveURL(/route=product\/search/)
    await except(page.locator("body")).toContainText("MacBook")
})



