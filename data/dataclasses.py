__author__ = 'aberes'
from data.random_functions import *


class OrgInformationData:
    Your_Url = None
    Name = None
    Zip_Code = None
    Phone = None
    Party = None
    Short_Description = None
    Level = None
    SignUpButton = None

    class LevelData:
        LEVEL = "County / City - display in searches of your county and city"
        STATEWIDE = "Statewide - display in searches of your state"
        NATIONWIDE = "Nationwide - display in any search"

    class PartyData:
        NO_PARTY = "No Party"
        DEMOCRATIC_PARTY = "Democratic Party"
        REPUBLICAN_PARTY = "Republican Party"
        INDEPENDENT = "Independent"
        AMERICAN_INDEPENDENT_PARTY = "American Independent Party"
        AMERICAN_PARTY = "American Party"
        CITIZENS_PARTY = "Citizens Party"
        CONSERVATIVE_PARTY = "Conservative Party"
        CONSTITUTIONAL = "Constitutional"
        DEMOCRAT_FARM_LABOR_PARTY = "Democrat Farm Labor Party"
        DEMOCRAT_NONPARTISAN_LEAGUE = "Democrat Nonpartisan League"
        GREEN_PARTY = "Green Party"
        INDEPENDENT_AMERICAN_PARTY = "Independent American Party"
        INDEPENDENT_CITIZENS_MOVEMENT = "Independent Citizens Movement"
        LABOR = "Labor"
        LIBERTARIAN = "Libertarian"
        NATURAL_LAW_PARTY = "Natural Law Party"
        NEW_PROGRESSIVE_PARTY = "New Progressive Party"
        NON_PARTISAN = "Non-Partisan"
        POPULAR_DEMOCRATIC_PARTY = "Popular Democratic Party"
        PROGRESSIVE_PARTY = "Progressive Party"
        PUERTO_RICAN_INDEPENDENCE_PARTY = "Puerto Rican Independence Party"
        REFORM_PARTY = "Reform Party"
        RIGHT_TO_LIFE_PARTY = "Right to Life Party"
        SOCIALIST_WORKERS_PARTY = "Socialist Workers Party"
        TAXPAYERS_PARTY = "Taxpayers Party"
        OTHER = "Other"

    def set_random_data(self):
        self.Your_Url = randstring(4) + "@gmail.com"
        self.Name = randstring(5)
        self.Zip_Code = "10160"
        self.Phone = "1234567890"
        self.Party = OrgInformationData.PartyData.AMERICAN_PARTY
        self.Short_Description = "Some Description"
        self.Level = OrgInformationData.LevelData.NATIONWIDE
        self.SignUpButton = None
