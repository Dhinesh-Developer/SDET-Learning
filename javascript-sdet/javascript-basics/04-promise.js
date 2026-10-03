
const loginCheck = new Promise((resolve,reject) => {
    const loginSuccessful = true

    if(loginSuccessful){
        console.log("Login successful")
    }else{
        reject(new Error("Invalid credentials"))
    }
});

loginCheck.then(res => console.log(res)).catch(err => console.log(err.message))

// dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/javascript-basics$ node promise.js
// Login successful