"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class ProductValidator {
    validate(response) {
        return (response.status === 200 &&
            response.data.id > 0 &&
            response.data.price >= 0);
    }
}
const response = {
    status: 200,
    data: {
        id: 101,
        name: "Laptop",
        price: 55000
    }
};
const validator = new ProductValidator();
console.log(validator.validate(response));
//# sourceMappingURL=api-response.js.map