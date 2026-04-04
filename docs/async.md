(async-guide)=

# Async Client

If you are working with an async framework like [aiohttp](https://docs.aiohttp.org/) or [FastAPI](https://fastapi.tiangolo.com/), you can use the async client from the {mod}`deezer.asyncio` sub-package. It provides the same functionality as the synchronous {class}`Client <deezer.Client>`, but with `async`/`await` support.

## Getting started

The async client should be used as an async context manager:

```python
from deezer.asyncio import AsyncClient

async with AsyncClient() as client:
    album = await client.get_album(302127)
    print(album.title)
```

As with the sync client, you can pass an `access_token` for authenticated requests:

```python
async with AsyncClient(access_token="your-token") as client:
    user = await client.get_user()
    print(user.name)
```

## Fetching resources

All the methods that fetch resources from the Deezer API are coroutines and need to be awaited:

```python
async with AsyncClient() as client:
    artist = await client.get_artist(27)
    album = await client.get_album(302127)
    track = await client.get_track(3135556)
```

The returned objects are async resource classes (e.g. {class}`~deezer.asyncio.AsyncArtist`, {class}`~deezer.asyncio.AsyncAlbum`), which mirror their sync counterparts.

## Navigating relationships

Relationship methods that return a single resource or a plain list need to be awaited:

```python
async with AsyncClient() as client:
    track = await client.get_track(3135556)

    # These return a single resource
    artist = await track.get_artist()
    album = await track.get_album()

    # This returns a plain list
    radio = await artist.get_radio()
```

Methods that return paginated responses return an {class}`~deezer.asyncio.AsyncPaginatedList` **synchronously** (no `await` needed), as the actual API calls are deferred until you iterate or access elements:

```python
async with AsyncClient() as client:
    artist = await client.get_artist(27)

    # No await here - returns AsyncPaginatedList immediately
    albums = artist.get_albums()
```

See the next section for how to work with paginated results.

## Async Pagination

For endpoints returning paginated responses, items are wrapped in an {class}`~deezer.asyncio.AsyncPaginatedList`. This works similarly to the synchronous {class}`~deezer.PaginatedList` described in the {ref}`pagination guide <pagination-guide>`, but uses async iteration.

### Iterating over elements

Use `async for` to iterate over all elements, transparently fetching additional pages as needed:

```python
artist_albums = artist.get_albums()

async for album in artist_albums:
    print(album.title)
```

### Total number

The total number of items is fetched from the API asynchronously:

```python
total = await artist_albums.total()
```

### Accessing elements by index

Use the {meth}`~deezer.asyncio.AsyncPaginatedList.get` method to access an element by index:

```python
first_album = await artist_albums.get(0)
fifth_album = await artist_albums.get(4)
```

As with the sync version, accessing a large index may trigger extra API calls to fetch preceding pages.

### Collecting all elements

To fetch all pages and get a plain list, use {meth}`~deezer.asyncio.AsyncPaginatedList.collect`:

```python
all_albums = await artist_albums.collect()
```

### Search

Search methods also return {class}`~deezer.asyncio.AsyncPaginatedList`:

```python
async with AsyncClient() as client:
    results = client.search("Daft Punk")

    async for track in results:
        print(track.title)
```

Variant search methods are also available: {meth}`~deezer.asyncio.AsyncClient.search_albums`, {meth}`~deezer.asyncio.AsyncClient.search_artists`, and {meth}`~deezer.asyncio.AsyncClient.search_playlists`.
