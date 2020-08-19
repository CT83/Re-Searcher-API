#!/usr/bin/env python
import os

from app import create_app

env = os.environ.get("FLASK_ENV", "default")
app = create_app(os.environ.get("FLASK_ENV", "default"))
client = app.client


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, )


@app.cli.command()
def create_all_tables():
    """Create all tables"""
    from models.search_results import SearchRequests
    if not SearchRequests.exists():
        SearchRequests.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)


@app.cli.command()
def drop_all_tables():
    """Drop all tables"""
    raise NotImplementedError("This is not Implemented Yet!")
