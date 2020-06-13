# Usage

## First steps

To start calling the API, you first need to instantiate a
{class}`Client <deezer.client.Client>`:

```python
>>> client = deezer.Client()
```

From there, you can search for some terms:

```python
>>> client.search('Daft Punk')
[<Track: Daft Punk>,
<Track: Daft Punk>,
<Track: One More Time>,
<Track: Around the World>,
<Track: Harder, Better, Faster, Stronger>,
<Track: Da Funk>,
<Track: Veridis Quo>,
<Track: Aerodynamic>,
<Track: Something About Us>,
<Track: Giorgio by Moroder>,
<Track: Give Life Back to Music>,
<Track: Within>,
<Track: Daft Punk>,
<Track: Digital Love>,
<Track: Nightvision>,
<Track: The Game of Love>,
<Track: Around the World / Harder, Better, Faster, Stronger>,
<Track: Beyond>,
<Track: I Feel It Coming>,
<Track: Contact>,
<Track: Voyager>,
<Track: One More Time (Short Radio Edit)>,
<Track: Starboy>,
<Track: Face to Face>,
<Track: Motherboard>]
```

The above returned a lot of tracks. If you wanted to search for artists
instead, you may do so by specifying the `relation` argument:

```python
>>> client.search('Daft Punk', relation='artist')
[<Artist: Daft Punk>,
 <Artist: Daft Punk - Stardust>,
 <Artist: Tribute to Daft Punk>,
 <Artist: Daft Punk feat. Pharrell Williams and Nile Rodgers>,
 <Artist: Made famous by Daft Punk>,
 <Artist: Daft Punk's Karaoke Band>]
```

The `relation` parameter accepts any resource name as value. The name of
a resource is a string with the class name in lowercase. This is
explained in a following section.

## Main concepts

As we just seen above, the entry point is the
{class}`Client <deezer.client.Client>` class,
which gives access to a number of methods. The methods are attempting to
map to the REST API endpoints from Deezer.

You may have noticed from the above examples, but depending on the
endpoint that is being called, the methods will return various type of
resources. All the resources are listed in the
{ref}`resources reference page <resources-reference>`.

## More examples

### Getting a field about a resource

When you ge a resource, you have access to all the fields that are in
the REST API response. For example, all the fields presented in the
documentation for [the track
object](https://developers.deezer.com/api/track) are accessible as
attribute on the {class}`Track <deezer.resources.Track>` resource:

```python
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

As well as giving access to its own attributes, a resource also gives
access to other related resources.

For example, when you get an {class}`Artist <deezer.resources.Artist>`, you
may call one of the methods documented to get the artist's albums, then
from an {class}`Album <deezer.resources.Album>` get its tracks, and from a
{class}`Track <deezer.resources.Track>` you may go back to the
{class}`Album <deezer.resources.Album>` or the
{class}`Artist <deezer.resources.Artist>`.

Let\'s try from the initial example:

```python
>>> daft_punk = client.search('Daft Punk', relation='artist')[0]
>>> daft_punk.get_albums()
[<Album: Random Access Memories>,
 <Album: TRON: Legacy Reconfigured>,
 <Album: Alive 2007>,
 <Album: Burnin'>,...]
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

As you can see, it doesn\'t look like we\'re making API requests, but
under the hood, the client is passed around and makes further API calls
as needed.

You can tell the difference, though: attributes access are using the
data from the resource which was already fetched, while calling a method
on the resource does extra API requests.

### Getting the raw data

At some point, you might want to get the resources exported as Python
dictionaries to store them somewhere else or transform them further.

Each resource has a `asdict()` method to export its content as
dictionary:

```python
>>> instant_crush.asdict()
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

The `deezer-python` library doesn't handle the authentication process,
but it accepting an API token, which one can obtain using other
libraries.

Obtaining a authentication token is better done client side, for example
with [Python Social Auth](https://github.com/python-social-auth), which
supports Deezer authentication.

Once the OAuth2 flow is complete, Deezer should give you a token which
can be passed to the {class}`Client <deezer.client.Client>` class:

```python
client = deezer.Client(access_token='your-super-secret-token')
```

From there, you should be able to perform authenticated requests.
