#!/usr/bin/python3
from faker import Faker
from faker.providers import DynamicProvider

nonprofit_provider = DynamicProvider(
     provider_name="ngo_name",
     elements=["GreenThumb", "HealthFirst", "Animal Allies", "YouthBuilders",
               "ArtReach", "HomeSafe", "HopeWorks", "FoodForAll", "TechBridge",
               "CultureConnect", "Minful Matters", "CommunityBuilders", "Ocean Guardians",
               "Brighter Futures", "HealthLink", "Creative Impact", "HomeFront", "SafeHarbor",
               "FoodForThought", "LiteracyLink"],
)



fake = Faker()
# then add new provider to faker instance
fake.add_provider(nonprofit_provider)

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
        
        name = fake.unique.ngo_name()
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
create_nonprofits(19)
print("Populating complete")

