with open("country_info.txt") as country_file:
    country_file.readline()
    countryexist = input("Please enter name or code of country: ")
    for row in country_file:
        data = row.strip("\n").split("|")
        country,capital,code,code3,dialing,timezone,currency = data
        country_dic = {"name":country,"capital":capital,"country_code":code}

        if countryexist == country_dic.get("name") or countryexist == country_dic.get("country_code"):
            print("The capital is", country_dic.get("capital"))
