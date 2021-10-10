import phonenumbers

number2 = input('Ölkə kodu ilə nömrəni daxil edin: ')#"+994773849424"

from phonenumbers import geocoder
number = phonenumbers.parse(number2)
print(number)
print(geocoder.description_for_number(number,'az'))

from phonenumbers import carrier

number=phonenumbers.parse(number2)
print(carrier.name_for_number(number,'az'))

from phonenumbers import timezone
number = phonenumbers.parse("+994773849424", "az")
print(timezone.time_zones_for_number(number))


