from uuid import uuid4

from behave import fixture
from faker import Faker


@fixture
def eyb_random_data(context):
    fake = Faker()
    data = {
        'email_address': f'automated-ui-test+{uuid4()}@mail.ci.uktrade.digital',
        'password': f'A1!{uuid4()}',
        'company_name': fake.company(),
        'partial_company_headquarters_location': 'ita',
        'user_full_name': fake.name(),
        'user_role': fake.job(),
        'company_website': f'www.{fake.domain_name()}',
        'telephone_number': fake.phone_number(),
    }

    setattr(context, 'user_data', data)
