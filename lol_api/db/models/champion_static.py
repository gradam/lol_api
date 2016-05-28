# encoding: utf-8
from sqlalchemy import Column, Integer, Text, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from lol_api.db.db import Base
from lol_api.db.utils import db_text_to_list, list_to_db_text


class ChampionStatic(Base):
    __tablename__ = 'champions_static'

    id = Column(Integer, primary_key=True)
    _enemy_tips = Column(Text)
    _ally_tips = Column(Text)

    stats = relationship('ChampionStats')
    tags = relationship('ChampionTags')
    recomended = relationship('Images')

    @hybrid_property
    def enemy_tips(self):
        return db_text_to_list(self.enemy_tips)

    @enemy_tips.setter
    def enemy_tips(self, tips):
        self._enemy_tips = list_to_db_text(tips)

    @hybrid_property
    def ally_tips(self):
        return db_text_to_list(self.ally_tips)

    @ally_tips.setter
    def ally_tips(self, tips):
        self._ally_tips = list_to_db_text(tips)


class ChampionStats(Base):
    __tablename__ = 'champion_stats'

    champion_id = Column(Integer, ForeignKey('champions_static.id'), primary_key=True)
    attack_range = Column(Float, nullable=False)
    mp_per_level = Column(Float, nullable=False)
    mp = Column(Float, nullable=False)
    attack_damage = Column(Float, nullable=False)
    hp = Column(Float, nullable=False)
    hp_per_level = Column(Float, nullable=False)
    attack_damage_per_level = Column(Float, nullable=False)
    armor = Column(Float, nullable=False)
    mp_regen_per_level = Column(Float, nullable=False)
    hp_regen = Column(Float, nullable=False),
    crit_per_level = Column(Float, nullable=False)
    spell_block_per_level = Column(Float, nullable=False)
    mp_regen = Column(Float, nullable=False)
    attack_speed_per_level = Column(Float, nullable=False)
    spell_block = Column(Float, nullable=False)
    move_speed = Column(Float, nullable=False)
    attack_speed_off_set = Column(Float, nullable=False)
    crit = Column(Float, nullable=False)
    hp_regen_per_level = Column(Float, nullable=False)
    armor_per_level = Column(Float, nullable=False)

    champion = relationship("ChampionStatic")


class ChampionTags(Base):
    __tablename__ = 'champions_tags'

    champion_id = Column(Integer, ForeignKey('champions_static.id'), primary_key=True)
    assasin = Column(Boolean, deafult=False)
    fighter = Column(Boolean, default=False)
    mage = Column(Boolean, default=False)
    support = Column(Boolean, default=False)
    tank = Column(Boolean, default=False)
    marksman = Column(Boolean, default=False)

    champion = relationship('ChampionStatic')


class Images(Base):
    __tablename__ = 'champion_images'

    w = Column(Integer)
    full = Column(Text, primary_key=True)
    sprite = Column(Text)
    group = Column(Text)
    h = Column(Integer)
    y = Column(Integer)
    x = Column(Integer)

