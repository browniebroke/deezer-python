# Asynchronous client

You also can use an
{class}`AsyncClient <deezer.contrib.tornado.AsyncClient>` with tornado, which requires an optional dependency. You should install with `pip install deezer-python[tornado]`.

Then, making a request would look like this:

```python
>>> from tornado.gen import coroutine
>>> from tornado.ioloop import IOLoop
>>> from deezer.contrib.tornado import AsyncClient
>>>
>>>
>>> @coroutine
... def main():
...     client = AsyncClient()
...     album = yield client.get_album(12)
...     print(album.title)
...
>>> IOLoop.instance().run_sync(main)
Monkey Business
```

The {class}`AsyncClient <deezer.contrib.tornado.AsyncClient>` implements the same methods as the main
{class}`Client <deezer.client.Client>` class
and would return the same resources.
