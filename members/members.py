from flask import Blueprint, make_response, request
from mysql import mysql
from flask import jsonify
import pymysql
from constant import MESSAGE

members_bp = Blueprint('members_bp', __name__)


@members_bp.route('/members/getAll', methods=['GET'])
def get_all():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM members")
        data = cur.fetchall()
        _obj = {
            'result': {
                'status': 'Ok',
                'data': data,
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    except Exception as e:
        print('exception',e)
        _obj = {
            'result': {
                'message': MESSAGE.get('SERVER_ERROR'),
                'status': 'NotOk',
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    finally:
        cur.close()
        conn.close()



@members_bp.route('/members/getOne/<string:membership_number>', methods=['GET'])
def get_one(membership_number):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT * FROM members WHERE membership_number = {membership_number}"
        cur.execute(query)
        data = cur.fetchone()
        _obj = {
            'result': {
                'status': 'Ok',
                'data': data,
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    except Exception as e:
        print('exception', e)
        _obj = {
            'result': {
                'message': MESSAGE.get('SERVER_ERROR'),
                'status': 'NotOk',
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    finally:
        cur.close()
        conn.close()


@members_bp.route('/members/getByGender', methods=['GET'])
def get_by_gender():
    try:
        gender1 = request.args.get('gender1')
        gender2 = request.args.get('gender2')
        genderList = []
        if gender1 is not None:
            genderList.append(gender1)
        if gender2 is not None:
            genderList.append(gender2)
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT * FROM members WHERE gender in ({','.join(map(str, genderList))})"
        cur.execute(query)
        data = cur.fetchall()
        _obj = {
            'result': {
                'status': 'Ok',
                'data': data,
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    except Exception as e:
        print('exception', e)
        _obj = {
            'result': {
                'message': MESSAGE.get('SERVER_ERROR'),
                'status': 'NotOk',
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    finally:
        cur.close()
        conn.close()


@members_bp.route('/members/getList', methods=['POST'])
def get_list():
    try:
        payload = request.get_json()
        idList = payload.get('idList')
        idList.append('null')
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT * FROM members WHERE membership_number IN ({','.join(map(str, idList))})"
        cur.execute(query)
        data = cur.fetchall()
        _obj = {
            'result': {
                'status': 'Ok',
                'data': data,
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    except Exception as e:
        print('exception', e)
        _obj = {
            'result': {
                'message': MESSAGE.get('SERVER_ERROR'),
                'status': 'NotOk',
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    finally:
        cur.close()
        conn.close()



@members_bp.route('/members/countMembers', methods=['GET'])
def count_members():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT COUNT(membership_number) as total_members FROM members"
        cur.execute(query)
        data = cur.fetchone()
        _obj = {
            'result': {
                'status': 'Ok',
                'data': data,
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    except Exception as e:
        print('exception', e)
        _obj = {
            'result': {
                'message': MESSAGE.get('SERVER_ERROR'),
                'status': 'NotOk',
            }
        }
        resp = make_response(jsonify(_obj), 200)
        return resp
    finally:
        cur.close()
        conn.close()

