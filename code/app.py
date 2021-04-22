#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify,abort
from db import dbstore

import sys

## APP is a WEBService with FLASK
app = Flask(__name__)


## End-Point /particles/
@app.route('/particles/', methods=['GET'])
def astrolake_particles():

	if request.method == 'GET':
		
		lookup= request.args.get("lookup")
		species=request.args.get("species") # Optional

		## Check if lookup param is received (almost)
		if lookup!=None:
			## Check if lookup string is less or equal to 3 chars
			if (len(lookup)>=3):
				db=dbstore.dbmanager()
				particles=db.lookup_particle(term=lookup)
				return jsonify(particles)				
			else:
				entries=[]
		else:
			abort(405)
	else:
		## 405 Method not allowed
		abort(405)


## Main APP
if __name__ == '__main__':
	
	host=str(sys.argv[1])
	port=int(sys.argv[2])

	app.run(debug=False,host=host,port=port)

