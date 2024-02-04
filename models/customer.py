class Customer:
    def __init__(self, first_name: str, last_name: str, phone_number: str):
        if (len(first_name) < 2 or len(first_name) > 15) or not first_name.isalpha():
            raise ValueError(f'!!! ERROR FIRST NAME: "{first_name}"!!!\n'
                             f'   -First name can contains ONLY letters and length has to be 2-15 symbols!')

        if (len(last_name) < 2 or len(last_name) > 15) or not last_name.isalpha():
            raise ValueError(f'!!! ERROR LAST NAME: "{last_name}"!!!\n'
                             f'   -Last name can contains ONLY letters and length has to be 2-15 symbols!')

        if not (len(phone_number) == 10) or not phone_number.isdigit():
            raise ValueError(
                f'!!! ERROR PHONE NUMBER: "{phone_number}"!!!\n'
                f'   -Phone number can contains ONLY digits and length has to be 10 symbols!')

        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return self._phone_number

    def __str__(self):
        return f'---Contact info: ---\n' \
               f'   #First Name: {self.first_name}\n' \
               f'   #Last Name: {self.last_name}\n' \
               f'   #Phone Number: {self.phone_number}'


