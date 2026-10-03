
async function fetchUser() {
    try{
        const res = await fetch(
            "https://jsonplaceholder.typicode.com/users/1"
        )

        if(!res.ok){
            throw new Error(`HTTP error: ${response.status}`);
        }

        const user = await res.json()
    }catch(err){
        console.error("Request failed: ",err.message)
    }
}

fetchUser()
