import set_game
import pytest


def test_cards_1():
	"""Если ловится ошибка, то тест успешный
	Если ошибки нет, то тест фейлится"""
	with pytest.raises(ValueError):
		set_game.create_cards()

def test_cards_2():
	assert not isinstance(set_game.create_cards(), bool)

def test_set():
	"""Если получили сет, то тест успешный
	Если сета нет, то тест фейлится"""
	
	assert set_game.check_set(set_game.create_cards()) == True
