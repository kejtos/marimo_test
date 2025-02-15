# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair==5.5.0",
#     "marimo",
#     "polars==1.22.0",
# ]
# ///
import marimo

__generated_with = "0.10.12"
app = marimo.App(width="medium")


@app.cell
def _():
    from helpers.menu import menu
    output, definitions = menu.run()
    output
    return definitions, menu, output


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    import polars as pl
    import altair as alt
    return alt, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## 1. Econometric Paradigms

        Let's make a simple econometric model:

        $$
        y = \\beta_0 + \\beta_1 x + \\varepsilon
        $$

        Two or three approaches are generally taken in econometric (and not only econometric) modeling depending on the goal of the analysis.

        ### To **explain** relationship between $x$ and $y$

        We care about the existence and size of a relatioship between variables. We use this when we care about ifs and whys, which should influence our decision making. We are concerned about the sign and the size of $\\beta_1$, and about how much confidence we have in that $\\beta_1$.

        #### Descriptive
        Here, we just describe relationship between variables. $\\beta_1$ shows the size of the relationship between $x$ and $y$ of size.

        #### Structural (Causal)
        Here, we attempt to identify causal relationships. $\\beta_1$ shows how much does $x$ cause $y$.

        ### To **predict** $y$

        We do not care as much about the existence and size of a relatioship between variables, but rather about how well can our model predict future $y$. We are concerned about how close are our predictions to newly observed values of y.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        | Example | Descriptive | Structural | Predictive |
        |-----------------------------------|----------------------------------------|--------------------------------------|---------------------------------------------|
        | Education and Earnings | Do earings increase with education? | Does education increase earnings? | Can we predict earnings customer's earnings? |
        | Crime and Policing | Is there a relationship between the number police officers and crime? | What is the effect of police on crime? | What will the level of crime in LA be in 10 years? |
        | Consumption and Income | Is there an association between incomes and spending? | How much more do people spend when their income doubles? | What are the likely spendings of a customer's household? |
        | Unemployment and Economic Growth | What is the relationship between economic growth and unemployment? | Is there a causal effect of economic growth on unemployment? | Can we forecast unemployment next year? |
        | Health Outcomes and Quality of Care | Is there a relationship between the quality of care and health? | Does better care improve health? | Can we predict the quality of health of a Vinohradska hospital from data about other hospitals in Prague? |

        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## 2. Causality

        The structural paradigm attempts to find the causal effects of variables. However, identifying genuine causal effects is difficult, and various methods have been developed to address these issues.
        """
    )
    return


@app.cell(hide_code=True)
def _(chart, mo):
    mo.md(
        f"""
    ### Correlation vs causation

    Correlation does not imply causation. Just because I find (or see) a relationship between variables $x$ and $y$, it does not mean that $x$ causes $y$ or that changes in $y$ happened due to changes in $x$.

    #### Spurious correlation or regression

    Random correlations occur all over the place. For instance, you can find strong correlation between bachelor's degrees awarded in precision production and the number of parking enforcement workers in New Jersey. You can find many other examples [here](https://www.tylervigen.com/spurious-correlations).

    {chart}

    Similarly, you can find strong correlations between seasonal or trending variables. Last, _If you torture the data long enough, it will confess to anything._

    #### Causal Schemes

    Even if the relationship between $x$ and $y$ is genuine, the causal relationship can go in different directions.

    1. $ x \\rightarrow y $, in other words $x$ causes $y$
    2. $ y \\rightarrow x $, in other words $y$ causes $x$
    3. $ x \\leftarrow z \\rightarrow y $, in other words $z$ cause both $x$ and $y$.

    Few examples of the possible relationships:
    """
    )
    return


@app.cell(hide_code=True)
def _(crime, econ, mo, sport):
    mo.ui.tabs(
        {
            "Sport psychology": sport,
            "Economics": econ,
            "Crime": crime,
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        When trying to infer causality, different experimental designs provide varying degrees of credibility:

        **Natural Experiments:** When something outside of the power of hte investigator ('natural') split subjects into two groups. For instance, South vs North Korea, Czechia vs Slovakia, Vietnam War draft etc.

        **Randomized Experiments:** Individuals (or units) are randomly assigned to treatment and control groups by the researchers. 

        **Laboratory Experiments:** Conducted in a controlled environment, usually a laboratory (hence the name).

        **Ceteris Paribus modeling:** Regression attempts to model the effect of $x$ on $y$ ceteris paribus ('all else staying the same'). It is used as a complement or a substitute to the experimental design. Estimating relationships ceteris paribus do not guarantee we find genuine causal effects, but it is often the best we can do.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""The descriptive and structural paradigm are often used somewhat interchangably, but we need to take extra care when we try to imply or infer an actual causal relationship. You might often see alterantive naming, which categorizes models into **inferential** or **predicive**.""")
    return


@app.cell(hide_code=True)
def _(mo):
    def x_to_y(x, y):
        return mo.mermaid(
            f"""
        flowchart LR
            A[{x}]
            B[{y}]

            A ====> B

            classDef roundedRect fill:transparent, stroke:#333, stroke-width:3px, rx:10, ry:10;
            class A,B roundedRect;
        """
        )


    def y_to_x(x, y):
        return mo.mermaid(
            f"""
        flowchart RL
            A[{x}]
            B[{y}]

            B ====> A

            classDef roundedRect fill:transparent, stroke:#333, stroke-width:3px, rx:10, ry:10;
            class A,B, roundedRect;
        """
        )


    def x_y_y(x, y):
        return mo.mermaid(
            f"""
        flowchart RL
            A[{x}]
            B[{y}]

            B <====> A

            classDef roundedRect fill:transparent, stroke:#333, stroke-width:3px, rx:10, ry:10;
            class A,B, roundedRect;
        """
        )


    def z_to_x_y(x, y, z):
        return mo.mermaid(
            f"""
        flowchart BT
            A[{x}]
            B[{y}]
            C[{z}]

            C ====> A
            C ====> B

            classDef roundedRect fill:transparent, stroke:#333, stroke-width:3px, rx:10, ry:10;
            class A,B,C roundedRect;
        """
        )
    return x_to_y, x_y_y, y_to_x, z_to_x_y


@app.cell(hide_code=True)
def _():
    sport_x = "Self-confidence"
    sport_y = "Performance"
    sport_z = "Quality coaching"

    econ_x = "Wealth"
    econ_y = "Education"
    econ_z = "Inherited traits"

    crime_x = "Police budget"
    crime_y = "Level of crime"
    crime_z = "Size of the city"
    return (
        crime_x,
        crime_y,
        crime_z,
        econ_x,
        econ_y,
        econ_z,
        sport_x,
        sport_y,
        sport_z,
    )


@app.cell(hide_code=True)
def _(
    crime_x,
    crime_y,
    crime_z,
    econ_x,
    econ_y,
    econ_z,
    mo,
    sport_x,
    sport_y,
    sport_z,
    x_to_y,
    x_y_y,
    y_to_x,
    z_to_x_y,
):
    sport = mo.vstack(
        [
            mo.vstack(["X cause Y", x_to_y(sport_x, sport_y)]),
            mo.vstack(["Y cause X", y_to_x(sport_x, sport_y)]),
            mo.vstack(["X cause Y and Y cause X", x_y_y(sport_x, sport_y)]),
            mo.vstack(["Z cause X and Y", z_to_x_y(sport_x, sport_y, sport_z)]),
        ],
        gap=2,
    )

    econ = mo.vstack(
        [
            mo.vstack(["X cause Y", x_to_y(econ_x, econ_y)]),
            mo.vstack(["Y cause X", y_to_x(econ_x, econ_y)]),
            mo.vstack(["X cause Y and Y cause X", x_y_y(econ_x, econ_y)]),
            mo.vstack(["Z cause X and Y", z_to_x_y(econ_x, econ_y, econ_z)]),
        ],
        gap=2,
    )

    crime = mo.vstack(
        [
            mo.vstack(["X cause Y", x_to_y(crime_x, crime_y)]),
            mo.vstack(["Y cause X", y_to_x(crime_x, crime_y)]),
            mo.vstack(["X cause Y and Y cause X", x_y_y(crime_x, crime_y)]),
            mo.vstack(["Z cause X and Y", z_to_x_y(crime_x, crime_y, crime_z)]),
        ],
        gap=2,
    )
    return crime, econ, sport


@app.cell(hide_code=True)
def _(alt, mo, pl):
    df = pl.DataFrame(
        {
            "Bachelor_Degrees": [37, 36, 37, 48, 51, 32, 45, 47, 39, 28],
            "Parking_Workers": [410, 390, 400, 460, 430, 340, 440, 460, 410, 300],
        }
    )

    scatter = (
        alt.Chart(df)
        .mark_point(size=100)
        .encode(
            x=alt.X(
                "Bachelor_Degrees:Q",
                title="Bachelor's degrees awarded in Precision production",
                scale=alt.Scale(domain=[25, 55]),
            ),
            y=alt.Y(
                "Parking_Workers:Q",
                title="Number of parking enforcement workers in New Jersey",
                scale=alt.Scale(domain=[250, 500]),
            ),
        )
        .properties(title="Scatter Plot with Regression Line")
    )

    chart = mo.ui.altair_chart(
        scatter.configure_axis(titleFontSize=12, labelFontSize=10, grid=False)
        .configure_title(fontSize=16)
        .properties(title="Spurious correlation", width=950, height=400)
    )
    return chart, df, scatter


if __name__ == "__main__":
    app.run()
