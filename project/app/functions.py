import numpy as np
import plotly.graph_objects as go
from sklearn import linear_model

_data_size = np.random.randint(200, 600)

fig_layout = {
    "plot_bgcolor": "black",
    "paper_bgcolor": "black",
    "title": {"font": {"size": 20, "color": "white"}},
    "legend": {
        "font": {"size": 14, "color": "white"},
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.02,
        "xanchor": "right",
        "x": 1,
    },
    "xaxis": {"color": "lightgray", "showgrid": False},
    "yaxis": {"color": "lightgray"},
}


def plot_regression(std=10):
    _x_og = np.arange(0, _data_size)
    x = _x_og.reshape((-1, 1))
    y = _x_og * (
        np.full(shape=_data_size, fill_value=1, dtype=np.int)
        + np.random.normal(size=_data_size, loc=1, scale=std / 10)
    )

    model = linear_model.LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    preds = model.predict(x)

    layout = go.Layout(
        title=f"Regression fit R squared: {round(r_sq, 3)}",
        height=700,
    )
    fig = go.Figure(layout=layout)

    fig.add_trace(
        go.Scatter(
            x=_x_og,
            y=y,
            mode="markers",
            name=f"x * (1 + rand_norm(mean=1, std={std}/10))",
        )
    )
    fig.add_trace(go.Line(x=_x_og, y=preds, name="linear regression"))
    fig.update_layout(fig_layout)

    return fig


def getStackedBar():
    print()  
    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=[''],
        x=[15],
        name="Remaining",
        orientation='h',
        marker=dict(
            color='#F44336',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        ),
    ))
    fig.add_trace(go.Bar(
        y=[''],
        x=[20],
        name="Paid",
        orientation='h',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))
    fig.update_layout(
        barmode="stack",
    )
    fig.update_traces(marker_line_width=0, hovertemplate="%{x}%")
    return fig


def get_user_stats():
    return {
        "Successfully paid loans": 65,
        "Outstanding loans": 15.7,
        "Forgiven loans": 5.6,
        "In progress": 2.1,
        "Forfeit": 1.9,
        "Other": 1.5
    }


def loan_balance():
    return {
        "credit_score": 700, 
        "score_increase": 25, 
        "remaining_debt": 15000, 
        "original_loan": 20000, 
    }
