import marimo

__generated_with = "0.9.10-dev11"
app = marimo.App(width="medium", layout_file="layouts/notebook.grid.json")


@app.cell
def __():
    import marimo as mo
    import altair as alt
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    from scipy import stats
    return alt, mo, norm, pd, plt, stats


@app.cell
def __(mo):
    import numpy as np
    from numpy.linalg import inv

    mo.show_code()
    return inv, np


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""# Least square regression""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        \[
        \\hat{\\beta}_{ols} = (X^TX)^{-1}X^Ty
        \]
        """
    )
    return


@app.cell
def __(np):
    np.random.seed(11)
    N = 1_000
    x_min, x_max = 140, 210
    return N, x_max, x_min


@app.cell
def __(mo):
    N_slider = mo.ui.slider(
        start=3,
        stop=1_000,
        # debounce=True,
        value=10,
        label="Number of observations",
        full_width=True,
        show_value=True,
    )

    slider_width = mo.ui.slider(
        start=100,
        stop=2560,
        step=10,
        value=1040,
        label="Width",
        debounce=True,
        show_value=True,
        full_width=True,
    )

    slider_height = mo.ui.slider(
        start=50,
        stop=1440,
        step=10,
        value=460,
        label="Height",
        debounce=True,
        show_value=True,
        full_width=True,
    )
    return N_slider, slider_height, slider_width


@app.cell
def __(N, np):
    height = np.floor(np.random.normal(loc=180, scale=10, size=N))
    weight = height // 3 + np.random.randint(low=0, high=50, size=N)
    const = np.ones(N)
    return const, height, weight


@app.cell
def __(N_slider, const, height, np, pd, weight):
    x = height[: N_slider.value]
    y = weight[: N_slider.value]
    c = const[: N_slider.value]
    X = np.column_stack((c, x))
    df = pd.DataFrame({"Height (cm)": x, "Weight (kg)": y})
    df["Height (cm)"] = df["Height (cm)"].astype(int)
    df["Weight (kg)"] = df["Weight (kg)"].astype(int)
    return X, c, df, x, y


@app.cell
def __(X, inv, mo, y):
    intercept, slope = inv(X.T @ X) @ X.T @ y

    mo.show_code()
    return intercept, slope


@app.cell
def __(
    alt,
    df,
    intercept,
    mo,
    pd,
    slider_height,
    slider_width,
    slope,
    x_max,
    x_min,
):
    chart = (
        alt.Chart(df)
        .mark_circle(size=20)
        .encode(
            x=alt.X(
                "Height (cm)",
                axis=alt.Axis(format="d"),
                scale=alt.Scale(domain=(x_min, x_max)),
            ),
            y=alt.Y(
                "Weight (kg)",
                axis=alt.Axis(format="d"),
                scale=alt.Scale(domain=(50, 115)),
            ),
            tooltip=["Height (cm)", "Weight (kg)"],
            color=alt.value("#56B4E9"),
            stroke=alt.value("black"),
            strokeWidth=alt.value(1),
        )
    )

    abline_data = pd.DataFrame(
        {
            "Height (cm)": [x_min, x_max],
            "Weight (kg)": [slope * x_min + intercept, slope * x_max + intercept],
        }
    )

    abline = (
        alt.Chart(abline_data)
        .mark_line(color="#E69F00")
        .encode(x="Height (cm)", y="Weight (kg)")
    )

    final_chart = (
        (chart + abline)
        .configure_axis(titleFontSize=12, labelFontSize=10, grid=False)
        .properties(width=slider_width.value, height=slider_height.value)
    )

    final_altair_chart = mo.ui.altair_chart(final_chart)
    return abline, abline_data, chart, final_altair_chart, final_chart


@app.cell
def __(df, mo):
    weight_height_table = mo.ui.table(
        data=df,
        pagination=True,
        label="Dataframe with heights and weights",
        # selection=None,
        show_column_summaries=False,
    )
    return (weight_height_table,)


@app.cell
def __(weight_height_table):
    weight_height_table
    return


@app.cell
def __(mo):
    mo.md("""# Adding observations""")
    return


@app.cell
def __(mo):
    mo.md("""Number of observations""")
    return


@app.cell(hide_code=True)
def __(N_slider):
    N_slider
    return


@app.cell(hide_code=True)
def __(slider_width):
    slider_width
    return


@app.cell(hide_code=True)
def __(slider_height):
    slider_height
    return


@app.cell(hide_code=True)
def __(intercept, mo, slope):
    if slope >= 0:
        equation_ols = mo.md(
            f"""\[ \\widehat{{\\text{{Weight}}}} = {intercept:.2f} + {slope:.2f} \\text{{Height}} \]"""
        )
    else:
        equation_ols = mo.md(
            f"""\[ \\widehat{{\\text{{Weight}}}} = {intercept:.2f}{slope:.2f} \\text{{Height}} \]"""
        )
    return (equation_ols,)


@app.cell
def __(equation_ols):
    equation_ols
    return


@app.cell(hide_code=True)
def __(final_altair_chart):
    final_altair_chart
    return


if __name__ == "__main__":
    app.run()
