import json
import dawa_api_client

def main():

    try:
        dawa = dawa_api_client.DAWA()

        print("Results for a single address:")
        result = dawa.adgangsadresser(struktur="mini", vejnavn="Christian X's Vej", husnr="39", postnr="6100")
        print(json.dumps(result, indent=2))

        print("-" * 80 + "\r\n")
        for r in result:
            print(f'{r.get("vejnavn")} {r.get("husnr"):>3}, {r.get("postnr")} {r.get("postnrnavn")}'
                  f' ({r.get("x")}, {r.get("y")})')
        print(f"Results: {len(result)}")
 

    except dawa_api_client.ApiError as error:
        print("The request failed:")
        print(f"{error.type}, {error.title}")
        for detail in error.details:
            print(f"Parameter: {detail[0]:20} => {detail[1]}")
    except Exception as error:
        raise error


if __name__ == "__main__":
    main()
