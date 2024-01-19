def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'naver':
        user.name = user.username 
        user.save()
        