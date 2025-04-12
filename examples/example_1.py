import sys
import dawa_api as dawa


def main():
    try:
        client = dawa.Client()

        print("Results for a complete postalcode:")
        query = dawa.AdresseQuery(postnr="1218")
        result = client.adgangsadresser_mini(query)
        for r in result:
            print(f"{r.vejnavn} {r.husnr:>3}, {r.postnr} {r.postnrnavn} ({r.x}, {r.y})")
        print(f"Results: {len(result)}")
        print("-" * 25 + "\r\n")

        print("Results for a single address:")
        query = dawa.AdresseQuery(
            vejnavn="Christian X's Vej", husnr="39", postnr="6100"
        )
        result = client.adgangsadresser_mini(query)
        for r in result:
            print(f"{r.vejnavn} {r.husnr:>3}, {r.postnr} {r.postnrnavn} ({r.x}, {r.y})")
        print(f"Results: {len(result)}")
        print("-" * 25 + "\r\n")

        print("Result of a invalid request:")
        query = dawa.AdresseQuery(vejpunkt_id="2", adgangspunktid="0")
        result = client.adgangsadresser_mini(query)
        print(result)

    except dawa.ApiError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)
