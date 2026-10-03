
from flask import Flask, jsonify, request
from database import init_db, get_connection

app = Flask(__name__)
init_db()


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.post("/users")
def create_user():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(error="JSON object required"), 400

    name = data.get("name")
    email = data.get("email")

    if not isinstance(name, str) or not name.strip():
        return jsonify(error="Name is required"), 400

    if not isinstance(email, str) or "@" not in email:
        return jsonify(error="Valid email is required"), 400

    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name.strip(), email.strip())
            )
            user_id = cursor.lastrowid
    except Exception:
        return jsonify(error="Email already exists"), 409

    return jsonify(
        id=user_id,
        name=name.strip(),
        email=email.strip()
    ), 201


@app.get("/users/<int:user_id>")
def get_user(user_id):
    with get_connection() as conn:
        user = conn.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()

    if user is None:
        return jsonify(error="User not found"), 404

    return jsonify(dict(user)), 200


@app.put("/users/<int:user_id>")
def update_user(user_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(error="JSON object required"), 400

    name = data.get("name")
    email = data.get("email")

    if not isinstance(name, str) or not name.strip():
        return jsonify(error="Name is required"), 400

    if not isinstance(email, str) or "@" not in email:
        return jsonify(error="Valid email is required"), 400

    with get_connection() as conn:
        user = conn.execute(
            "SELECT id FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()

        if user is None:
            return jsonify(error="User not found"), 404

        try:
            conn.execute(
                "UPDATE users SET name = ?, email = ? WHERE id = ?",
                (name.strip(), email.strip(), user_id)
            )
        except Exception:
            return jsonify(error="Email already exists"), 409

    return jsonify(
        id=user_id,
        name=name.strip(),
        email=email.strip()
    ), 200


@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        if cursor.rowcount == 0:
            return jsonify(error="User not found"), 404

    return jsonify(message="User deleted"), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ cd project1
# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/project1$ curl -i http://127.0.0.1:5000/health
# HTTP/1.1 200 OK
# Server: Werkzeug/3.1.9 Python/3.12.3
# Date: Sat, 03 Oct 2026 04:24:26 GMT
# Content-Type: application/json
# Content-Length: 16
# Connection: close

# {"status":"ok"}
# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/project1$ curl -i -X POST http://127.0.0.1:5000/users \
#   -H "Content-Type: application/json" \
#   -d '{"name":"Dhinesh","email":"dhinesh@example.test"}'
# HTTP/1.1 201 CREATED
# Server: Werkzeug/3.1.9 Python/3.12.3
# Date: Sat, 03 Oct 2026 04:24:36 GMT
# Content-Type: application/json
# Content-Length: 57
# Connection: close

# {"email":"dhinesh@example.test","id":1,"name":"Dhinesh"}
# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/project1$ curl -i -X POST http://127.0.0.1:5000/users \
#   -H "Content-Type: application/json" \
#   -d '{"name":"Dhinesh","email":"dhinesh@example.test"}'
# HTTP/1.1 409 CONFLICT
# Server: Werkzeug/3.1.9 Python/3.12.3
# Date: Sat, 03 Oct 2026 04:24:42 GMT
# Content-Type: application/json
# Content-Length: 33
# Connection: close

# {"error":"Email already exists"}
# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/project1$ curl -i http://127.0.0.1:5000/users/1
# HTTP/1.1 200 OK
# Server: Werkzeug/3.1.9 Python/3.12.3
# Date: Sat, 03 Oct 2026 04:25:01 GMT
# Content-Type: application/json
# Content-Length: 57
# Connection: close

# {"email":"dhinesh@example.test","id":1,"name":"Dhinesh"}
# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/project1$ 
