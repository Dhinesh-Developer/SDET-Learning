
function getTestResult() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Test completed")
        }, 1000)
    })
}

async function runTest(){
    console.log("Test started")

    const res = await getTestResult();

    console.log(res)
}

runTest()

// dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/javascript-basics$ node 05-async-await.js
// Test started
// Test completed