# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tests/login.spec.ts >> Login using TypeScript
- Location: tests/login.spec.ts:13:5

# Error details

```
Test timeout of 30000ms exceeded.
```

```
Error: locator.fill: Test timeout of 30000ms exceeded.
Call log:
  - waiting for getByLabel('Username')

```

# Page snapshot

```yaml
- iframe [ref=e2]:
  - generic [ref=f1e1]:
    - generic [ref=f1e2]:
      - generic [ref=f1e5]: Application error
      - paragraph [ref=f1e6]:
        - text: An error occurred in the application and your page could not be served. If you are the application owner,
        - link "check your logs for details" [ref=f1e7] [cursor=pointer]:
          - /url: https://devcenter.heroku.com/articles/logging#view-logs?utm_source=error-pages&utm_content=application-error
        - text: . You can do this from the Heroku CLI with the command
        - code [ref=f1e8]: heroku logs --tail
    - link [ref=f1e15] [cursor=pointer]:
      - /url: https://devcenter.heroku.com/articles/logging#view-logs?utm_source=error-pages&utm_content=application-error
```

# Test source

```ts
  1  | import {test, expect} from "@playwright/test"
  2  | 
  3  | interface Credentials{
  4  |     username: string
  5  |     password: string
  6  | }
  7  | 
  8  | const validUser: Credentials = {
  9  |     username: "tomsmith",
  10 |     password: " SuperSecretPassword!"
  11 | } 
  12 | 
  13 | test("Login using TypeScript", async ({ page }) =>{
  14 |     await page.goto("https://the-internet.herokuapp.com/login")
  15 | 
> 16 |     await page.getByLabel("Username").fill(validUser.username)
     |                                       ^ Error: locator.fill: Test timeout of 30000ms exceeded.
  17 |     await page.getByLabel("Password").fill(validUser.password)
  18 |     await page.getByRole("button", {name: "Login"}).click()
  19 | 
  20 |     await expect(page).toHaveURL(/secure/)
  21 |     await expect(page.locator("h2")).toHaveText("Secure Area")
  22 | 
  23 | })
  24 | 
  25 | 
  26 | 
```