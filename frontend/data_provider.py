import requests
import plotly.graph_objs as go
import pandas as pd
import random

API_URL = "https://example.com/api/dashboard"  # هنا نحط API

def generate_mock_data():
    total_spots = 200
    occupied_spots = random.randint(100, 200)
    available_spots = total_spots - occupied_spots
    occupancy_rate = round((occupied_spots / total_spots) * 100, 2)
    expected_occupancy = min(100, occupancy_rate + random.uniform(-5, 10))
    avg_parking_time = random.randint(15, 90)
    avg_entries = random.randint(20, 80)
    peak_entry = f"{random.randint(7, 10)}:00"
    peak_exit = f"{random.randint(16, 19)}:00"
    total_today = random.randint(150, 400)

    hours = list(range(0, 24))
    entries = [random.randint(0, 25) for _ in hours]
    exits = [random.randint(0, 25) for _ in hours]
    traffic_df = pd.DataFrame({"hour": hours, "entries": entries, "exits": exits})

    return {
        "total_spots": total_spots,
        "available_spots": available_spots,
        "occupied_spots": occupied_spots,
        "occupancy_rate": occupancy_rate,
        "expected_occupancy": round(expected_occupancy, 2),
        "avg_parking_time": avg_parking_time,
        "avg_entries_per_hour": avg_entries,
        "peak_entry_time": peak_entry,
        "peak_exit_time": peak_exit,
        "total_cars_today": total_today,
        "traffic_df": traffic_df
    }

def get_dashboard_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        api_data = response.json()

        total_spots = api_data.get("total_spots", "--")
        available_spots = api_data.get("available_spots", "--")
        occupied_spots = api_data.get("occupied_spots", "--")
        occupancy_rate = api_data.get("occupancy_rate", "--")
        expected_occupancy = api_data.get("expected_occupancy", "--")
        avg_parking_time = api_data.get("avg_parking_time", "--")
        avg_entries = api_data.get("avg_entries_per_hour", "--")
        peak_entry = api_data.get("peak_entry_time", "--")
        peak_exit = api_data.get("peak_exit_time", "--")
        total_today = api_data.get("total_cars_today", "--")
        traffic_df = pd.DataFrame(api_data.get("traffic_data", []))

    except Exception as e:
        print("API Error:", e)
        print("Using mock data instead.")
        mock_data = generate_mock_data()
        total_spots = mock_data["total_spots"]
        available_spots = mock_data["available_spots"]
        occupied_spots = mock_data["occupied_spots"]
        occupancy_rate = mock_data["occupancy_rate"]
        expected_occupancy = mock_data["expected_occupancy"]
        avg_parking_time = mock_data["avg_parking_time"]
        avg_entries = mock_data["avg_entries_per_hour"]
        peak_entry = mock_data["peak_entry_time"]
        peak_exit = mock_data["peak_exit_time"]
        total_today = mock_data["total_cars_today"]
        traffic_df = mock_data["traffic_df"]

    try:
        traffic_figure = go.Figure()

        traffic_figure.add_trace(go.Scatter(
            x=traffic_df["hour"],
            y=traffic_df["entries"],
            mode='lines+markers',
            name='Entries',
            line=dict(color="#00cc36")
        ))

        traffic_figure.add_trace(go.Scatter(
            x=traffic_df["hour"],
            y=traffic_df["exits"],
            mode='lines+markers',
            name='Exits',
            line=dict(color="#b80000")
        ))

        traffic_figure.update_layout(
            title="Traffic Movement Today",
            xaxis_title="Hour",
            yaxis_title="Number of Cars",
            template="plotly_white",
            xaxis=dict(range=[0, max(traffic_df["hour"].max(), 1)]),
            yaxis=dict(range=[0, max(max(traffic_df["entries"].max(), traffic_df["exits"].max()), 1)]),
            legend=dict(
                x=1, y=1,
                xanchor="right",
                yanchor="top",
                bgcolor="rgba(255,255,255,0.8)",
                bordercolor="lightgray",
                borderwidth=1
            )
        )

    except Exception as e:
        print("Plot Error:", e)
        traffic_figure = go.Figure()

    return {
        "total_spots": total_spots,
        "available_spots": available_spots,
        "occupied_spots": occupied_spots,
        "occupancy_rate": occupancy_rate,
        "expected_occupancy": expected_occupancy,
        "avg_parking_time": avg_parking_time,
        "avg_entries_per_hour": avg_entries,
        "peak_entry_time": peak_entry,
        "peak_exit_time": peak_exit,
        "total_cars_today": total_today,
        "traffic_figure": traffic_figure
    }
