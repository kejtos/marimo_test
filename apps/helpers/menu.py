# /// script
# requires-python = '>=3.13'
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.11.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import os
    return mo, os


@app.cell
def _(os):
    repo_full = os.environ.get('GITHUB_REPOSITORY')
    if repo_full:
        repo_name = repo_full.split('/')[-1]

    repo_name = 'marimo_test'
    folder = f'/{repo_name}/apps/'

    pairing = {
        'causality_and_experiments': 'Causality and experiments',
        'population_sample': 'Population vs sample',
        'adding_observations': 'Adding observations',
        'estimator_properties': 'Estimator properties',
        'gauss_markov': 'Gauss-Markov Theorem',
        'r_squared': 'R-squared',
        'issues_r_squared': 'Issues with R-squared',
        'hypothesis_testing': 'Hypothesis testing',
        'heteroscedasticity': 'Heteroscedasticity',
    }

    intro_eko = {}
    for key, value in pairing.items():
        intro_eko[f'/{folder}{key}.html'] = value

    intro_games = {
        f'/{folder}heteroscedasticity.html': 'Heteroscedasticity',
        f'/{folder}hypothesis_testing.html': 'Hypothesis testing',
    }
    return intro_eko, intro_games, repo_full, repo_name


@app.cell
def menu(intro_eko, intro_games, mo):
    intro_eko_menu = mo.nav_menu({'4EK214': intro_eko}, orientation='vertical')
    intro_eko_games = mo.nav_menu({'4EK602': intro_games}, orientation='vertical')

    mo.sidebar([
        mo.md('## Materials'),
        intro_eko_menu,
        mo.md('[Moodle](https://moodle.vse.cz/course/view.php?id=14663)'),

        intro_eko_games,
        mo.md('[Moodle](https://moodle.vse.cz/course/view.php?id=16655)'),
    ])
    return intro_eko_games, intro_eko_menu


if __name__ == "__main__":
    app.run()
