def kushel(age):
    if age < 15:
        print('he studied at st.John Keats')
    elif 16<= age < 18:
        print('he was at MES college')


def gender(sex='unknown'):
    if sex is'm':
       sex = 'male'
    elif sex is 'f':
        sex = 'female'
    print(sex)
gender()
gender('m')
