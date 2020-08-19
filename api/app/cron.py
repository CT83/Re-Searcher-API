from shared.factories import client


@client.task
def scheduler_start(config):
    print("Running on the worker!")


def init_cron(app, config_name):
    pass
    # scheduler = APScheduler()
    # scheduler.init_app(app)
    #
    # lock = "/tmp/lock"
    # if not os.path.isfile(lock):
    #     create_random_file(lock)
    #
    #     with app.app_context():
    #         scheduler_start.apply_async(args=[config_name])
    #
    #         app.apscheduler.add_job(id="spawn_" + str(generate_random_hex()),
    #                                 func=scheduled_task, args=[config_name],
    #                                 trigger="interval",
    #                                 seconds=45,
    #                                 replace_existing=True)
    #
    #     # Shut down the scheduler when exiting the app
    #     def cleanup():
    #         scheduler.shutdown()
    #         os.remove(lock)
    #
    #     atexit.register(lambda: cleanup())
