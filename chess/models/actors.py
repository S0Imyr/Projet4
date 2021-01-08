from chess.utils.conversion import list_to_str_space


ID_WIDTH = 8


class Actor:
    """
    An actor is the identity of player of the different tournaments
    """
    last_actor_id = "0"*ID_WIDTH

    def __init__(self, last_name, first_name, birthdate, gender, rank):
        if Actor.last_actor_id.lstrip('0') == "":
            Actor.last_actor_id = str(1)
        else:
            Actor.last_actor_id = str(int(Actor.last_actor_id.lstrip('0')) + 1)
        self.actor_id = \
            (ID_WIDTH - len(Actor.last_actor_id.lstrip('0'))) * "0" \
            + Actor.last_actor_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.tournaments = []

    def __repr__(self):
        return f"Personne: Nom: {self.last_name}, Prénom: {self.first_name} \n" \
               f"Identifiant: {self.actor_id}\n" \
               f"Classement: {self.rank} \n"

    def modify_rank(self, rank):
        self.rank = rank

    def actor_to_dict(self):
        """
        convert the actor into a dictionnary
        :return:
        """
        string_attributes = ['actor_id', 'last_name', 'first_name', 'gender', 'rank']
        serialized_actor = {}
        for attribute in string_attributes:
            serialized_actor[attribute] = self.__getattribute__(attribute)
        # no_string_attributes = ['birthdate', 'tournaments']
        serialized_actor['birthdate'] = str(self.birthdate)
        serialized_actor['tournaments'] = list_to_str_space(self.tournaments)
        return serialized_actor


    def dict_to_actor(self, dict):
        """
        convert a dictionnary into actor
        :return:
        """
        pass


class Player:
    """
    A player mean a player in a specific tournament
    """
    def __init__(self, actor, tournament_id, player_id):
        self.actor = actor
        self.name = self.actor.first_name + " " + self.actor.last_name
        self.tournament_id = tournament_id
        self.player_id = player_id
        self.rank = actor.rank
        self.ranking = 0
        self.points = 0
        self.place = 0
        self.opponents = []

    def __repr__(self):
        return f"Nom: {self.name} \n" \
               f"Identifiant: {self.actor.actor_id}\n" \
               f"Classement: {self.rank}\n" \
               f"Dans le tournoi {self.tournament_id}: \n" \
               f"Place: {self.place}\n" \
               f"Points: {self.points}\n" \
               f"A joué contre: {self.opponents} \n"

    def player_to_dict(self):
        """
        convert an actor into a dictionnary
        :return:
        """
        string_attributes = ['name', 'tournament_id', 'player_id', 'rank', 'ranking', 'points', 'place']
        serialized_player = {}
        for attribute in string_attributes:
            serialized_player[attribute] = self.__getattribute__(attribute)
        # no_string_attributes = ['actor', 'opponents']
        serialized_player['actor'] = self.actor.actor_to_dict()
        serialized_player['opponents'] = list_to_str_space(self.opponents)
        return serialized_player


    def dict_to_player(self, dictio):
        """
        convert a dictionnary into an actor
        :return:
        """

        pass

if __name__ == "__main__":
    import datetime
    acteur1 = Actor("Skywalker", "Anakin", datetime.date(41, 5, 6), "M", 8)       # 2
    acteur2 = Actor("Skywalker", "Luke", datetime.date(19, 12, 7), "M", 21)       # 3

    joueur1 = Player(acteur1, "00000001", 1)
    joueur2 = Player(acteur2, "00000001", 2)

    print(joueur1.player_to_dict())
    print(acteur2.actor_to_dict())