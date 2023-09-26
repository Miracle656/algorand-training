import beaker as bk
import pyteal as pt

class MyState:
    result = bk.GlobalStateValue(pt.TealType.uint64)

app = bk.Application("Calculator", state=MyState())

@app.external
def add(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    add_result = a.get() + b.get()
    return pt.Seq(
        app.state.result.set(add_result),
        output.set(add_result)
    )

@app.external
def subtract(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    sub_result = a.get() - b.get()
    return pt.Seq(
        app.state.result.set(sub_result),
        output.set(sub_result)
    )

@app.external
def product(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    product_result = a.get() * b.get()
    return pt.Seq(
        app.state.result.set(product_result),
        output.set(product_result)
    )

@app.external
def divide(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    try:
        divide_result = a.get() / b.get()
        return pt.Seq(
            app.state.result.set(divide_result),
            output.set(divide_result)
        )
    except:
        return output.set("Division by 0 error")


@app.external(read_only=True)
def read_result(*, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(app.state.result)


if __name__ == "__main__":
    spec = app.build()
    spec.export("artifacts")
