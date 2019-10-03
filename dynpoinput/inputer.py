

class Inputer:
    validation_type = {
        'string': str,
        'integer': int,
        'float': float,
        'boolean': bool
    } 

    def __init__(self, **config):
        """."""
        self.provided_data = None
        self.skip = None
        self.error_msg = None
        self.instructions = '[enter] to skip / [""] for empty value'
        self.config = self._assign_config(config)

    def _assign_config(self, config, expected=None):
        """."""

        # Enhance configuration adding key to determine:
        # - size of data;
        # - allow space or not;
        # - add custom validator;
        # - Add custom printer;
        # - add logger;
        # - Confirm data entered;
        # - confirm upon skip;


        # Add configurations for input.
        if expected is None:
            expected = {
                'infinit': False,
                'valid_attempts': 5,
                'msg': '',
                'required': True,
                'data_type': 'string'
            }

        for key, value in expected.items():
            if key in config:
                expected[key] = config[key]
        return expected

    def _valid(self, data, data_type):
        """."""
        try:
            valid_data = self.validation_type[data_type](data)
            return True
        except ValueError as error:
            return False

    def _treat_special_cases(self):
        """."""
        if self.provided_data == '':
            self.skip = True

        elif self.provided_data == '""':
            self.provided_data = ''

        if self.config['infinit']:
            self.config['valid_attempts'] += 1

    def _test_conditions(self, required):
        """."""
        # If value is required and tried to skip, we are not satisfied
        if required and self.skip:
            self.error_msg = str('Error: This value canno\'t be skipped '
                                 'as it\'s required.')
            return False
        else:
            # If it was not skipted then let's test the validity.
            if not self.skip:
                # If data is valid, then we are satisfied.
                if self._valid(self.provided_data, self.config['data_type']):
                    return True
                # If data is not valid, we are not satisfied.
                else:
                    self.error_msg = str('Error: The data provided is invalid, '
                                     'incompatible with the expected type'
                                     ' [%s].' % self.config['data_type'])
                    return False
            # If it was skipped and its not required, we are satisfied.
            else:
                return True

    def _communicate(self):
        print(self.error_msg)

    def get_input(self, **config):
        """."""
        self.config = self._assign_config(config, expected=self.config)
        satisfied = False
        attempts = 0

        while satisfied == False and attempts < self.config['valid_attempts']:
            self.skip = False
            attempts += 1

            # Get the necesary data.
            self.provided_data = input(self.config['msg'])

            # Treat special cases, skip and empty value.
            self._treat_special_cases()

            # Test all conditions, it cannot be required and skiped, or
            # invalid
            satisfied = self._test_conditions(self.config['required'])

            if not satisfied:
                self._communicate()

        if self.config['required'] and self.skip:
            raise Exception('It cannot be required and have no data!')

        # Assemble proper result
        result = {
            'satisfied': satisfied,
            'skiped': self.skip,
            'data': self.provided_data
        }

        return result


