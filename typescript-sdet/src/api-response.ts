interface ApiResponse<T>{
    status: number
    data: T
}

interface Product{
    id:number
    name:string
    price:number
}

class ProductValidator{
    validate(response: ApiResponse<Product>):boolean {
        return(
            response.status === 200 &&
            response.data.id > 0 &&
            response.data.price >= 0
        )
    }
}

const response: ApiResponse<Product> = {
    status: 200,
    data : {
        id: 101,
        name: "Laptop",
        price: 55000
    }
}

const validator = new ProductValidator()
console.log(validator.validate(response))

// dhinesh@Arise:~/eclipse-workspace/SDET/typescript-sdet$ npx tsc
// dhinesh@Arise:~/eclipse-workspace/SDET/typescript-sdet$ node src/api-response.ts
// true