from django.shortcuts import render
import pickle

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

def index(request):
    return render(request,'index.html')

def analyze(request):
    if request.method == "POST":
        fever =float(request.POST.get('fever','default'))
        age =float(request.POST.get('age','default'))
        bodyPain =float(request.POST.get('bodyPain','default'))
        runnyNose =float(request.POST.get('runnyNose','default'))
        diffBreath =float(request.POST.get('diffBreath','default'))
        inputFeatures = [fever,bodyPain,age,runnyNose,diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        infProb = round(infProb * 100)
        params = {'inf':infProb}
        return render(request,'show.html', params)
    return render(request,'index.html')

def contactus(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')