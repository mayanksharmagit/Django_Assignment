from django.shortcuts import render
from .forms import FigureForm
from .utils import number_to_words

def convert_figure(request):
    if request.method == 'POST':
        form = FigureForm(request.POST)
        if form.is_valid():
            figure = form.cleaned_data['figure']
            words = number_to_words(figure)
            return render(request, 'converter/result.html', {'figure': figure, 'words': words})
    else:
        form = FigureForm()
    return render(request, 'converter/index.html', {'form': form})
