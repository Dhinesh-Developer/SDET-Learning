import {test ,expect} from "@playwright/test"

test("Create a post", async ({ request }) => {
    const response = await request.post(
        "https://jsonplaceholder.typicode.com/posts",
        {
            data : {
                title: "Playwright Testing",
                body: "Learning API automation",
                userId: 1
            }
        }
    )

    expect(response.status()).toBe(201)
    const res = await response.json()

    expect(res.title).toBe("Playwright Testing")
    expect(res.body).toBe("Learning API automation")
    expect(res.userId).toBe(1)
})


// dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/playwright$ npx playwright test tests/api-post.spec.js

// Running 3 tests using 3 workers
//   3 passed (1.6s)

// To open last HTML report run:

//   npx playwright show-report
