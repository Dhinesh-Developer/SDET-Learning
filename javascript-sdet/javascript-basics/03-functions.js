const users = [
    {name: "Dhinesh", age: 20, active: true},
    {name: "Arun", age:22, active: false},
    {name: "kumar", age:21, active: true}
]

const activeUsers = users.filter(user => user.active)
const names = activeUsers.map(user => user.name)

console.lof(names);