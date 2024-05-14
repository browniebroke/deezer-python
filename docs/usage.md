# Usage

## First steps

To start calling the API, you first need to instantiate a {class}`Client <deezer.client.Client>`:

```pycon
>>> client = deezer.Client()
```

While this usage is simple and convenient for using in the Python console, it's best to use it as a context manager:

```python
with deezer.Client() as client:
    ...
```

This is [the recommended way to use it by `httpx`](https://www.python-httpx.org/advanced/clients/#usage, which is the library we use under the hood.

From there, you can search for some terms:

```pycon
>>> client.search('Daft Punk')
<PaginatedList [
 <Track: One More Time>,
 <Track: I Feel It Coming>,
 <Track: Starboy>,
 <Track: Around the World>,
 <Track: Veridis Quo>,
 '...']>
```

The above returned a lot of tracks, wrapped in a {class}`PaginatedList <deezer.PaginatedList>`, which is a list-like object (see the dedicated {ref}`page about pagination <pagination-guide>` for more details).

If you wanted to search for artists instead, you may use the {meth}`Client.search_artists() <deezer.Client.search_artists>` method:

```pycon
>>> client.search_artists('Daft Punk')
<PaginatedList [
 <Artist: Daft Punk>,
 <Artist: Daft Punk - Stardust>,
 <Artist: Tribute to Daft Punk>,
 <Artist: Daft Punk Experience>,
 <Artist: Daft Punk's Karaoke Band>,
 '...']>
```

## Main concepts

As we have just seen above, the entry point is the {class}`Client <deezer.Client>` class, which gives access to a number of methods. The methods are attempting to map to the REST API endpoints from Deezer.

You may have noticed from the above examples, but depending on the endpoint that is being called, the methods will return various type of resources. All the resources are listed in the {ref}`resources reference page <resources-reference>`.

## More examples

### Getting a field about a resource

When you ge a resource, you have access to all the fields that are in the REST API response. For example, all the fields presented in the documentation for [the track object](https://developers.deezer.com/api/track) are accessible as attribute on the {class}`Track <deezer.Track>` resource:

```pycon
>>> instant_crush
<Track: Instant Crush>
>>> instant_crush.duration
337
>>> instant_crush.readable
True
>>> instant_crush.disk_number
1
```

### Navigating resource relationships

As well as giving access to its own attributes, a resource also gives access to other related resources.

For example, when you get an {class}`Artist <deezer.Artist>`, you may call one of the methods documented to get the artist's albums, then from an {class}`Album <deezer.Album>` get its tracks, and from a {class}`Track <deezer.Track>` you may go back to the {class}`Album <deezer.Album>` or the {class}`Artist <deezer.Artist>`.

Let's try from the initial example:

```pycon
>>> daft_punk = client.search_artists('Daft Punk')[0]
>>> daft_punk.get_albums()[:4]
[<Album: Random Access Memories>,
 <Album: TRON: Legacy Reconfigured>,
 <Album: Alive 2007>,
 <Album: Burnin'>,]
>>> random_access_memories = daft_punk.get_albums()[0]
>>> random_access_memories.get_tracks()
[<Track: Give Life Back to Music>,
 <Track: The Game of Love>,
 <Track: Giorgio by Moroder>,
 <Track: Within>,
 <Track: Instant Crush>,
 <Track: Lose Yourself to Dance>,
 <Track: Touch>,
 <Track: Get Lucky>,
 <Track: Beyond>,
 <Track: Motherboard>,
 <Track: Fragments of Time>,
 <Track: Doin' it Right>,
 <Track: Contact>]
>>> instant_crush = random_access_memories.get_tracks()[4]
>>> instant_crush.get_artist()
<Artist: Daft Punk>
>>> instant_crush.get_album()
<Album: Random Access Memories>
```

As you can see, it doesn't look like we're making API requests, but under the hood, the client is passed around and makes further API calls as needed.

You might have spotted the difference, though: attributes access are using the data from the resource which was already fetched, while calling a method on the resource does extra API requests.

#### N+1 API calls

When traversing relations, the Deezer API returns a simplified version of the objects. For example, the [album tracks](https://developers.deezer.com/api/album/tracks) have fewer fields returned that when you get [a track](https://developers.deezer.com/api/track) directly and this applies to lot of related resources: podcast episodes, artist albums, ...

To mitigate this problem and make sure the resources being returned have all the documented attributes, the client might make additional API calls to get the full version of the resources. This happens lazily, when you access an attribute of the resource which wasn't returned yet. If you try to access an attribute that doesn't exist on the resource, you'll get a `AttributeError` without extra API calls.

This might cause N+1 API calls if you're doing this in a loop:

```pycon
>>> album = client.get_album(302127)
... for track in album.get_tracks():
...     print(track.bpm)  # This will make an API call for each track
```

This is because the `bpm` field isn't returned when listing tracks of an album.

Some fields can be inferred from the resource type and ID (e.g. `Episode.link`), and in this case the client should do its best to avoid API calls. If you found some that could be avoided this way, feel free to open an issue or submit a pull request.

### Getting the raw data

At some point, you might want to get the resources exported as Python dictionaries to store them somewhere else or transform them further.

Each resource has a `as_dict()` method to export its content as dictionary:

```pycon
>>> instant_crush.as_dict()
{'id': 67238732,
 'readable': True,
 'title': 'Instant Crush',
 'title_short': 'Instant Crush',
 'title_version': '',
 'isrc': 'USQX91300105',
 'link': 'https://www.deezer.com/track/67238732',
 'duration': 337,
 'track_position': 5,
 ...}
```

## Authentication

Deezer Python itself doesn't handle the authentication & authorization, but it accepts an API token. Authentication tokens are issued for a specific user using the OAuth 2.0 protocol. The protocol states that the user needs to grant to your application the permissions you need, and this happens in the browser, on the Deezer website, which then redirect users to your application.

To integrate the OAuth flow in your application, we recommend looking at other libraries like [Python Social Auth](https://github.com/python-social-auth), which supports Deezer authentication.

Once the OAuth2 flow is complete, Deezer should give you a token which can be passed to the {class}`Client <deezer.Client>` class:

```python
client = deezer.Client(access_token='your-super-secret-token')
```

From there, you should be able to perform authenticated requests.
