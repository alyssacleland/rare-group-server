from rareapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User Account
    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']
    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()
    # If authentication was successful, respond with their info
    if user is not None:
        data = {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'bio': user.bio,
            'profile_image_url': user.profile_image_url,
            'active': user.active,
            'is_staff': user.is_staff
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''
    # Now save the user info in the rareapi_user table
    user = User.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        bio=request.data.get('bio', ''),
        profile_image_url=request.data.get('profile_image_url', ''),
        email=request.data['email'],
        active=request.data.get('active', True),
        is_staff=request.data.get('is_staff', False),
        uid=request.data['uid']
    )
    # Return the user info to the client
    data = {
        'id': user.id,
        'uid': user.uid,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'bio': user.bio,
        'profile_image_url': user.profile_image_url,
        'active': user.active,
        'is_staff': user.is_staff
    }
    return Response(data)