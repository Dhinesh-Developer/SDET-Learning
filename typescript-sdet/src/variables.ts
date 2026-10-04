let testerName: string = "Dhinesh"
let testCount: number = 10
let isPassed: boolean = true

function calculatePassPercentage(
    passed: number,
    total: number,
): number {
    if(total == 0){
        return 0
    }
    return (passed / total) * 100
}

console.log(testerName)
console.log(testCount)
console.log(isPassed)
console.log(calculatePassPercentage(8,10))

// node tsc -> complie
// node src/variables.js -> run

// Dhinesh
// 10
// true
// 80