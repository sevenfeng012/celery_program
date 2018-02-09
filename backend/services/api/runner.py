import commands

commands.getoutput("celery -A tasks worker --loglevel=info")
