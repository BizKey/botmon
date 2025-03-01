from dash import Dash, html, dcc
import psycopg
import os


def get_exchanges():
    """Get data from db."""
    with psycopg.connect(
        f"host={os.getenv('PG_HOST')} port={os.getenv('PG_PORT')} dbname={os.getenv('PG_DATABASE')} user={os.getenv('PG_USER')} password={os.getenv('PG_PASSWORD')}"
    ) as conn:

        with conn.cursor() as cur:
            cur.execute("""SELECT DISTINCT exchange FROM main""")
            return [str(d[0]) for d in cur.fetchall()]


app = Dash()

app.title = "BotMon"
app._favicon = "favicon.png"

list_exchange = get_exchanges()

app.layout = html.Div(
    [
        html.H1(children="BotMon"),
        dcc.Dropdown(list_exchange, list_exchange[0], id="dropdown-selection"),
        dcc.Graph(id="graph-content"),
    ]
)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
