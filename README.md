# Sanic-bug

The code of the application can be found in the `api/main.py`.

The code of the tests can be found in the `api/tests.py`.

### Problem

When the test `Tests.test_1` calls the `/` endpoint - everything is fine.

When the test `Tests.test_2` calls the `/` endpoint - a `RuntimeError` is raised with the message ` Event loop is closed`.

In case `aiopg` is not used - tests run fine.

### Run tests

Once you've built the container with a `docker-compose build` - just do `docker-compose up` any time you want to run the tests.
