from faker import Faker
import random

fake = Faker()

#jumlah = int(input("[*] Mau berapa: "))
#for result in range(jumlah):
print(f'Name: {fake.name()}')
print(f'No hp: {fake.msisdn()}')
print(f'address: {fake.address()}')
print(f'address2: {fake.address()}')
print(f'city: {fake.city()}')
print(f'city: {fake.city()}')
print(f'Zip: {random.randint(1000,9999)}')
print('\n')