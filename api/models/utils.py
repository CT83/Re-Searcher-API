def init_tables(app):
    from models.search_results import SearchRequests
    if app.config['DB_URL'] == "":
        SearchRequests.Meta.host = None
    else:
        SearchRequests.Meta.host = app.config['DB_URL']
    SearchRequests.Meta.aws_access_key_id = app.config['AWS_ACCESS_KEY_ID']
    SearchRequests.Meta.aws_secret_access_key = app.config['AWS_SECRET_ACCESS_KEY']

    if not SearchRequests.exists():
        SearchRequests.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)