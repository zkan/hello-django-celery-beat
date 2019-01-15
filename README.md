# Hello, Django Celery Beat!

Start a scheduler:

```sh
$ cd hello_django_celery_beat
$ celery -A hello_django_celery_beat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

Start a worker:

```sh
$ cd hello_django_celery_beat
$ celery -A hello_django_celery_beat worker -l info -Q my_queue_1,my_q_2
```

Alternatively, we can start a scheduler and a worker in one command:

```sh
$ cd hello_django_celery_beat
$ celery -A hello_django_celery_beat worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler -Q my_queue_1,my_q_2
```
