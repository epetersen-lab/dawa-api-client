import json
import dawa_api as dawa


def main():
    try:
        client = dawa.Client()

        print("Results for a single address:")
        query = dawa.AdresseQuery(
            vejnavn="Christian X's Vej", husnr="39", postnr="6100"
        )
        result = client.adgangsadresser_mini(query)
        print(result)

        print("-" * 80 + "\r\n")
        for r in result:
            print(
                f"{r.vejnavn} {r.husnr:>3}, {r.postnr} {r.postnrnavn}"
                f" ({r.x}, {r.y})"
            )
        print(f"Results: {len(result)}")

    except dawa.ApiError as error:
        print("The request failed:")
        print(f"{error.type}, {error.title}")
        print(f"{error.details}")
    except Exception as error:
        raise error


if __name__ == "__main__":
    main()
