# /// script
# requires-python = '>=3.13'
# dependencies = [
#     'marimo',
#     'polars==1.22.0',
# ]
# ///

import marimo

__generated_with = '0.11.4'
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import polars as pl
    return mo, pl


@app.cell
def _(mo):
    mo.sidebar(
        [
            mo.md('# testos'),
            mo.nav_menu(
                {
                    '#/home': f'{mo.icon('lucide:home')} Home',
                    '#/about': f'{mo.icon('lucide:user')} About',
                    '#/contact': f'{mo.icon('lucide:phone')} Contact',
                    'Links': {
                        '/apps/heteroscedasticity.html': 'Heteroscedasticity',
                        '/apps/hypothesis_testing.html': 'Hypothesis testing',
                    },
                },
                orientation='vertical',
            ),
        ]
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == '__main__':
    app.run()
