from django.shortcuts import render, redirect

data_dict = {}  # Initialize an empty dictionary to store key-value pairs

def create_view(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        data_dict[key] = value
        return redirect('read')
    return render(request, 'create.html')

def read_view(request):
    return render(request, 'read.html', {'data': data_dict})

def update_view(request, key):
    if request.method == 'POST':
        new_value = request.POST.get('value')
        if key in data_dict:
            data_dict[key] = new_value
            return redirect('read')
    return render(request, 'update.html', {'key': key, 'value': data_dict.get(key, '')})

def delete_view(request, key):
    if key in data_dict:
        del data_dict[key]
    return redirect('read')
