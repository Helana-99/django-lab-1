from django.shortcuts import render, redirect, get_object_or_404
from .models import Tracking
from .forms import TrackingForm

def tracking_list(request):
    trackings = Tracking.objects.all()
    return render(request, 'tracking/list.html', {'trackings': trackings})

def tracking_create(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracking_list')
    else:
        form = TrackingForm()
    return render(request, 'tracking/form.html', {'form': form})

def tracking_update(request, id):
    tracking = get_object_or_404(Tracking, id=id)
    if request.method == 'POST':
        form = TrackingForm(request.POST, instance=tracking)
        if form.is_valid():
            form.save()
            return redirect('tracking_list')
    else:
        form = TrackingForm(instance=tracking)
    return render(request, 'tracking/form.html', {'form': form})

def tracking_delete(request, id):
    tracking = get_object_or_404(Tracking, id=id)
    if request.method == 'POST':
        tracking.delete()
        return redirect('tracking_list')
    return render(request, 'tracking/confirm_delete.html', {'tracking': tracking})

def tracking_details(request, id):
    tracking = get_object_or_404(Tracking, id=id)
    return render(request, 'tracking/details.html', {'tracking': tracking})
