from flask import Flask, jsonify, abort

app = Flask(__name__)

def compute_factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@app.route("/fact/<int:n>", methods=["GET"])
def fact(n: int):
    if n < 0:
        abort(400, description="El número debe ser un entero no negativo")

    factorial = compute_factorial(n)
    parity = "impar" if n in (0, 1) else "par"

    return jsonify({
        "input": n,
        "factorial": str(factorial),
        "paridad_factorial": parity
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensaje": "Bienvenido al microservicio factorial. Usa /fact/<n> para calcular el factorial de n."
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
