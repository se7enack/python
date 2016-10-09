#!/usr/bin/python

# This is the REST API wrapper for the Python scrpits contained in this directory.

import string, random, datetime, time, hmac, hashlib, base64, requests, json, re, sys

class REST:

	# Tracks current output
	results = {}
	status_code = 0
	encoding = ''
	headers = ''

	def __init__(self, secretKey, accessKey, url, timeDelta=0):
		self._secretKey = secretKey
		self._accessKey = accessKey
		self._url = url
		self._timeDelta = timeDelta

	def _stripAndEncodeApiResource(self, apiResource): 
		return re.sub(self._url, '', apiResource.encode('ascii', 'ignore'))

	def _createCanonicalizedHeaders(self, headers):
		return ""
    
	def _addAuthHeaders(self, restVerb, contentType, apiResource, canonicalizedHeaders={}, params={}):
		
		now = datetime.datetime.utcnow() + datetime.timedelta(minutes=self._timeDelta)
                timeStamp = now.strftime("%a, %d %b %Y %H:%M:%S GMT")

		# Create the string to sign, comprising five fields, each terminated by a newline
		# All field must be in ASCII format
		stringToSign = restVerb.encode('ascii', 'ignore') + "\n"	# GET, POST, PATCH, etc, in all CAPS
		stringToSign += contentType.encode('ascii', 'ignore') + "\n"	# The MIME type of data being sent.
		stringToSign += timeStamp.encode('ascii', 'ignore') + "\n"	# The timestamp as calculated above
		stringToSign += canonicalizedHeaders.encode('ascii', 'ignore') + "\n"		# The canonicalized headers as calculated above
		stringToSign += apiResource.encode('ascii', 'ignore') + "\n"	# The resource string, all lowercase
		for item in params.keys():					# The url parms separted by :
		  stringToSign += item.encode('ascii', 'ignore') + ":" + params[item].encode('ascii', 'ignore') + "\n"

		signature = base64.b64encode(hmac.new(key=self._secretKey, msg=unicode(stringToSign, "utf-8"), digestmod=hashlib.sha256).digest())
		
		return {'Date': timeStamp, 
				'x-ms-authorization': 'CloudApplication AccessKey=' + self._accessKey + ' SignatureType=HMAC-SHA256 Signature=' + signature }

	def _reqREST(self, restVerb, apiResource, canonicalizedHeaders='', headers={}, data={}, params={}, dryRun=False, printJSON=False):

		self.results = {}

		if 'Content-Type' in headers.keys():
			contentType = headers['Content-Type']
		else:
			contentType = ''

		#Strip out the URL if it has been passed in with the apiResource
		apiResource = self._stripAndEncodeApiResource(apiResource)
	
		#Add the authentication headers for this request
		headers.update(self._addAuthHeaders(restVerb=restVerb, contentType=contentType, 
										apiResource=apiResource, canonicalizedHeaders=canonicalizedHeaders, params=params))	
		#Make the REST call if dryRun is set to False
		if dryRun == False:
			r = requests.request(restVerb, self._url + apiResource, headers=headers, data=json.dumps(data), params=params)
			self.status_code = r.status_code
			self.encoding = r.encoding
			self.headers = r.headers
		
			#Return JSON object if not one of the following errors 

			print self.status_code

			if (self.status_code == 204):
				print "Successfully Deleted"
                        elif (self.status_code == 200):
                                print "Success"
                                try:
                                	self.results = r.json()
                                except:
                                	self.results = []
                        elif (self.status_code == 401):
                                print "ERROR: Access Key and/or Secret Key is invalid or missing"
                        elif (self.status_code == 404):
                                print "ERROR: Not Found"
                        elif (self.status_code == 500):
                                print "ERROR: Check log file for more details"
                        elif (self.status_code == 503):
                                print "ERROR, Service Unavailable: Check log file for more details"
                        elif (self.status_code == 504):
                                print "ERROR: Endpoint not reachable"
                        else :
                        	print "ERROR: Check log file for more details"
                        	quit()
		else:
			self.results['method'] = restVerb
			self.results['url'] = self._url + apiResource
			self.results['headers'] = headers
			self.results['data'] = data
			self.results['params'] = params

		#Return the results as a dictionary object if printJSON is set to False
		if printJSON == False:
			return self.results

		#Otherwise, print the JSON object, and return nothing (this is useful for interactive discovery)
		else:
			print json.dumps(self.results,indent=3)
			return

	def _getContentTypes(self, restVerb, apiResource):
		headers = {}

		if restVerb in ('GET','OPTIONS'):
			return headers

		#Make a REST OPTIONS call to the API Resource
		types = self._reqREST('OPTIONS', apiResource)

		if 'methods' in types.keys():
			if restVerb in types['methods'].keys():
				#All valid resources will have an Accept MIME type
				headers['Accept'] = types['methods'][restVerb]['responseType']

				#But not all will have a Content-type
				if 'requestType' in types['methods'][restVerb].keys():
					headers['Content-type'] = types['methods'][restVerb]['requestType']
		return headers

	def request(self, restVerb, apiResource, headers, data={}, params={}, dryRun=False, printJSON=False):
		#print "data:" + data
		return self._reqREST(restVerb=restVerb, 
					apiResource=apiResource,
					# headers=self._getContentTypes(restVerb=restVerb, apiResource=apiResource),
					headers=headers,
					data=data,
					params=params,
					dryRun=dryRun,
					printJSON=printJSON)      

if __name__ == "__main__":
	pass
