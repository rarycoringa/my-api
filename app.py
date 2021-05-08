from flask import Flask, jsonify

from datetime import date

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def index():
    response = {
        'title': 'My API',
        'version': 'v1.0.0',
        'url': 'api.rary.dev'
    }
    return jsonify(response)

@app.route('/experiences', methods=['GET'])
def experiences():
    response = [
        {
            'company': 'DevGrid',
            'experience': [
                {
                    'title': 'Python Backend Developer',
                    'employment': 'Full-time',
                    'location': {
                        'city': 'London',
                        'country': 'United Kingdom'
                    },
                    'period': {
                        'start': date(2021, 4, 6),
                        'currently': True,
                        'end': None
                    }
                }
            ]
        },
        {
            'company': 'STI - UFRN',
            'experience': [
                {
                    'title': 'Python Developer',
                    'employment': 'Scholarship',
                    'location': {
                        'city': 'Natal',
                        'country': 'Brazil'
                    },
                    'period': {
                        'start': date(2020, 11, 2),
                        'currently': False,
                        'end': date(2021, 3, 31)
                    }
                }
            ]
        },
        {
            'company': 'EJECT',
            'experience': [
                {
                    'title': 'Project Advisor',
                    'employment': None,
                    'location': {
                        'city': 'Natal',
                        'country': 'Brazil'
                    },
                    'period': {
                        'start': date(2019, 11, 4),
                        'currently': False,
                        'end': date(2020, 10, 30)
                    }
                }
            ]
        },
        {
            'company': 'IFRN',
            'experience': [
                {
                    'title': 'Tutor and Monitor',
                    'employment': 'Scholarship',
                    'location': {
                        'city': 'Mossoró',
                        'country': 'Brazil'
                    },
                    'period': {
                        'start': date(2018, 4, 2),
                        'currently': False,
                        'end': date(2018, 12, 28)
                    }
                }
            ]
        }
    ]
    return jsonify(response)

@app.route('/educations', methods=['GET'])
def educations():
    response = [
        {
            'institution': 'Universidade Federal do Rio Grande do Norte',
            'course': 'Science and Technology',
            'degree': 'Bachelor\'s',
            'location': {
                'city': 'Natal',
                'country': 'Brazil'
            },
            'period': {
                'start': date(2019, 2, 11),
                'currently': True,
                'end': None
            }
        },
    ]
    return jsonify(response)
