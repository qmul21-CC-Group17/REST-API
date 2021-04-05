#defining endpoints for get_jobs method 
from flask import request, jsonify
import requests
from app.main.dto import JobDto
from app.main.decorator import login_required
from app.main.service.auth import AuthHelper

from flask_restx import Resource


api = JobDto.api

parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/get_jobs', methods=['GET'])
class JobList(Resource):
    @api.doc('Search job for current user')
    @api.expect(parser)
    @login_required
    def get(self): # parameters sent in the request made to the external api
        """Search job for current user"""
        resp = AuthHelper.get_loged_in_user(request)
        if resp[0]['status'] == 'success':
            user_data = resp[0]['user_data']
            print(user_data)
            job_template = 'https://jobs.github.com/positions.json?description={job}&location={loc}&full_time={fu}' # actual request format for github jobs public api
            desc = user_data['keyword']
            location = user_data['location']
            desc = desc.replace(" ","+")
            ft = user_data['full_time']
            job_url = job_template.format(job = desc, loc = location, fu = ft)
            resp = requests.get(job_url)
            print(jsonify(resp.json()))
            if resp.ok:
                if len(resp.json()) == 0:
                    return jsonify({'message': 'No jobs found'}), 200
                else:
                    return resp.json(), 200
            else:
                print(resp.reason)

    



