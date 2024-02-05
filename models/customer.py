class Customer:

    def __init__(self, first_name: str, last_name: str, email: str):
        if (len(first_name) < 2 or len(first_name) > 15) or not first_name.isalpha():
            raise ValueError(f'!!! ERROR FIRST NAME: "{first_name}"!!!\n'
                             f'   -First name can contain ONLY letters and length has to be 2-15 symbols!')

        if (len(last_name) < 2 or len(last_name) > 15) or not last_name.isalpha():
            raise ValueError(f'!!! ERROR LAST NAME: "{last_name}"!!!\n'
                             f'   -Last name can contain ONLY letters and length has to be 2-15 symbols!')

        if (len(email) < 5 or len(email) > 30) or ('@' not in email) or ('.' not in email):
            raise ValueError(f'!!! ERROR EMAIL ADDRESS: "{email}"!!!\n'
                             f'   -Email address has to be between 5-30 symbols and it has to contain " @ . " symbols!')

        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    def __str__(self):
        string = f'#First Name: {self.first_name}\n' \
                 f'  #Last Name: {self.last_name}\n' \
                 f'  #Email: {self.email}'
        return string
