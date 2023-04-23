def validate_iban(iban: str) -> (bool, str):
    """
    An IBAN-compliant account number consists of:
    * A two-letter country code taken from the ISO 3166-1 standard
      (e.g., FR for France, GB for Great Britain, DE for Germany,
      and so on)
    * Two check digits used to perform the validity checks – fast and
      simple, but not fully reliable, tests, showing whether a number
      is invalid (distorted by a typo) or seems to be good;
    * the actual account number (up to 30 alphanumeric characters –
      the length of that part depends on the country)    
    """

    # The number can contain spaces as they significantly
    # iporve number readability... but remove them immediately
    iban = iban.replace(' ','')
    
    if not iban.isalnum():
        return False, "You have entered invalid characters."
    elif len(iban) < 15: # shortest variant used in Norway
        return False, "IBAN entered is too short."
    elif len(iban) > 31: # longest variant used in Malta
        return False, "IBAN entered is too long."
    else:
        # Move the 4 initial characters to the numbers's end,
        # and convert all letters to upper case
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                # Replace each letter in the string with 2-digts,
                # thereby expanding the string, where A = 10, B = 11...
                # Z = 35
                iban2 += str(10 + ord(ch) - ord('A'))
        iban = int(iban2)
        if iban % 97 == 1:
            return True, "IBAN entered is valid."
        else:
            return False, "IBAN entered is invalid."

if __name__ == "__main__":
    assert validate_iban("GB72 HBZU 7006 7212 1253 00")[0] == True
    assert validate_iban("FR76 30003 03620 00020216907 50")[0] == True
    assert validate_iban("DE02100100100152517108")[0] == True
    assert validate_iban("GB63 HBZU 7006 7212 1253 00")[0] == False
    assert validate_iban("FR65 30003 03620 00020216907 50")[0] == False
    assert validate_iban("DE13100100100152517108")[0] == False
