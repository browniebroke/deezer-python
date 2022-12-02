(pagination-guide)=

# Pagination

For endpoints returning a paginated response, the list of items are wrapped in a {class}`PaginatedList <deezer.PaginatedList>` class which makes working with pagination more Pythonic while doing the necessary API calls transparently.

## Iterating over elements

The class is an iterator, meaning that you can go through instances in the list with a for loop, or by calling `next()` to get the following item:

```python
artist_albums = artist.get_albums()

# Iterable style
for album in artist_albums:
    print(album.title)

# Iterator
album_1 = next(artist_albums)
album_2 = next(artist_albums)
album_3 = next(artist_albums)
```

This will take care or fetching extra pages if needed. Once all the elements have been fetched, no further network calls will happen. This will work if you iterate over the same paginated response again:

```python
# No API calls: artist_albums is reused from above
for album in artist_albums:
    print(album.title)
```

However, API calls would be repeated if you get a fresh paginated response again:

```python
# New API calls: artist.get_albums() returns a fresh paginated list
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

In case the index is too big, an `IndexError` will be raised, as if it were a list. Unlike list, this feature doesn't support negative values at the time.

## Slicing

Slicing is also supported, you may take a slice with or without a start or end, and also provide a custom step number, like with a regular list:

```python
# With start & end
artist_albums[2:5]

# Without start
artist_albums[:5]

# Without end
artist_albums[5:]

# With start, end & step
artist_albums[2:10:2]
```

As with the rest, not providing an end, or providing a large value as end may produce extra network calls to the Deezer API. Like indexing, negative values aren't supported at the moment.
