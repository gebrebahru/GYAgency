from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Worker, EmployerRequirement
from .forms import AssetForm, WorkerForm, EmployerRequirementForm

def home_page(request):
    assets = Asset.objects.filter(is_paid=True)
    workers = Worker.objects.filter(is_paid=True)
    requirements = EmployerRequirement.objects.filter(is_paid=True)

    search_query = request.GET.get('search', '')
    if search_query:
        assets = assets.filter(location__icontains=search_query)
        workers = workers.filter(skill__icontains=search_query)
        requirements = requirements.filter(location__icontains=search_query)

    asset_form = AssetForm()
    worker_form = WorkerForm()
    employer_form = EmployerRequirementForm()

    if request.method == 'POST':
        if 'submit_asset' in request.POST:
            form = AssetForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.is_paid = True  
                obj.save()
                return redirect('home')

        elif 'submit_worker' in request.POST:
            form = WorkerForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.is_paid = True
                obj.save()
                return redirect('home')

        elif 'submit_employer' in request.POST:
            form = EmployerRequirementForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.is_paid = True
                obj.save()
                return redirect('home')

    context = {
        'house_sales': assets.filter(category='house_sale'),
        'house_rents': assets.filter(category='house_rent'),
        'car_sales': assets.filter(category='car_sale'),
        'land_sales': assets.filter(category='land_sale'),
        'local_workers': workers.filter(worker_type='local'),
        'foreign_workers': workers.filter(worker_type='foreign'),
        'employer_requirements': requirements,
        'asset_form': asset_form,
        'worker_form': worker_form,
        'employer_form': employer_form,
        'search_query': search_query,
    }
    return render(request, 'core/home.html', context)


# 🌟 አዲስ የተጨመረ፦ የፖስቱን ዝርዝር የሚያሳይ እና እይታ የሚቆጥር ቪው
def post_detail(request, obj_type, obj_id):
    if obj_type == 'asset':
        obj = get_object_or_404(Asset, id=obj_id)
    elif obj_type == 'worker':
        obj = get_object_or_404(Worker, id=obj_id)
    elif obj_type == 'employer':
        obj = get_object_or_404(EmployerRequirement, id=obj_id)
    
    # እይታውን በ 1 ጨምርና ሴቭ አድርግ
    obj.views_count += 1
    obj.save()
    
    return render(request, 'core/post_detail.html', {'obj': obj, 'obj_type': obj_type})
def post_detail(request, obj_type, obj_id):
    if obj_type == 'asset':
        obj = get_object_or_404(Asset, id=obj_id)
    elif obj_type == 'worker':
        obj = get_object_or_404(Worker, id=obj_id)
    elif obj_type == 'employer':
        obj = get_object_or_404(EmployerRequirement, id=obj_id)
    
    obj.views_count += 1  # ቁጥሩን በ 1 ይጨምራል
    obj.save()            # ዳታቤዙን ያድሳል
    
    return render(request, 'core/post_detail.html', {'obj': obj, 'obj_type': obj_type})