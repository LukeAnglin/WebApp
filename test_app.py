import pytest
import categories as cat 
import pprint as pp

def test_fetch_note_meta():
    result_dict = {}
    result_dict['title'] = 'Test post'
    result_dict['author'] = 'Luke'
    file = 'test.md'
    assert cat.fetch_note_meta(file) == result_dict






# author: Luke
# title: Bayesian Statistics
