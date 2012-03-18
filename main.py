import urllib
access_token='AAACb8n2uW5MBAIcNU17sEZBsHnnBZBXw7E3DXCSiSj7S3AZBpxPXzfNknRIjzUDorsg1MHHi4LeojEIOC2CMDGmmZBug5pSgYoENCZAOJhAZDZD'
url='https://graph.facebook.com/526757727?access_token='+access_token
friends_url='https://graph.facebook.com/632735851/friends?access_token='+access_token

if __name__ == "__main__":
	# Get authorization set up and create the OAuth client
	
	##############################
	# Getting Data from FACEBOOK #
	##############################
	
	# Simple profile call
	response = urllib.urlopen(url).read()
	friends= urllib.urlopen(friends_url).read()
	print friends