class TestDataError extends Error{
    constructor(message){
        super(message)
        this.name = "TestDataError"
    }
}

function validateUser(user){
    try{
        if (!user.username){
            throw new TestDataError("Username is missing")
        }
        console.log("User data is valid")
    }catch(error){
        console.error(error.name, error.message)
    }finally{
        console.log("Validation completed")
    }

}

validateUser({ username:"kumar"})

// dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/javascript-basics$ node 07-custom-error.js
// TestDataError Username is missing
// Validation completed
// dhinesh@Arise:~/eclipse-workspace/SDET/javascript-sdet/javascript-basics$ node 07-custom-error.js
// User data is valid
// Validation completed
