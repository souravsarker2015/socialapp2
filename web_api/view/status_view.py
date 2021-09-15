from django.http import JsonResponse

from web_api.models import StatusLike


def status_like(request, id):
    if request.user.is_anonymous:
        return JsonResponse({"status": False, "message": "Please Login"})

    you_like = True
    sl = StatusLike.objects.filter(user=request.user, status_id=id).first()
    if sl is None:
        StatusLike.objects.create(user=request.user, status_id=id)
    else:
        you_like = False
        StatusLike.objects.filter(user=request.user, status_id=id).delete()

    data = {
        "status_id": id,
        'total_like': len(StatusLike.objects.filter(status_id=id)),
        'you_like': you_like
    }
    return JsonResponse({"status": True, "data": data})
