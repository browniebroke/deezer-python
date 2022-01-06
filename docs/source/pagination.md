# Pagination

For endpoints returning a paginated response, the list of items are wrapped in a {class}`PaginatedList <deezer.pagination.PaginatedList>` class which makes working with pagination more Pythonic while doing the necessary API calls transparently.

## Iterating over elements

The class is iterable, meaning that you can go through instances in the list with a for loop:

```python
artist_albums = artist.get_albums()
for album in artist_albums:
    print(album.title)
```

This will take care or fetching extra pages if needed. Once all the elements have been fetched, no further network calls will happen. This will work if you iterate over the same paginated response again:

```python
# No API calls: artist_albums is reused from above
for album in artist_albums:
    print(album.title)
```

However, API calls would be repeated if you get a fresh paginated response again:

```python
for album in artist.get_albums():
    print(album.title)
```

Be mindful of that when writing your code otherwise you'll consume your API quota quickly!

## Total number

If you want to know the total number of items in the list, you can either use the `total` property, which is mirroring what's returned by Deezer, or use the more Pythonic `len()` built-in:

```python
# total property
print(artist_albums.total)
# with len() built-in
len(artist_albums)
```

## Indexing

You can also access elements by index:

```python
second_album = artist_albums[1]
```

Beware that accessing a large index may produce some extra network calls to the Deezer API as pages preceding the given index will be fetched. For example, assuming the page size is 25, this will perform 5 API calls:

```python
artist_albums[110]
```

In case the index is too big, an `IndexError` will be raised, as if it were a list.

## Slicing

Slicing (`artist_albums[2:5]`) is not supported at this point, it might be added later.
