def create_response_label_dict():
    '''
    Creates dictionary with labels for each response in each question

    Returns
    -------
    labels : dictionary
        Dictionary where key is a topic name or group, and then key is another
        dictionary where key is numeric answer and value is the label.
    '''
    # Define the labels to use for different columns
    labels = {
        'symbol': {
            1: 'Happy',
            2: 'Ok',
            3: 'Sad'
        },
        'gender': {
            0: 'Male',
            1: 'Female'
        },
        'year_group': {
            7: 'Year 7',
            8: 'Year 8',
            9: 'Year 9',
            10: 'Year 10',
            11: 'Year 11'
        },
        'fsm': {
            0: 'Non-FSM',
            1: 'FSM'
        },
        'sen': {
            0: 'Non-SEN',
            1: 'SEN'
        },
        'ethnicity': {
            1: 'Ethnic minority',
            2: 'White British'
        },
        'english_additional': {
            0: 'No',
            1: 'Yes'
        },
        'school': {
            1: 'School A',
            2: 'School B'
        }
    }

    def add_keys(keys, value, dictionary=labels):
        '''
        Add multiple keys with the same value to the dictionary
        Inputs:
        keys: Array with the keys
        value: String which is the value for all the keys
        dictionary: Dictionary to add the keys and values to, default is labels
        '''
        dictionary.update(dict.fromkeys(keys, labels[value]))

    # Add values for the keys below, so each key has the same set of values
    # (Rather than repeatedly defining them all above)
    add_keys(['symbol_family', 'symbol_home', 'symbol_friends',
              'symbol_choice', 'symbol_things', 'symbol_health',
              'symbol_future', 'symbol_school', 'symbol_free',
              'symbol_life'], 'symbol')

    return labels
