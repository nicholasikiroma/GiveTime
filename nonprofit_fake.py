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

category_provider = DynamicProvider(
    provider_name="categories",
    elements=["Education", "Community Development", "Hunger/Food Security", "Domestic Violence Prevention",
              "Housing/Homelessness", "Arts/Education", "Healthcare/Access", "Youth Development",
              "Environment/Conservation", "Mental Health", "Diversity/Inclusion",
              "Animal Welfare"
              ],
)

location_provider = DynamicProvider(
    provider_name="opp_location",
    elements=["Lagos", "Port Harcourt", "Abuja", "Uyo",
              "Kaduna", "Yola", "Enugu"
              ],
)


fake = Faker()
# then add new provider to faker instance
fake.add_provider(location_provider)


def create_category(n):
    from givetime import create_app

    app = create_app()

    app.app_context().push()

    from givetime.modified_model import Category
    for _ in range(n):

        name = fake.unique.categories()
        Category.create(name=name)
        print("Done...")


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


def create_opportunity():

    from givetime import create_app

    app = create_app()

    app.app_context().push()

    from givetime.modified_model import Opportunity

    opportunities = [
        {
            'nonprofit_id': "fc04a7ad-1576-4129-a8f0-06189683931e",
            'category_id': "3c0ecced-e9b1-4765-a1f0-9c80f41428e5",
            'location': fake.opp_location(),
            'title': "Eco-Village",
            'description': "GreenThumb's Eco-Village project aims to create sustainable living spaces in urban areas, promoting eco-friendly living and reducing carbon footprints. The project involves constructing eco-friendly buildings, providing community gardens, and educating residents on sustainable living practices.",
            'status': 'open'
        },
        {
            'nonprofit_id': "cf01b481-97f0-4e2f-9577-7642ae93a54d",
            'category_id': "47431e26-b784-4ab0-9604-b843ca056fa6",
            'location': fake.opp_location(),
            'title': "Mobile Medical Clinic",
            'description': "HealthFirst's Mobile Medical Clinic project aims to provide healthcare services to underserved communities by bringing medical professionals and resources to them. The project involves equipping and operating mobile clinics to offer services such as medical consultations, vaccinations, and health screenings.",
            'status': 'open'
        },
        {
            'nonprofit_id': "5e5011c8-a9ba-4c79-930a-315a40d3fdb3",
            'category_id': "a7e97fd4-5707-41eb-bedd-32f4884b226a",
            'location': fake.opp_location(),
            'title': "Wildlife Rehabilitation",
            'description': "Animal Allies' Wildlife Rehabilitation project aims to rescue, rehabilitate, and release injured and orphaned wild animals back into their natural habitats. The project involves setting up rehabilitation centers staffed by trained professionals to provide medical care and support for wildlife in need.",
            'status': 'open'
        },
        {
            'location': fake.opp_location(),
            "title": "Career Training Program",
            "category_id": "2491cb23-0c3c-4e88-ad84-72a9cc16d805",
            "description": "YouthBuilders' Career Training Program project aims to provide young people with the skills and training they need to succeed in the workforce. The project involves offering vocational training and mentorship programs to help youth gain practical skills, experience, and confidence.",
            "nonprofit_id": "81a312a2-6c42-435b-a879-5e39544c4137",
            'status': 'open'
        },
        {
            'location': fake.opp_location(),
            "title": "Homeless Shelter Expansion",
            "category_id": "3c0ecced-e9b1-4765-a1f0-9c80f41428e5",
            "description": "HomeSafe's Homeless Shelter Expansion project aims to expand the organization's shelter facilities to provide more safe and supportive housing for homeless individuals and families. The project involves renovating existing facilities and constructing new buildings to accommodate more people.",
            "nonprofit_id": "287374b1-d12f-491d-a515-407559b50762",
            'status': 'open'
        },
        {
            'location': fake.opp_location(),
            "title": "Community Art Project",
            "category_id": "a1cf7136-dd13-497d-8a6c-fbce804f6563",
            "description": "ArtReach's Community Art Project aims to engage and inspire local communities through public art installations. The project involves organizing art workshops, recruiting artists to create public art pieces, and collaborating with local organizations to bring art to public spaces.",
            "nonprofit_id": "00b21443-c78a-4112-b18a-8151193dcc42",
            'status': 'open'
        },
        {"location": fake.opp_location(),
         "title": "Domestic Violence Counseling Program",
         "category_id": "ee9140a1-cf0f-4ec1-9657-9fcfd60ff27d",
         "description": "HopeWorks' Domestic Violence Counseling Program project aims to provide counseling and support services to survivors of domestic violence. The project involves offering individual and group counseling, safety planning, and legal advocacy to help survivors heal and rebuild their lives.",
         "nonprofit_id": "18bf9380-4588-4801-81eb-ef38a83e61d4",
         'status': 'open'},

        {"location": fake.opp_location(),
         "title": "Community Garden Project",
         "category_id": "e58452b3-fda5-4fe3-97a4-f86970cfa123",
         "description": "FoodForAll's Community Garden Project aims to increase access to fresh, healthy food for low-income communities by creating community gardens. The project involves setting up and maintaining community gardens, providing gardening education, and distributing the harvest to those in need.",
         "nonprofit_id": "11d3f5ed-a49d-4b39-acae-48b5b4750ef5",
         'status': 'open'},

        {"location": fake.opp_location(),
         "title": "Digital Literacy Program",
         "category_id": "98f22c93-ab2c-4b86-8186-f0d95b490f4e",
         "description": "TechBridge's Digital Literacy Program project aims to bridge the digital divide by providing technology education and access to underserved communities. The project involves offering computer and internet access, technology training, and digital skills workshops to help individuals and families thrive in the digital age.",
         "nonprofit_id": "9555ba31-f5ef-43b9-a587-64d3cb9cc36c",
         'status': 'open'},

        {
            "location": fake.opp_location(),
            "title": "Language Exchange Program",
            "category_id": "f7f497c4-3218-4070-98bf-9e84efb034ea",
            "description": "CultureConnect's Language Exchange Program aims to promote cross-cultural understanding and language learning by connecting people from different backgrounds. The project involves pairing language learners with native speakers for conversation practice, cultural exchange events, and language classes.",
            "nonprofit_id": "be947e31-7da7-4b18-ad38-0cf8dc529bb9",
            'status': 'open'},
    ]

    for opportunity in opportunities:
        Opportunity.create(
            title=opportunity['title'],
            description=opportunity['description'],
            location=opportunity['location'],
            nonprofit_id=opportunity['nonprofit_id'],
            category_id=opportunity['category_id'],
            status=opportunity['status']
        )
        print("Done...")
    
def create_relations():
    from givetime import create_app

    app = create_app()

    app.app_context().push()

    # Get all Opportunity instances from the database
    from givetime.modified_model import OpportunityCategory

    opp_cat = [
        {'opp_id':"65537937-4c99-4726-9af3-525859d7d723",
         'cat_id': "22898d10-5c71-4557-97a2-51d5c923251b"},

         {'opp_id':"b72e194b-1b4c-4493-afef-6d0dca8751da",
         'cat_id': "47431e26-b784-4ab0-9604-b843ca056fa6"},

         {'opp_id':"574906be-cf75-4aa1-97ea-ab77e40b258f",
         'cat_id': "a7e97fd4-5707-41eb-bedd-32f4884b226a"},

         {'opp_id':"c521df16-b301-442b-98f4-e243e1dd1f24",
         'cat_id': "2491cb23-0c3c-4e88-ad84-72a9cc16d805"},

         {'opp_id': "2a505e88-84b9-45a6-a287-0c0fefa0e76d",
         'cat_id': "3c0ecced-e9b1-4765-a1f0-9c80f41428e5"},

         {'opp_id':"b4d2a734-2aa7-4599-b31c-8095f16988c6",
         'cat_id': "a1cf7136-dd13-497d-8a6c-fbce804f6563"},

         {'opp_id':"2df533f6-8028-4719-830e-d1af66ef1aa4",
         'cat_id': "ee9140a1-cf0f-4ec1-9657-9fcfd60ff27d"},

         {'opp_id':"4f55400a-aeee-466d-bbb2-312743762627",
         'cat_id': "e58452b3-fda5-4fe3-97a4-f86970cfa123"},

         {'opp_id':"2c866b61-a2d0-44cc-afa5-0817d114cc74",
         'cat_id': "98f22c93-ab2c-4b86-8186-f0d95b490f4e"},

         {'opp_id':"8d1c0609-3255-400c-a661-dbec1854600a",
         'cat_id': "f7f497c4-3218-4070-98bf-9e84efb034ea"},
    ]

    for opp in opp_cat:
        OpportunityCategory.create(opp_id=opp["opp_id"],
                                   category_id=opp["cat_id"])
        print('DONE...')



print("Populating database...")
print()
create_relations()
print()
print("Populating complete")
