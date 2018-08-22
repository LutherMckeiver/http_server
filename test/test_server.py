import pytest
import requests as req


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000')
    assert 'cowsay' in str(response.text)


def test_server_get_bad_requests():
    response = req.get('http://127.0.0.1:5000/dad')
    assert response.status_code == 404


def test_server_get_cow_route_good_status():
    response = req.get('http://127.0.0.1:5000/cow?msg=HelloWorld')
    assert response.status_code == 200
    assert 'HelloWorld' in str(response.text)


def test_server_get_cow_route_bad_status_with_data():
    response = req.get('http://127.0.0.1:5000/cow?blargle=yargle')
    assert response.status_code == 400


def test_server_get_cow_route_bad_status_with_no_data():
    response = req.get('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_server_post_cow_good_status():
    response = req.post('http://127.0.0.1:5000/cow?msg=HelloWorld')
    assert response.status_code == 200
    assert 'HelloWorld' in response.text


def test_server_post_cow_bad_path():
    response = req.post('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_server_post_cow_bad_request():
    response = req.post('http://127.0.0.1:5000/cow?type=HelloWorld&Glargle=Yargle')
    assert response.status_code == 400


def test_server_route_method_dne():
    response = req.put('http://127.0.0.1:5000/cow')
    assert response.status_code == 501
