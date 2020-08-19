import random

from flask import request
from flask_restful import Resource

from shared.factories import db, client

#
# @client.task
# def background_task(data):
#     """ Function to send emails.
#     """
#     v = SampleDataModel(random_data=str(random.randint(1, 1000)))
#     db.session.add(v)
#     db.session.commit()
#     print("this is running on worker")
#
#
# class TasksRes(Resource):
#
#     def post(self):
#         seed = request.get_json()['seed']
#         background_task.apply_async(args=[seed], countdown=0)
#         return {"message": "Job added to queue",
#                 "job_id": 0, }
#
#     def get(self):
#         return {"msg": {"test"}, }
#
#
# class HelloWorldRes(Resource):
#
#     def get(self):
#         return "Hello World"
