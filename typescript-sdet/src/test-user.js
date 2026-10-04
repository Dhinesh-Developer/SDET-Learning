"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const user = {
    id: 1,
    username: "dhinesh",
    email: "dhinesh@example.com",
    active: true,
    role: "tester"
};
function displayUser(user) {
    console.log(user.username);
    console.log(user.email);
    console.log(user.active);
}
displayUser(user);
// dhinesh@Arise:~/eclipse-workspace/SDET/typescript-sdet$ npx tsc
// dhinesh@Arise:~/eclipse-workspace/SDET/typescript-sdet$ node src/test-user.ts
// dhinesh
// dhinesh@example.com
// true
//# sourceMappingURL=test-user.js.map