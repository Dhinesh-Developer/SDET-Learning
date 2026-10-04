import {test, expect} from "@playwright/test"

test("Get a user", async ({ request })=>{
    const response = await request.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    expect(response.status()).toBe(200)

    const user = await response.json()

    expect(user.id).toBe(1)
    expect(user.name).toBeTruthy()
    expect(user.email).toContain("@")
})

// dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/playwright$ npx playwright test tests/api-get.spec.js

// Running 3 tests using 3 workers
//   3 passed (867ms)

// To open last HTML report run:

//   npx playwright show-report

// dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/playwright$ npx playwright show-report

//   Serving HTML report at http://localhost:9323. Press Ctrl+C toquit.
// ^C