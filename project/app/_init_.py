app = dash.Dash(__name__)
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True, threaded=True)