
export default function login(username,password){
    if(username === "admin" && password === "admin123"){
        return "Login successful"
    }
    return "Login failed!!"
}
