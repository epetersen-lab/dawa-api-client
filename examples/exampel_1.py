import dawa_api
from dawa_api import AdresseQuery


def main():
    try:
        dawa = dawa_api.DAWA()

        print("Results for a complete postalcode:")
        query = AdresseQuery(postnr="1218")
        result = dawa.adgangsadresser_mini(query)
        for r in result:
            print(
                f"{r.vejnavn} {r.husnr:>3}, {r.postnr} {r.postnrnavn}"
                f" ({r.x}, {r.y})"
            )
        print(f"Results: {len(result)}")
        print("-" * 25 + "\r\n")

        print("Results for a single address:")
        query = AdresseQuery(vejnavn="Christians X's Vej", husnr="39", postnr="6100")
        result = dawa.adgangsadresser_mini(query)
        for r in result:
            print(
                f"{r.vejnavn} {r.husnr:>3}, {r.postnr} {r.postnrnavn}"
                f" ({r.x}, {r.y})"
            )
        print(f"Results: {len(result)}")
        print("-" * 25 + "\r\n")

        print("Result of a invalid request:")
        query = AdresseQuery(vejpunkt_id="2", adgangspunktid="0")
        result = dawa.adgangsadresser_mini(query)
        print(result)

    except dawa_api.ApiError as error:
        print("The request failed:")
        print(f"{error.type}, {error.title}")
        print(f"{error.details}")
    except Exception as error:
        raise error


if __name__ == "__main__":
    main()
