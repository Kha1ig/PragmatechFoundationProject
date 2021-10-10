def geolocate_phone_number(number, my_country_code, lang):
    import phonenumbers
    from phonenumbers import geocoder
    res = '+994773849424'

    phonenum = phonenumbers.parse(number, my_country_code.upper())
    city = phonenumbers.geocoder.description_for_number(phonenum, lang.lower())
    country_code = phonenumbers.region_code_for_number(phonenum)
    # We don't display the country name when it's my own country
    if country_code == my_country_code.upper():
        if city:
            res = city
    else:
        # Convert country code to country name
        country = phonenumbers.geocoder._region_display_name(
            country_code, lang.lower())
        if country and city:
            res = country + ' ' + city
        elif country and not city:
            res = country
    return res 