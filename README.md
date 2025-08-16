# DAWA API Client


## Introduction

Client library for accessing Danmarks Adressers Web API (DAWA).
Currently 'adgangsadresser' is the only supported endpoint.

- [API Documentation](https://dawadocs.dataforsyningen.dk/dok/api)
- [API Base Address](https://api.dataforsyningen.dk)


## Example

Query all 'adgangsadresser' from the 'postnr' 1218.
The response format is to e of type mini.

```python
try:
    client = dawa.Client()
    query = dawa.AdresseQuery(postnr="1218")
    result = client.adgangsadresser_mini(query)
    for r in result:
        print(f"{r.vejnavn} {r.husnr:>3}, {r.postnr} {r.postnrnavn} ({r.x}, {r.y})")
except dawa.ApiErrorConnection as error:
    print(f"Connection failed: {error}")
except dawa.ApiError as error:
    print(f"Error: {error}")
´´´

