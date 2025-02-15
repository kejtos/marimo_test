# /// script
# requires-python = '>=3.13'
# dependencies = [
#     'marimo',
# ]
# ///

import marimo

__generated_with = '0.11.4'
app = marimo.App()


@app.cell
def _():
    from apps.helpers.menu import menu
    output, definitions = menu.run()
    output
    return definitions, menu, output


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def menu(mo):
    mo.md('All the apps should run in your browser. Some of them might take a few seconds, especially if you have got a slow PC.')
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
