def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Putkin', name='Vovka', year='1956', city='Moscow', email='vovaPut02@mail.ru',
              telephone='8-800-555-35-55'))