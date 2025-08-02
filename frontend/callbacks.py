from dash.dependencies import Output, Input
from data_provider import get_dashboard_data

def register_callbacks(app):
    @app.callback(
        [
            Output("total-spots", "children"),
            Output("available-spots", "children"),
            Output("occupied-spots", "children"),
            Output("occupancy-rate", "children"),
            Output("expected-occupancy", "children"),
            Output("avg-parking-time", "children"),
            Output("avg-entries", "children"),
            Output("peak-entry", "children"),
            Output("peak-exit", "children"),
            Output("total-today", "children"),
            Output("traffic-chart", "figure"),
        ],
        [Input("total-spots", "id")]  
    )
    def update_dashboard(_):
        
        data = get_dashboard_data()

        return (
            data['total_spots'],
            data['available_spots'],
            data['occupied_spots'],
            f"{data['occupancy_rate']}%",
            f"{data['expected_occupancy']}%",
            f"{data['avg_parking_time']} min",
            data['avg_entries_per_hour'],
            data['peak_entry_time'],
            data['peak_exit_time'],
            data['total_cars_today'],
            data['traffic_figure']
        )
