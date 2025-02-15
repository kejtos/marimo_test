# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair==5.5.0",
#     "marimo",
#     "numpy==2.2.3",
#     "pandas==2.2.3",
#     "scipy==1.15.1",
# ]
# ///

import marimo

__generated_with = "0.11.4"
app = marimo.App()


@app.cell
def _():
    from helpers.menu import menu
    output, definitions = menu.run()
    output
    return definitions, menu, output


@app.cell
def _():
    import altair as alt
    return (alt,)


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    from numpy.linalg import inv
    from scipy import stats
    import math
    from numpy.random import normal
    from numpy import var, cov, ones, column_stack
    return (
        column_stack,
        cov,
        inv,
        math,
        mo,
        normal,
        np,
        ones,
        pd,
        stats,
        var,
    )


@app.cell
def _(alt):
    GRAPH_WIDTH = 600
    GRAPH_HEIGHT = 200
    _ = alt.theme.enable('opaque')
    return GRAPH_HEIGHT, GRAPH_WIDTH


@app.cell
def _(mo):
    mo.md("""# Ordinary Least Squares""")
    return


@app.cell
def _(column_stack, cov, inv, normal, np, ones, var):
    np.random.seed(11)
    N = 100
    y = normal(50_000, 10_000, N)
    x = normal(180, 10, N)
    constant = ones(N)
    X = column_stack((constant, x))

    x_min, x_max = x.min(), x.max()
    y_min, y_max = y[x.argmin()], y[x.argmax()]

    slope = (x_max - x_min)/(y_max - y_min)
    line = slope*x
    beta = inv(X.T @ X) @ X.T @ y

    var_y = var(y)
    var_x = var(x)
    cov_xy = cov(x, y)[0, 1]

    xi = normal(1, 2, N)
    X = column_stack((X, xi))
    k = X.shape[1] - 1
    beta = inv(X.T @ X) @ X.T @ y
    y_hat = X @ beta
    residuals = y_hat - y
    SSR = sum((residuals)**2)
    SST = sum(((y - y.mean())**2))
    SSE = SST - SSR
    R_squared = SSE / SST
    R_adj = 1 - (((1 - R_squared) * (N - 1)) / (N - k - 1))
    return (
        N,
        R_adj,
        R_squared,
        SSE,
        SSR,
        SST,
        X,
        beta,
        constant,
        cov_xy,
        k,
        line,
        residuals,
        slope,
        var_x,
        var_y,
        x,
        x_max,
        x_min,
        xi,
        y,
        y_hat,
        y_max,
        y_min,
    )


@app.cell
def _(mo):
    n = mo.ui.slider(0, 98, debounce=False, value=5)
    return (n,)


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
