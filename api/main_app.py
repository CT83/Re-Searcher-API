#!/usr/bin/env python
import os

import click
from flask_sqlalchemy import Model

from app import create_app
from shared.factories import db

env = os.environ.get("FLASK_ENV", "default")
app = create_app(os.environ.get("FLASK_ENV", "default"))
client = app.client


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Model=Model)


@app.cli.command()
def create_all_tables():
    """Create all tables"""
    db.create_all()


@app.cli.command()
def drop_all_tables():
    """Drop all tables"""
    db.drop_all()
