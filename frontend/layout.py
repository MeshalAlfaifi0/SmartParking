from dash import dcc, html
import dash_bootstrap_components as dbc

def create_card(title, id_value):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H6(title, className="card-title text-center"),
                html.H2(id=id_value, children="--", className="card-value text-center")
            ]),
            className="info-card h-100 shadow"
        ),
        xs=12, sm=6, md=4, lg=2, xl=2, xxl=2, className="mb-4"
    )

def create_layout(app):
    return dbc.Container([
        html.H2("Smart Parking Management Dashboard", className="text-center my-3"),

        # الصف الأول - البطاقات
        dbc.Row([
            create_card("Total Parking Spots", "total-spots"),
            create_card("Available Spots", "available-spots"),
            create_card("Occupied Spots", "occupied-spots"),
            create_card("Current Occupancy Rate", "occupancy-rate"),
            create_card("Expected Occupancy Next Hour", "expected-occupancy"),
        ], className="justify-content-center"),

        # الصف الثاني - البطاقات
        dbc.Row([
            create_card("Average Parking Time (min)", "avg-parking-time"),
            create_card("Average Entries per Hour", "avg-entries"),
            create_card("Total Cars Today", "total-today"),
            create_card("Peak Entry Time", "peak-entry"),
            create_card("Peak Exit Time", "peak-exit"),
        ], className="justify-content-center"),

        # الرسم البياني
        dbc.Row([
            dbc.Col(dcc.Graph(id="traffic-chart", style={"height": "450px"}), width=10)
        ], className="justify-content-center mt-4")
    ], fluid=True)