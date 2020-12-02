import pytest
import front_matter as fm
import categories as cat
import pprint as pp


def test_fetch_note_meta():
    result_dict = {}
    result_dict['title'] = 'Test post'
    result_dict['author'] = 'Luke'
    file = 'test.md'
    assert fm.fetch_note_meta(file) == result_dict


def test_generate_note_dict():
    my_category_dict = cat.category_dict.copy()
    # Temporarily not using that key. 
    del my_category_dict['Machine Learning']
    expected = fm.generate_note_dict(my_category_dict)




# author: Luke
# title: Bayesian Statistics
