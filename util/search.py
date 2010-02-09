import string

class SearchPhoneNumbers(object):
    '''
    This class extracts one or more phone numbers from a given database entry.
    '''
    def __init__(self, input_string, country_code = '509', 
                 local_min_len = 7, international_min_len = 11):
        '''
        Defaults area code and length are for Haiti
        '''
        self.__number_subdividers = '+-() ' # non-digit characters which can be used within a phone number
        self.__matches = self.__get_matches(input_string)
        self.__country_code = str(country_code)
        self.__local_min_len = local_min_len
        self.__international_min_len = international_min_len
        self.__numbers = []
        last_full_number = '' # assume that the first number is always correct
        for match in self.__matches:
            number = \
                self.to_international(match, last_full_number)
            last_full_number = number
            self.__numbers.append(number)

    def __get_matches(self, input_string):
        '''
        extracts numbers from non-phone-number text surronding them
        '''
        import string
        matches = []
        allowed = string.digits + self.__number_subdividers
        number = ''
        for character in input_string:
            if character in allowed: # collecting digits (and sudividers)
                number += character
            elif number != '': # number is finished
                # remove subdividers
                number = number.translate(None, self.__number_subdividers)
                if number != None and number != '': # if any digits collected
                    matches.append(number)
                number = ''
        return matches

    def to_international(self, number, last_full_number = ''):
        '''
        converts entries containing only one phone number to international format
        '''
        reverted = self.__matches[:]
        reverted.reverse()
        prefix = last_full_number[:-len(number)]
        if len(prefix) >=3: # assume that nobody doesn't write out a prefix of less then 3 digits
            number = self.to_international(prefix + number, last_full_number)
        if number.startswith(self.__country_code): # international
            return number            
        elif len(number) <= self.__local_min_len: # unknown format
            return self.__country_code + number
        elif len(number) <= self.__international_min_len: # national
            return number
        return number
    
    def search(self, phone):
        '''
        Returns true if phone number is within the processed numbers.
        The phone numbers may be in international or national format,
        but not in an unknown format.
        '''
        phone = self.to_international(phone)
        if phone in self.__numbers:
            return True
        return False
    def get_numbers(self):
        '''
        returns processed numbers in international format
        '''
        return self.__numbers
    def get_matches(self): 
        '''
        returns extracted and processed numbers as they are
        '''
        return self.__matches
   
# below are test cases 
db = '''
257 -3646 / 4711 
509-36-013-988 / +1-413-241-6526 (Tim Traynor)
509-262-1877, 509-262-1205, 509-262-1206
509 441 2566
509-245-1053, 509-245-0205
509-2244-7110
509-22-44-72-00
509-222-2757
509-222-3846, 509-222-7853
Dr. Theodore Crevecoeur 509-3455-7697 or 509-3872-2986 
Dr. Theodore Crevecoeur 509-3455-7697 or 509-3872-2986 
Dr. Elric Metayer 509-3461-5920 (cell) and 509-2224-3005(clinic) 
509-222-1221, 509-223-4254
509-222-5033, 509-222-0232
509-222-4242, 509-223-9988
509-274-0322
609-257-0857/509-257-6762
509-284-5260
509-286-0249d
d509-284-5260
'''
obj = SearchPhoneNumbers(db) 
assert obj.search('5092573646') == True
assert obj.search('5092574711') == True

assert obj.search('50936013988') == True
assert obj.search('14132416526') == True
assert obj.search('5092621877') == True
assert obj.search('5092621205') == True 
assert obj.search('5092621206') == True
assert obj.search('5094412566') == True
assert obj.search('5092451053') == True
assert obj.search('5092450205') == True
assert obj.search('50922447110') == True
assert obj.search('50922447200') == True
assert obj.search('5092222757') == True
assert obj.search('5092223846') == True
assert obj.search('5092227853') == True
assert obj.search('50934557697') == True
assert obj.search('50938722986') == True
assert obj.search('50934557697') == True
assert obj.search('50938722986') == True

assert obj.search('50934615920') == True
assert obj.search('50922243005') == True
assert obj.search('5092221221') == True
assert obj.search('5092234254') == True
assert obj.search('5092225033') == True
assert obj.search('5092220232') == True
assert obj.search('5092224242') == True
assert obj.search('5092239988') == True
assert obj.search('5092740322') == True
assert obj.search('6092570857') == True
assert obj.search('5092576762') == True
assert obj.search('5092845260') == True
assert obj.search('5092860249') == True
assert obj.search('5092845260') == True

assert obj.search('5092845260464') == False

print "extracted matches = %s" % obj.get_matches()
print "converted numbers = %s" % obj.get_numbers()
print 'OK'
