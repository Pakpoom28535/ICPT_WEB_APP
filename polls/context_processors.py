from .models import * 
def name_context(request):
    try:
        name = f" {request.user.first_name} {request.user.last_name}"
        # user_profile = UserProfile.objects.filter(user__id=request.user.id).first()
        # user_id= user_profile.UserProfile_id
        user_id= request.user.id
        staff = request.user.is_staff
        print(name,staff)
    except:
        name=""
        user_id=""
        staff = ""
    return {'name': name,'id':user_id,'staff':staff}