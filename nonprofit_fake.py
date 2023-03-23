#!/usr/bin/python3
from faker import Faker
from faker.providers import DynamicProvider

category_provider = DynamicProvider(
     provider_name="categories",
     elements=["Animals", "Disaster Relief", "Education",
               "Environment", "Social Justice & Equity", "Health",
               "Life Skils", "Poverty", "Senior Services"],
)



fake = Faker()
# then add new provider to faker instance
fake.add_provider(category_provider)

def create_category(n):
    from givetime import create_app
    
    app = create_app()

    app.app_context().push()

    from givetime.modified_model import Category
    for _ in range(n):

        name = fake.unique.categories()
        Category.create(name=name)


def create_nonprofits(n):
    from givetime import create_app
    
    app = create_app()

    app.app_context().push()

    from givetime.modified_model import Nonprofit
    for _ in range(n):
        
        name = fake.company()
        password_hash = fake.password()
        email = fake.unique.email()
        description = fake.paragraph()
        website = fake.url()


        Nonprofit.create(name=name, email=email,
                         password=password_hash, description=description,
                         website=website)


def create_opportunity(n):

    from givetime import create_app

    app = create_app()

    app.app_context().push()

    from givetime.modified_model import Opportunity
    for _ in range(n):

        title = "Save a child"
        description = fake.paragraph()
        location = "Lagos"


        Opportunity.create(title=title, description=description, location=location,
                           nonprofit_id=1, category_id=1, status='open')


print("Populating database...")
create_opportunity(1)
print("Populating complete")

