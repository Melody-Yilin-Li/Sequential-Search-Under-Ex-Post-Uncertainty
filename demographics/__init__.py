from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    last_name = models.StringField(label='What is your last name?')
    first_name = models.StringField(label='What is your first name?')
    ucscID = models.IntegerField(label='What is your UCSC student ID number', min=0000000, max=9999999)
    email = models.StringField(label='What is your UCSC email address?')
    participantID = models.StringField(label='What is your participant ID (Zoom Username)?')
    venmoID = models.StringField(label='What is your Venmo ID?')
    searchcomment = models.LongStringField(label='Given a searched list, which item will you purchase in the search task?')
    stopcomment = models.LongStringField(label='When did you decide to stop searching in the search task?')
    suggest = models.LongStringField(label='Do you have any other suggestion on the experiment?')


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['last_name', 'first_name', 'ucscID', 'email', 'participantID', 'venmoID', 'searchcomment', 'stopcomment', 'suggest']


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(player=player)


page_sequence = [Demographics, Results]
