"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
let testerName = "Dhinesh";
let testCount = 10;
let isPassed = true;
function calculatePassPercentage(passed, total) {
    if (total == 0) {
        return 0;
    }
    return (passed / total) * 100;
}
console.log(testerName);
console.log(testCount);
console.log(isPassed);
console.log(calculatePassPercentage(8, 10));
// node tsc -> complie
// node src/variables.js -> run
// Dhinesh
// 10
// true
// 80
//# sourceMappingURL=variables.js.map