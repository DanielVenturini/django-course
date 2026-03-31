from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseBadRequest
from django.http import JsonResponse
from .forms import UserModelForm
from .models import UserModel

def serialize_user(user: UserModel) -> dict:
	return {
		'name': user.name,
		'job': user.job,
		'age': user.age,
		'created_at': user.created_at.isoformat() if user.created_at else None,
		'updated_at': user.updated_at.isoformat() if user.updated_at else None,
		'id': user.id,
	}

def serialize_users(users: list) -> list:
	usersFinal = []
	for user in users:
		usersFinal.append(serialize_user(user))

	return usersFinal

def find_user(name: str, ignore_case: bool) -> dict:
	if name == 'all':
		return list(UserModel.objects.all())

	nameToSearch = name if not ignore_case else name.lower()

	return list(UserModel.objects.filter(name__iexact=name)) if ignore_case else list(UserModel.objects.filter(name__exact=name))

def get_user(name: str, ignore_case: bool) -> HttpResponse:
	finalUserObj = []
	userObj = find_user(name, ignore_case)
	finalUserObj = serialize_users(userObj)

	return JsonResponse(finalUserObj, safe=False) if finalUserObj else HttpResponseNotFound()


def create_user(POST) -> HttpResponse:
	userModelForm = UserModelForm(POST)
	if not userModelForm.is_valid():
		return HttpResponseBadRequest()

	savedModel = userModelForm.save()

	return JsonResponse(serialize_user(savedModel))

def update_user() -> HttpResponse:
	return 'User updated'

def delete_user(name: str, ignore_case: bool) -> HttpResponse:
	userModelToDelete = UserModel.objects.filter(name__iexact=name) if ignore_case else UserModel.objects.filter(name__exact=name)
	usersSerialized = serialize_users(list(userModelToDelete))

	userModelToDelete.delete()
	return JsonResponse(usersSerialized, safe=False)


# requestable viewes
def users(request: HttpRequest, **kwargs: dict) -> HttpResponse:
	name = kwargs.get('name')
	ignore_case = request.GET.get('ignore_case') == 'True'
	match request.method:
		case 'GET':
			name = kwargs.get('name')
			if not name:
				return HttpResponseNotAllowed(['POST', 'PUT', 'DELETE'])
			else:
				return get_user(name, ignore_case)
		case 'POST':
			return create_user(request.POST)
		case 'PUT':
			return update_user()
		case 'DELETE':
			return delete_user(name, ignore_case)


def web_users(request: HttpRequest, **kwargs: dict) -> HttpResponse:
	name = kwargs.get('name')
	# GET on api/users/<str:name>, so simply render
	if request.method == 'GET' and name:
		userObj = find_user(name, request.GET.get('ignore_case'))
		if userObj:
			return render(request, 'viewer-users.html', {'users': serialize_users(userObj)})
		else:
			return HttpResponseNotFound()
	# GET on api/web/users/
	elif request.method == 'GET' and not name:
		return render(request, 'post-users.html', {'userForm': UserModelForm})
	else:
		return HttpResponseNotAllowed(['GET'])