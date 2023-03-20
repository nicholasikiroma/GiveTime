from faker impoirt Faker
from faker.providers import address, company, phone_number
from givetime.models import Nonprofit

fake= Faker()
fake.add_provider(address, company, phone_number)


def create_fake(n):

    for _ in range(n):
        name = fake.company()
        address = fake.street_address()
        city = fake.city()
        phone = fake.phone_number()
        state = "Lagos"



if __name__ == "__main__":


